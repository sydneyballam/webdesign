// Builds jessica-retreats.json from Jessica's Cal.com "Events" (cal.com/events).
// Runs on a schedule in GitHub Actions (see .github/workflows/retreats.yml).
// Every published, visible, non-cancelled Event is a retreat. Seats left = capacity - confirmed guests.
// Needs one setting: CAL_API_KEY (secret).

import { writeFileSync, mkdirSync, existsSync, readdirSync, readFileSync, statSync, unlinkSync } from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const API = 'https://api.cal.com/v2';
const VERSION = '2026-05-01';
const DEFAULT_CAPACITY = 10;   // used only if an event has no capacity set in Cal.com
const PHOTO_ROOT = 'retreat-photos';   // one folder per retreat inside this folder; Jessica drops photos in
const FULL_PX = 1600, THUMB_PX = 480;
const IMAGE_EXT = /\.(jpe?g|png|webp)$/i;

/* ---------- pure logic (tested separately) ---------- */

export function isShown(e) {
    return e.publishedAt && !e.cancelledAt && !e.hidden && (!e.visibility || e.visibility === 'PUBLIC');
}
export function placeOf(e) {
    const loc = (e.locations || []).find(l => l.type === 'address');
    return loc && loc.address ? loc.address : '';
}
// Folder name for a retreat: its start date (Pacific time) plus its Cal.com address name, e.g. 2026-11-04-jessica-s-faux-retreat
export function keyOf(e) {
    const day = new Intl.DateTimeFormat('en-CA', { timeZone: 'America/Los_Angeles', year: 'numeric', month: '2-digit', day: '2-digit' }).format(new Date(e.startTime));
    const name = String(e.slug || e.title || 'retreat').toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-+|-+$/g, '');
    return day + '-' + name;
}
export function build({ upcoming, past, now = new Date(), photosFor = () => [] }) {
    const retreats = upcoming.filter(isShown).filter(e => new Date(e.endTime) > now).map(e => {
        const capacity = Number(e.capacity) > 0 ? Number(e.capacity) : DEFAULT_CAPACITY;
        const taken = Number(e.confirmedCount || 0);
        const left = Math.max(0, capacity - taken);
        return {
            title: e.title, description: e.description || '', slug: e.slug, url: 'https://cal.com/' + e.slug,
            place: placeOf(e), start: new Date(e.startTime).toISOString(), end: new Date(e.endTime).toISOString(),
            capacity, left, soldOut: left === 0, photos: photosFor(keyOf(e))
        };
    }).sort((a, b) => a.start.localeCompare(b.start));
    const archive = past.filter(isShown).map(e => ({ title: e.title, start: new Date(e.startTime).toISOString(), end: new Date(e.endTime).toISOString(), photos: photosFor(keyOf(e)) }))
        .sort((a, b) => b.start.localeCompare(a.start));
    return { retreats, archive };
}

/* ---------- photo folders ---------- */

const FOLDER_README = (title) => `# Photos: ${title}

Drop this retreat's photos into this folder and they appear on the website under "Past retreats" within a few minutes.

1. Click **Add file**, then **Upload files**.
2. Drag in your photos (or choose them from your phone or computer).
3. Click **Commit changes**.

Big photos are fine. They are shrunk automatically, and location details are removed. JPG and PNG work. Delete a photo here to remove it from the site.
`;

// Makes a folder (with a how-to note) for every retreat that is on Cal.com. Returns the folder names.
export function ensureFolders(events, root = PHOTO_ROOT) {
    const keys = [];
    for (const e of events) {
        const key = keyOf(e), dir = path.join(root, key);
        keys.push(key);
        mkdirSync(dir, { recursive: true });
        const readme = path.join(dir, 'README.md');
        if (!existsSync(readme)) writeFileSync(readme, FOLDER_README(e.title));
    }
    return keys;
}

// Shrinks anything big, removes location/camera details, writes small thumbnails. Safe to run again and again.
export async function processPhotos(root = PHOTO_ROOT) {
    let sharp; try { sharp = (await import('sharp')).default; } catch { console.log('sharp is not installed: skipping photo processing'); return; }
    if (!existsSync(root)) return;
    for (const key of readdirSync(root, { withFileTypes: true }).filter(d => d.isDirectory()).map(d => d.name)) {
        const dir = path.join(root, key), thumbs = path.join(dir, 'thumbs');
        for (const f of readdirSync(dir).filter(n => IMAGE_EXT.test(n))) {
            try {
                const src = path.join(dir, f), base = f.replace(/\.[^.]+$/, '');
                const out = path.join(dir, base + '.jpg'), thumb = path.join(thumbs, base + '.jpg');
                const meta = await sharp(src).metadata();
                const isJpg = /\.jpe?g$/i.test(f);
                const needsFull = !isJpg || f !== base + '.jpg' || Boolean(meta.exif) || Math.max(meta.width, meta.height) > FULL_PX || (meta.orientation || 1) !== 1;
                if (needsFull) {
                    const buf = await sharp(src).rotate().resize(FULL_PX, FULL_PX, { fit: 'inside', withoutEnlargement: true }).jpeg({ quality: 80, mozjpeg: true }).toBuffer();
                    if (src !== out) unlinkSync(src);
                    writeFileSync(out, buf);
                    console.log(`OK   ${key}/${f} -> ${base}.jpg (${Math.round(buf.length / 1024)} KB)`);
                }
                if (!existsSync(thumb)) {
                    mkdirSync(thumbs, { recursive: true });
                    await sharp(out).resize(THUMB_PX, THUMB_PX, { fit: 'inside', withoutEnlargement: true }).jpeg({ quality: 75 }).toFile(thumb);
                }
            } catch (err) { console.log(`FAIL ${key}/${f}: ${err.message}`); }
        }
        if (existsSync(thumbs)) for (const t of readdirSync(thumbs)) if (!existsSync(path.join(dir, t))) unlinkSync(path.join(thumbs, t));  // photo was deleted
    }
}

export function listPhotos(key, root = PHOTO_ROOT) {
    const dir = path.join(root, key);
    if (!existsSync(dir)) return [];
    return readdirSync(dir).filter(n => /\.jpg$/i.test(n)).sort()
        .map(n => ({ src: `${root}/${key}/${n}`, thumb: existsSync(path.join(dir, 'thumbs', n)) ? `${root}/${key}/thumbs/${n}` : `${root}/${key}/${n}` }));
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
    const shown = upcoming.concat(past).filter(isShown);
    ensureFolders(shown);
    await processPhotos();
    const data = build({ upcoming, past, now, photosFor: listPhotos });
    writeFileSync('jessica-retreats.json', JSON.stringify({ updated: now.toISOString(), ...data }, null, 2) + '\n');
    console.log(`Wrote ${data.retreats.length} upcoming and ${data.archive.length} past retreats.`);
}

if (process.argv[1] === fileURLToPath(import.meta.url)) main().catch(e => { console.error(e.message); process.exit(1); });
