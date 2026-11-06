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
import csv, datetime as dt, hashlib, io, json, os, re, sys, urllib.request

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
        print("No SHEET_CSV_URL set and no file given; nothing to do.")
        sys.exit(0)
    return list(csv.DictReader(io.StringIO(text)))


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
        })
    events.sort(key=lambda e: (e["date"], e["start_time"] or "00:00", e["title"]))
    return events


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


def write(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    old = open(path, encoding="utf-8", newline="").read() if os.path.exists(path) else None
    # keep files byte-identical when nothing real changed, so no needless commits
    strip = lambda t: re.sub(r"(DTSTAMP:|\"updated\": )[^\r\n,]*", "", t or "")
    if old is not None and strip(old) == strip(text):
        return
    open(path, "w", encoding="utf-8", newline="").write(text)


def main():
    events = clean_rows(load_rows())
    towns = sorted({e["town"] for e in events})
    now = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    write(os.path.join(HERE, "events.json"),
          json.dumps({"updated": now, "towns": towns, "events": events}, indent=1) + "\n")
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
