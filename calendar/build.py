#!/usr/bin/env python3
"""Turn the public sheet tab into events.json and subscribable .ics feeds.

Reads a CSV (a published Google Sheet tab, or a local file) and writes:
  calendar/events.json          what the calendar page shows
  calendar/feeds/all.ics        every town
  calendar/feeds/<town>.ics     one feed per town

Usage:
  SHEET_CSV_URL=https://... python3 calendar/build.py
  python3 calendar/build.py calendar/sample-sheet.csv

The CSV must be the PUBLIC tab only (already filtered to approved events, with
every field the submitter said No to left blank). This script never sees
contact names, phones or emails.
"""
import csv, datetime as dt, difflib, hashlib, html, io, json, os, re, sys, urllib.request
from zoneinfo import ZoneInfo
from dateutil.rrule import rrulestr

HERE = os.path.dirname(os.path.abspath(__file__))
FEEDS = os.path.join(HERE, "feeds")
CAL_NAME = "Along the 299 Events"


def slug(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")


def parse_date(s):
    s = (s or "").strip()
    for fmt in ("%Y-%m-%d", "%m/%d/%Y", "%m/%d/%y", "%B %d, %Y", "%b %d, %Y"):
        try:
            return dt.datetime.strptime(s, fmt).date()
        except ValueError:
            pass
    return None


def parse_time(s):
    s = (s or "").strip().lower().replace(".", "")
    if not s:
        return None
    for fmt in ("%H:%M", "%H:%M:%S", "%I:%M %p", "%I:%M%p", "%I %p", "%I%p"):
        try:
            return dt.datetime.strptime(s, fmt).time()
        except ValueError:
            pass
    return None


def load_rows():
    arg = sys.argv[1] if len(sys.argv) > 1 else None
    url = os.environ.get("SHEET_CSV_URL", "").strip()
    if arg:
        text = open(arg, encoding="utf-8").read()
    elif url:
        req = urllib.request.Request(url, headers={"User-Agent": "calendar-builder"})
        text = urllib.request.urlopen(req, timeout=30).read().decode("utf-8")
    else:
        # No sheet connected yet: use the starter events so the calendar is not empty.
        seed = os.path.join(HERE, "sample-sheet.csv")
        print("No SHEET_CSV_URL set; using sample-sheet.csv until a sheet is connected.")
        text = open(seed, encoding="utf-8").read()
    return list(csv.DictReader(io.StringIO(text)))


def recurring_rows():
    """Monthly events that follow a rule, such as the first Thursday, from recurring.json."""
    path = os.path.join(HERE, "recurring.json")
    if not os.path.exists(path):
        return []
    rows, today = [], dt.date.today()
    for item in json.load(open(path, encoding="utf-8")):
        y, m, made = today.year, today.month, 0
        while made < int(item.get("months", 6)):
            first = dt.date(y, m, 1)
            day = first + dt.timedelta(days=(int(item["weekday"]) - first.weekday()) % 7 + 7 * (int(item["nth"]) - 1))
            if day >= today:
                row = {k: str(v) for k, v in item.items() if k not in ("nth", "weekday", "months")}
                row["date"] = day.isoformat()
                rows.append(row)
                made += 1
            y, m = (y + 1, 1) if m == 12 else (y, m + 1)
    return rows


def clean_rows(rows):
    events, today = [], dt.date.today()
    for n, r in enumerate(rows, start=2):
        r = {(k or "").strip().lower(): (v or "").strip() for k, v in r.items()}
        title = r.get("title", "")
        start = parse_date(r.get("date"))
        if not title and not r.get("date"):
            continue  # blank row
        if not title or not start:
            print("Skipping row %d (needs a title and a date): %r" % (n, title))
            continue
        end = parse_date(r.get("end_date")) or start
        if end < start:
            end = start
        st, et = parse_time(r.get("start_time")), parse_time(r.get("end_time"))
        # drop events that ended more than 60 days ago, so files stay small
        if end < today - dt.timedelta(days=60):
            continue
        site = r.get("website", "")
        if site and not re.match(r"https?://", site, re.I):
            site = "https://" + site
        events.append({
            "id": hashlib.sha1((title + start.isoformat()).encode()).hexdigest()[:12],
            "title": title,
            "date": start.isoformat(),
            "end_date": end.isoformat(),
            "start_time": st.strftime("%H:%M") if st else "",
            "end_time": et.strftime("%H:%M") if et else "",
            "town": r.get("town", "") or "Other",
            "place": r.get("place", ""),
            "address": r.get("address", ""),
            "website": site,
            "description": r.get("description", ""),
            "free": r.get("free", "").lower() in ("yes", "y", "true", "free"),
            "category": r.get("category", ""),
            "source": r.get("source", ""),
            "source_url": r.get("source_url", ""),
        })
    events.sort(key=lambda e: (e["date"], e["start_time"] or "00:00", e["title"]))
    return events


# ---------- Importing other people's calendar feeds ----------
TOWNS = ["Eureka", "Arcata", "McKinleyville", "Blue Lake", "Fortuna", "Ferndale", "Trinidad",
         "Willow Creek", "Hoopa", "Orleans", "Salyer", "Burnt Ranch", "Big Bar", "Junction City",
         "Weaverville", "Hayfork"]
LOCAL_TZ = ZoneInfo("America/Los_Angeles")


def read_source(loc):
    if re.match(r"https?://|webcal://", loc, re.I):
        loc = re.sub(r"^webcal://", "https://", loc, flags=re.I)
        req = urllib.request.Request(loc, headers={"User-Agent": "calendar-builder"})
        return urllib.request.urlopen(req, timeout=30).read().decode("utf-8", "replace")
    return open(loc, encoding="utf-8").read()


def unescape(v):
    return (v.replace("\\n", "\n").replace("\\N", "\n").replace("\\,", ",")
             .replace("\\;", ";").replace("\\\\", "\\"))


def parse_ics(text):
    """Return a list of dicts of VEVENT properties: name -> (params, value)."""
    lines = []
    for raw in text.replace("\r\n", "\n").split("\n"):
        if raw[:1] in (" ", "\t") and lines:
            lines[-1] += raw[1:]
        else:
            lines.append(raw)
    events, cur = [], None
    for ln in lines:
        if ln == "BEGIN:VEVENT":
            cur = {}
        elif ln == "END:VEVENT":
            if cur is not None:
                events.append(cur)
            cur = None
        elif cur is not None and ":" in ln:
            head, val = ln.split(":", 1)
            parts = head.split(";")
            name = parts[0].upper()
            if name == "EXDATE" and name in cur:
                val = cur[name][1] + "," + val
            cur[name] = (dict(p.split("=", 1) for p in parts[1:] if "=" in p), val)
    return events


def ics_dt(prop):
    """('YYYY-MM-DD', 'HH:MM' or '') in local time, from a DTSTART/DTEND property."""
    params, v = prop
    v = v.strip()
    if params.get("VALUE") == "DATE" or re.fullmatch(r"\d{8}", v):
        d = dt.datetime.strptime(v[:8], "%Y%m%d").date()
        return d, None
    d = dt.datetime.strptime(v.rstrip("Z"), "%Y%m%dT%H%M%S")
    if v.endswith("Z"):
        d = d.replace(tzinfo=dt.timezone.utc).astimezone(LOCAL_TZ).replace(tzinfo=None)
    return d.date(), d.time()


def plain(s, limit=300):
    s = html.unescape(re.sub(r"<[^>]+>", " ", s or ""))
    s = re.sub(r"\s+", " ", s).strip()
    return s if len(s) <= limit else s[:limit].rsplit(" ", 1)[0] + "..."


def occurrences(ev, sd, st, today, horizon=90, cap=60):
    """Dates a repeating event falls on, from today to `horizon` days ahead."""
    rule = ev["RRULE"][1].strip()
    rule = re.sub(r"(UNTIL=\d{8}T\d{6})Z", r"\1", rule)
    rule = re.sub(r"UNTIL=(\d{8})(?!T)", r"UNTIL=\1T235959", rule)
    start = dt.datetime.combine(sd, st or dt.time(0, 0))
    skip = set()
    if "EXDATE" in ev:
        skip = {x.strip()[:8] for x in ev["EXDATE"][1].split(",") if x.strip()}
    try:
        rr = rrulestr(rule, dtstart=start)
        lo = dt.datetime.combine(today, dt.time(0, 0))
        hi = lo + dt.timedelta(days=horizon)
        found = [d.date() for d in rr.between(lo, hi, inc=True) if d.strftime("%Y%m%d") not in skip]
    except (ValueError, TypeError):
        return [sd] if sd >= today else []
    return found[:cap]


def events_from_ics(text, source):
    out, today = [], dt.date.today()
    for ev in parse_ics(text):
        if "SUMMARY" not in ev or "DTSTART" not in ev:
            continue
        try:
            sd, st = ics_dt(ev["DTSTART"])
            if "DTEND" in ev:
                ed, et = ics_dt(ev["DTEND"])
            else:
                ed, et = sd, None
        except ValueError:
            continue
        if st is None:                      # all-day: DTEND is the day after the last day
            ed = max(sd, ed - dt.timedelta(days=1)); et = None
        elif ed < sd:
            ed = sd
        span = ed - sd
        if "RRULE" in ev:
            days = occurrences(ev, sd, st, today)
        elif ed < today - dt.timedelta(days=60):
            continue
        else:
            days = [sd]
        loc = unescape(ev.get("LOCATION", ({}, ""))[1]).strip()
        town = next((t for t in TOWNS if t.lower() in loc.lower()), source.get("default_town", "Other"))
        parts = [p.strip() for p in loc.split(",") if p.strip()]
        place = parts[0] if parts else ""
        address = parts[1] if len(parts) > 1 and re.match(r"\d", parts[1]) else ""
        if place and re.match(r"\d", place):  # location was only a street address
            place, address = "", place
        title = plain(unescape(ev["SUMMARY"][1]), 120)
        for day in days:
            out.append({
                "id": hashlib.sha1((source["name"] + title + day.isoformat()).encode()).hexdigest()[:12],
                "title": title,
                "date": day.isoformat(), "end_date": (day + span).isoformat(),
                "start_time": st.strftime("%H:%M") if st else "",
                "end_time": et.strftime("%H:%M") if (st and et) else "",
                "town": town, "place": place, "address": address,
                "website": ev.get("URL", ({}, ""))[1].strip(),
                "description": plain(unescape(ev.get("DESCRIPTION", ({}, ""))[1])),
                "free": False, "category": "", "source": source["name"],
                "source_url": source.get("page", ""),
            })
    return out


def norm_title(t):
    t = re.sub(r"[^a-z0-9 ]", " ", t.lower())
    return " ".join(w for w in t.split() if w not in ("annual", "the", "a", "an", "of", "and"))


def minutes(t):
    return int(t[:2]) * 60 + int(t[3:5]) if t else None


def is_duplicate(a, b):
    if a["date"] != b["date"]:
        return False
    if difflib.SequenceMatcher(None, norm_title(a["title"]), norm_title(b["title"])).ratio() >= 0.75:
        return True
    ma, mb = minutes(a["start_time"]), minutes(b["start_time"])
    return bool(a["place"] and a["place"].lower() == b["place"].lower()
                and ma is not None and mb is not None and abs(ma - mb) <= 30)


def import_sources(sheet_events):
    path = os.environ.get("SOURCES_FILE") or os.path.join(HERE, "sources.json")
    if not os.path.exists(path):
        return sheet_events
    try:
        old = json.load(open(os.path.join(HERE, "events.json"), encoding="utf-8")).get("events", [])
    except (OSError, ValueError):
        old = []
    merged = list(sheet_events)  # the sheet always wins over an imported duplicate
    for src in json.load(open(path, encoding="utf-8")):
        url = src.get("url") or os.environ.get(src.get("url_env", ""), "").strip()
        if not url:
            print("%s: no feed address set (%s); keeping its previous events." % (src["name"], src.get("url_env", "url")))
            keep = [e2 for e2 in old if e2.get("source") == src["name"]]
            merged += [e for e in keep if not any(is_duplicate(e, m) for m in merged)]
            continue
        try:
            got = events_from_ics(read_source(url), src)
        except Exception as e:  # keep the last good copy of this source's events
            print("Could not read %s (%s); keeping its previous events." % (src["name"], e))
            got = [e2 for e2 in old if e2.get("source") == src["name"]]
        skip_words = [w.lower() for w in src.get("exclude", [])]
        added = skipped = 0
        for e in got:
            if any(w in e["title"].lower() for w in skip_words):
                skipped += 1
            elif any(is_duplicate(e, m) for m in merged):
                skipped += 1
            else:
                merged.append(e); added += 1
        print("%s: %d new, %d duplicates skipped" % (src["name"], added, skipped))
    return merged


# ---------- ICS ----------
def esc(s):
    return (s.replace("\\", "\\\\").replace(";", "\\;").replace(",", "\\,")
             .replace("\r\n", "\\n").replace("\n", "\\n"))


def fold(line):
    out, b = [], line.encode("utf-8")
    while len(b) > 74:
        cut = 74
        while cut > 0 and (b[cut] & 0xC0) == 0x80:
            cut -= 1
        out.append(b[:cut].decode("utf-8"))
        b = b[cut:]
        b = b" " + b
    out.append(b.decode("utf-8"))
    return "\r\n".join(out)


def ics_for(events, name):
    stamp = dt.datetime.now(dt.timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    L = ["BEGIN:VCALENDAR", "VERSION:2.0", "PRODID:-//Community Calendar//EN",
         "CALSCALE:GREGORIAN", "METHOD:PUBLISH", "X-WR-CALNAME:" + esc(name),
         "X-WR-TIMEZONE:America/Los_Angeles",
         "REFRESH-INTERVAL;VALUE=DURATION:PT4H", "X-PUBLISHED-TTL:PT4H"]
    for e in events:
        s = dt.date.fromisoformat(e["date"])
        en = dt.date.fromisoformat(e["end_date"])
        L += ["BEGIN:VEVENT", "UID:%s@community-calendar" % e["id"], "DTSTAMP:" + stamp]
        if e["start_time"]:
            # Local ("floating") times: 5pm shows as 5pm on every phone.
            st = e["start_time"].replace(":", "") + "00"
            et = (e["end_time"] or e["start_time"]).replace(":", "") + "00"
            if not e["end_time"]:  # no end given: assume one hour
                h = int(e["start_time"][:2]) + 1
                et = "%02d%s00" % (min(h, 23), e["start_time"][3:5])
            L.append("DTSTART:%sT%s" % (s.strftime("%Y%m%d"), st))
            L.append("DTEND:%sT%s" % (s.strftime("%Y%m%d"), et))
            days = (en - s).days + 1
            if days > 1:  # same hours each day
                L.append("RRULE:FREQ=DAILY;COUNT=%d" % days)
        else:
            L.append("DTSTART;VALUE=DATE:" + s.strftime("%Y%m%d"))
            L.append("DTEND;VALUE=DATE:" + (en + dt.timedelta(days=1)).strftime("%Y%m%d"))
        L.append("SUMMARY:" + esc(e["title"]))
        loc = ", ".join(x for x in (e["place"], e["address"]) if x) or e["town"]
        L.append("LOCATION:" + esc(loc))
        desc = e["description"]
        if e["website"]:
            desc = (desc + "\n" if desc else "") + e["website"]
        if desc:
            L.append("DESCRIPTION:" + esc(desc))
        if e["website"]:
            L.append("URL:" + e["website"])
        L.append("END:VEVENT")
    L.append("END:VCALENDAR")
    return "\r\n".join(fold(x) for x in L) + "\r\n"


def inject_jsonld(events):
    """Write schema.org Event data into index.html so search engines can read each event."""
    path = os.path.join(HERE, "index.html")
    if not os.path.exists(path):
        return
    html_text = open(path, encoding="utf-8").read()
    start, end = "<!-- EVENTS-JSONLD:START -->", "<!-- EVENTS-JSONLD:END -->"
    if start not in html_text or end not in html_text:
        return
    today = dt.date.today()
    items = []
    for e in events:
        s_d, e_d = dt.date.fromisoformat(e["date"]), dt.date.fromisoformat(e["end_date"])
        if e_d < today or s_d > today + dt.timedelta(days=120):
            continue
        def stamp(d, t):
            if not t:
                return d.isoformat()
            return dt.datetime.combine(d, dt.time(int(t[:2]), int(t[3:5])), tzinfo=LOCAL_TZ).isoformat()
        place = {"@type": "Place", "name": e["place"] or e["town"],
                 "address": {"@type": "PostalAddress", "addressLocality": e["town"], "addressRegion": "CA",
                             "addressCountry": "US"}}
        if e["address"]:
            place["address"]["streetAddress"] = e["address"]
        item = {"@context": "https://schema.org", "@type": "Event", "name": e["title"],
                "startDate": stamp(s_d, e["start_time"]),
                "endDate": stamp(e_d, e["end_time"] or e["start_time"]) if e["start_time"] else e_d.isoformat(),
                "eventStatus": "https://schema.org/EventScheduled",
                "eventAttendanceMode": "https://schema.org/OfflineEventAttendanceMode",
                "location": place}
        if e["description"]:
            item["description"] = e["description"]
        if e["website"]:
            item["url"] = e["website"]
        if e["free"]:
            item["isAccessibleForFree"] = True
        items.append(item)
        if len(items) >= 150:
            break
    block = '<script type="application/ld+json">' + json.dumps(items, ensure_ascii=False).replace("<", "\\u003c") + "</script>"
    new = html_text[: html_text.index(start) + len(start)] + "\n" + block + "\n" + html_text[html_text.index(end):]
    if new != html_text:
        open(path, "w", encoding="utf-8").write(new)


def write(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    old = open(path, encoding="utf-8", newline="").read() if os.path.exists(path) else None
    # keep files byte-identical when nothing real changed, so no needless commits
    strip = lambda t: re.sub(r"(DTSTAMP:|\"updated\": )[^\r\n,]*", "", t or "")
    if old is not None and strip(old) == strip(text):
        return
    open(path, "w", encoding="utf-8", newline="").write(text)


def main():
    events = import_sources(clean_rows(load_rows() + recurring_rows()))
    events.sort(key=lambda e: (e["date"], e["start_time"] or "00:00", e["title"]))
    towns = sorted({e["town"] for e in events})
    now = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    write(os.path.join(HERE, "events.json"),
          json.dumps({"updated": now, "towns": towns, "events": events}, indent=1) + "\n")
    inject_jsonld(events)
    write(os.path.join(FEEDS, "all.ics"), ics_for(events, CAL_NAME))
    keep = {"all.ics"}
    for t in towns:
        f = slug(t) + ".ics"
        keep.add(f)
        write(os.path.join(FEEDS, f), ics_for([e for e in events if e["town"] == t], "%s Events" % t))
    for f in os.listdir(FEEDS):
        if f.endswith(".ics") and f not in keep:
            os.remove(os.path.join(FEEDS, f))
    print("%d events, %d towns: %s" % (len(events), len(towns), ", ".join(towns)))


if __name__ == "__main__":
    main()
