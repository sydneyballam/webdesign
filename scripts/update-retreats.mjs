// Builds jessica-retreats.json from Jessica's Cal.com account.
// Runs on a schedule in GitHub Actions (see .github/workflows/retreats.yml).
// A "retreat" is any visible event type that has seats turned on in Cal.com.
// Needs two settings: CAL_API_KEY (secret) and CAL_USERNAME.

import { writeFileSync } from 'node:fs';
import { fileURLToPath } from 'node:url';

const API = 'https://api.cal.com/v2';
const V = { eventTypes: '2026-06-12', slots: '2024-09-04', bookings: '2026-05-01' };
const MAX_PER_RETREAT = 12;

/* ---------- pure logic (tested separately) ---------- */

export function isRetreat(t) {
    const seats = t.seats && !t.seats.disabled ? t.seats.seatsPerTimeSlot : t.seatsPerTimeSlot;
    return !t.hidden && Number(seats) > 0;
}
export function seatsOf(t) {
    return Number(t.seats && !t.seats.disabled ? t.seats.seatsPerTimeSlot : t.seatsPerTimeSlot);
}
// Seats taken in one booking: attendees that are not cancelled/rejected.
export function taken(b) {
    return (b.attendees || []).filter(a => a.status !== 'cancelled' && a.confirmationStatus !== 'rejected').length;
}

// slots: { "2026-11-04": [{start, end, attendeesCount}] }   (open times only)
// bookings: [{eventTypeId, start, end, status, attendees}]
export function build({ eventTypes, slotsByType, upcoming, past, username, now = new Date() }) {
    const retreats = [], archive = [];
    const types = eventTypes.filter(isRetreat);
    const byId = new Map(types.map(t => [t.id, t]));

    for (const t of types) {
        const cap = seatsOf(t);
        const occ = new Map();   // start ISO (ms) -> occurrence
        const key = s => String(new Date(s).getTime());
        for (const day of Object.values(slotsByType[t.id] || {})) {
            for (const s of day) {
                occ.set(key(s.start), { start: new Date(s.start).toISOString(), end: new Date(s.end || s.start).toISOString(), taken: Number(s.attendeesCount || 0) });
            }
        }
        for (const b of upcoming) {
            if (b.eventTypeId !== t.id || b.status === 'cancelled' || b.status === 'rejected') continue;
            const k = key(b.start), n = taken(b);
            const prev = occ.get(k);
            // a booking is the more complete record of who has a seat
            occ.set(k, { start: new Date(b.start).toISOString(), end: new Date(b.end).toISOString(), taken: Math.max(n, prev ? prev.taken : 0) });
        }
        const list = [...occ.values()].filter(o => new Date(o.end) > now).sort((a, b) => a.start.localeCompare(b.start)).slice(0, MAX_PER_RETREAT);
        for (const o of list) {
            const left = Math.max(0, cap - o.taken);
            retreats.push({
                title: t.title, description: t.description || '', slug: t.slug,
                url: t.bookingUrl || `https://cal.com/${username}/${t.slug}`,
                place: placeOf(t), start: o.start, end: o.end, capacity: cap, left, soldOut: left === 0
            });
        }
    }
    const seen = new Set();
    for (const b of past) {
        const t = byId.get(b.eventTypeId);
        if (!t || b.status === 'cancelled' || b.status === 'rejected') continue;
        const k = b.eventTypeId + '|' + new Date(b.start).getTime();
        if (seen.has(k)) continue; seen.add(k);
        archive.push({ title: t.title, start: new Date(b.start).toISOString(), end: new Date(b.end).toISOString() });
    }
    retreats.sort((a, b) => a.start.localeCompare(b.start));
    archive.sort((a, b) => b.start.localeCompare(a.start));
    return { retreats, archive };
}

function placeOf(t) {
    const loc = (t.locations || []).find(l => l.type === 'address');
    return loc && loc.address ? loc.address : '';
}

/* ---------- Cal.com calls ---------- */

async function call(path, version, key) {
    const r = await fetch(API + path, { headers: { Authorization: 'Bearer ' + key, 'cal-api-version': version } });
    if (!r.ok) throw new Error(`Cal.com ${r.status} for ${path.split('?')[0]}: ${(await r.text()).slice(0, 200)}`);
    return (await r.json()).data;
}
async function allBookings(status, key) {
    const out = []; let cursor = '';
    for (let i = 0; i < 20; i++) {
        const r = await fetch(`${API}/bookings?status=${status}&limit=100${cursor ? '&cursor=' + cursor : ''}`, { headers: { Authorization: 'Bearer ' + key, 'cal-api-version': V.bookings } });
        if (!r.ok) throw new Error(`Cal.com ${r.status} for bookings(${status})`);
        const j = await r.json(); out.push(...j.data);
        if (!j.pagination || !j.pagination.hasMore) break;
        cursor = j.pagination.nextCursor;
    }
    return out;
}

async function main() {
    const key = process.env.CAL_API_KEY, username = process.env.CAL_USERNAME;
    if (!key || !username) throw new Error('Set CAL_API_KEY (secret) and CAL_USERNAME.');
    const now = new Date(), end = new Date(now.getTime() + 548 * 864e5);
    const eventTypes = await call('/event-types?username=' + encodeURIComponent(username), V.eventTypes, key);
    const slotsByType = {};
    for (const t of eventTypes.filter(isRetreat)) {
        slotsByType[t.id] = await call(`/slots?eventTypeId=${t.id}&start=${now.toISOString()}&end=${end.toISOString()}&format=range`, V.slots, key);
    }
    const [upcoming, past] = await Promise.all([allBookings('upcoming', key), allBookings('past', key)]);
    const data = build({ eventTypes, slotsByType, upcoming, past, username, now });
    writeFileSync('jessica-retreats.json', JSON.stringify({ updated: now.toISOString(), ...data }, null, 2) + '\n');
    console.log(`Wrote ${data.retreats.length} upcoming and ${data.archive.length} past retreat dates.`);
}

if (process.argv[1] === fileURLToPath(import.meta.url)) main().catch(e => { console.error(e.message); process.exit(1); });
