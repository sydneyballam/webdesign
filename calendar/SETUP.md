# Community calendar: setup

How it fits together:

    Google Form  ->  Responses sheet (private)  ->  "Public" tab (approved + shared fields only)
                                                        |
                                    published as CSV  -> hourly GitHub Action -> events.json + .ics feeds
                                                        |
                                                 the calendar page (calendar/index.html)

Nothing private ever leaves the Responses tab. Only the Public tab is published.

## 1. Google Form questions (in this order)

Add the questions in exactly this order so the sheet columns match the formula below.
Do not add or reorder questions later without updating the formula.

| Col | Question | Type |
|-----|----------|------|
| B | Event name | Short answer, required |
| C | Date (first day) | Date, required |
| D | Last day (only if it runs more than one day) | Date |
| E | Start time | Time |
| F | End time | Time |
| G | Town | Dropdown: Willow Creek, Hoopa, Burnt Ranch, Big Bar, Weaverville, Eureka, Arcata, McKinleyville, Other |
| H | Place name (for example, Studio 299) | Short answer |
| I | Street address | Short answer |
| J | Show the street address publicly? | Yes / No, required |
| K | Website or Facebook page | Short answer |
| L | Show the website publicly? | Yes / No, required |
| M | Short description | Paragraph |
| N | Is it free? | Yes / No |
| O | Link to your flyer (or email it to us) | Short answer |
| P | Show the flyer publicly? | Yes / No, required |
| Q | Your name (private) | Short answer |
| R | Phone (private) | Short answer |
| S | Email (private) | Short answer |

Add a short note at the top: "Event name, date, time and town are always shown. The other details are shown only where you answer Yes."

Add a Yes/No question for logo and branding permission only when branding is added later.

## 2. The sheet

1. In the form, open Responses and click "Link to Sheets". Name the new tab `Form Responses 1` (the default).
2. In that tab, add a header `Approved` in column T. You type `Yes` in column T for each event you approve.
3. Add a new tab named `Public`.
4. In `Public` row 1, type these headers in A1 to K1:
   `title,date,end_date,start_time,end_time,town,place,address,website,description,free`
5. In `Public!A2`, paste this single formula (untested until the real form exists; I will adjust it when it does):

```
=IFERROR(FILTER({
 'Form Responses 1'!B2:B,
 ARRAYFORMULA(IF('Form Responses 1'!C2:C="","",TEXT('Form Responses 1'!C2:C,"yyyy-mm-dd"))),
 ARRAYFORMULA(IF('Form Responses 1'!D2:D="","",TEXT('Form Responses 1'!D2:D,"yyyy-mm-dd"))),
 ARRAYFORMULA(IF('Form Responses 1'!E2:E="","",TEXT('Form Responses 1'!E2:E,"HH:mm"))),
 ARRAYFORMULA(IF('Form Responses 1'!F2:F="","",TEXT('Form Responses 1'!F2:F,"HH:mm"))),
 'Form Responses 1'!G2:G,
 'Form Responses 1'!H2:H,
 ARRAYFORMULA(IF('Form Responses 1'!J2:J="Yes",'Form Responses 1'!I2:I,"")),
 ARRAYFORMULA(IF('Form Responses 1'!L2:L="Yes",'Form Responses 1'!K2:K,"")),
 'Form Responses 1'!M2:M,
 'Form Responses 1'!N2:N
}, 'Form Responses 1'!T2:T="Yes"), "")
```

Any answer left blank counts as No, so private by default.

## 3. Publish only the Public tab

1. In Sheets: File, Share, Publish to web.
2. Choose the `Public` tab and the format "Comma-separated values (.csv)". Click Publish and copy the link.
3. In the GitHub repo: Settings, Secrets and variables, Actions, New repository secret.
   Name `SHEET_CSV_URL`, value the link.

The published link is readable by anyone who has it. That is fine because the Public tab holds only what people agreed to share.

## 4. Turn it on

- The Action in `.github/workflows/calendar.yml` runs every hour (and on demand from the Actions tab). Scheduled runs only start once this is merged into the main branch.
- In `calendar/index.html`, set `FORM_URL` to the form's link. Until then the Submit buttons stay hidden.

## Other calendars we subscribe to

`calendar/sources.json` lists calendar feeds (`.ics` links) that the hourly build reads and merges in.
Today it holds the Willow Creek Chamber of Commerce feed.

To add one, add an entry with a name, the feed link (a `webcal://` link works, or the `https://` version),
and the town to use when the feed doesn't say:

    {"name": "Studio 299", "url": "https://example.com/feed.ics", "default_town": "Willow Creek"}

How it behaves:
- Events from a feed show "From the <name>" on each card, and link to the event's own page.
- If a feed event matches one already in the sheet (same date, and a very similar title, or the same place within 30 minutes), the sheet version wins and the feed copy is skipped.
- If a feed can't be reached one hour, its last good events stay on the calendar.
- A town is picked by finding a known town name in the event's location text.
- Feed events are trusted and appear without review. The review step is for submissions and Gemini suggestions.

## Suggested events from Gemini

Have Gemini write to a separate tab (for example `Suggested`) with the same columns as the form and a source link. Move a row into `Form Responses 1` (or copy it) and type `Yes` in Approved only after checking the source.

## Test locally

    python3 calendar/build.py calendar/sample-sheet.csv
    cd calendar && python3 -m http.server 8000     # then open http://localhost:8000
