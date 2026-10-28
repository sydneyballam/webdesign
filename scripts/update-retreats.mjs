// Builds jessica-retreats.json from Jessica's Cal.com "Events" (cal.com/events).
// Runs on a schedule in GitHub Actions (see .github/workflows/retreats.yml).
// Every published, visible, non-cancelled Event is a retreat. Seats left = capacity - confirmed guests.
// Needs one setting: CAL_API_KEY (secret).

import { writeFileSync } from 'node:fs';
import { fileURLToPath } from 'node:url';

const API = 'https://api.cal.com/v2';
const VERSION = '2026-05-01';
const DEFAULT_CAPACITY = 10;   // used only if an event has no capacity set in Cal.com

/* ---------- pure logic (tested separately) ---------- */

export function isShown(e) {
    return e.publishedAt && !e.cancelledAt && !e.hidden && (!e.visibility || e.visibility === 'PUBLIC');
}
export function placeOf(e) {
    const loc = (e.locations || []).find(l => l.type === 'address');
    return loc && loc.address ? loc.address : '';
}
export function build({ upcoming, past, now = new Date() }) {
    const retreats = upcoming.filter(isShown).filter(e => new Date(e.endTime) > now).map(e => {
        const capacity = Number(e.capacity) > 0 ? Number(e.capacity) : DEFAULT_CAPACITY;
        const taken = Number(e.confirmedCount || 0);
        const left = Math.max(0, capacity - taken);
        return {
            title: e.title, description: e.description || '', slug: e.slug, url: 'https://cal.com/' + e.slug,
            place: placeOf(e), start: new Date(e.startTime).toISOString(), end: new Date(e.endTime).toISOString(),
            capacity, left, soldOut: left === 0
        };
    }).sort((a, b) => a.start.localeCompare(b.start));
    const archive = past.filter(isShown).map(e => ({ title: e.title, start: new Date(e.startTime).toISOString(), end: new Date(e.endTime).toISOString() }))
        .sort((a, b) => b.start.localeCompare(a.start));
    return { retreats, archive };
}

/* ---------- Cal.com calls ---------- */

async function allEvents(status, key) {
    const out = []; let cursor = '';
    for (let i = 0; i < 20; i++) {
        const r = await fetch(`${API}/events?status=${status}&limit=100${cursor ? '&cursor=' + encodeURIComponent(cursor) : ''}`,
            { headers: { Authorization: 'Bearer ' + key, 'cal-api-version': VERSION } });
        if (!r.ok) throw new Error(`Cal.com ${r.status} for events(${status}): ${(await r.text()).slice(0, 300)}`);
        const j = await r.json(); out.push(...j.data);
        if (!j.pagination || !j.pagination.hasMore) break;
        cursor = j.pagination.nextCursor;
    }
    return out;
}

async function main() {
    const key = process.env.CAL_API_KEY;
    console.log('API key set: ' + Boolean(key));
    if (!key) throw new Error('Set CAL_API_KEY (secret) in the repo settings.');
    const now = new Date();
    const upcoming = await allEvents('upcoming', key);
    console.log(`OK   upcoming events: ${upcoming.length}` + upcoming.map(e => `\n       - ${e.title} (${e.startTime}) capacity=${e.capacity} confirmed=${e.confirmedCount} hidden=${e.hidden} published=${Boolean(e.publishedAt)}`).join(''));
    let past = [];
    try { past = await allEvents('past', key); console.log(`OK   past events: ${past.length}`); }
    catch (e) { console.log('FAIL past events (carrying on): ' + e.message); }
    const data = build({ upcoming, past, now });
    writeFileSync('jessica-retreats.json', JSON.stringify({ updated: now.toISOString(), ...data }, null, 2) + '\n');
    console.log(`Wrote ${data.retreats.length} upcoming and ${data.archive.length} past retreats.`);
}

if (process.argv[1] === fileURLToPath(import.meta.url)) main().catch(e => { console.error(e.message); process.exit(1); });
