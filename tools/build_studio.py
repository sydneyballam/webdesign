"""Builds the studio site's five designs from one set of words (harbor-source.html).
index.html = Design 1 (Harbor). studio-2.html .. studio-5.html = Designs 2 to 5.
Run: python3 tools/build_studio.py"""
import os, re
import content

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
C = content.load()
NAMES = {1: 'Harbor', 2: 'Zine', 3: 'Console', 4: 'Letter', 5: 'Bento'}
FILES = {1: 'index.html', 2: 'studio-2.html', 3: 'studio-3.html', 4: 'studio-4.html', 5: 'studio-5.html'}
DESC = "Websites, online booking, new-equipment setup and simple systems, explained in plain English for Willow Creek small businesses. Book a free first conversation."

def fonts(*fams):
    return '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?' + '&'.join('family=' + f for f in fams) + '&display=swap" rel="stylesheet">'

def picker(n):
    files = ','.join("'%s'" % FILES[i] for i in range(1, 6))
    return '''<div id="designPick" role="group" aria-label="Page design"><span>Design %d of 5 &middot; %s</span><button type="button" id="designNext">Shuffle design</button></div>
<script>
(function(){var F=[%s],me=%d;try{localStorage.setItem('design',me)}catch(e){}
document.getElementById('designNext').addEventListener('click',function(){var d;do{d=1+Math.floor(Math.random()*5)}while(d===me);
try{localStorage.setItem('design',d)}catch(e){}location.href=F[d-1]+(d===1?'?design=1':'')+location.hash})})();
</script>''' % (n, NAMES[n], files, n)

PICK_CSS = '''#designPick{position:fixed;right:12px;bottom:12px;z-index:60;display:flex;align-items:center;gap:8px;max-width:calc(100vw - 24px);padding:6px 8px 6px 14px;border-radius:999px;background:#14181f;color:#fff;box-shadow:0 4px 16px rgba(0,0,0,.3);font:600 14px/1.2 system-ui,sans-serif}
#designPick button{min-height:44px;padding:0 16px;border:0;border-radius:999px;background:#fff;color:#14181f;font:700 14px system-ui,sans-serif;cursor:pointer}
#designPick button:focus-visible{outline:3px solid #fff;outline-offset:2px}
@media print{#designPick{display:none}}
'''

# the work list needs the same markup in every design; classes are styled per design
def work_js():
    js = C['work_js']
    js = js.replace('<p style="font-weight: 700; color: #2B5EA7">', '<p class="client">')
    js = js.replace('class="card"', 'class="wcard"')
    return js

def work_block(cls=''):
    w = C['work']
    return '''<div class="workwrap %s">
<p id="workIntro" class="lede">%s</p>
<p class="lede">%s</p>
<div class="filters">
<div><span class="flabel">Show</span><div id="statusChips" class="chips"></div></div>
<div><span class="flabel">Type of business</span><div id="catChips" class="chips"></div></div>
<div><label for="clientSelect" class="flabel">Client</label><select id="clientSelect"></select></div>
<div class="fcount"><p id="resultCount" aria-live="polite"></p><button id="copyBtn" type="button" class="linkbtn">Copy link to this view</button></div>
</div>
<div id="results"></div>
<div id="emptyState" hidden><p id="emptyText"></p><button id="resetBtn" type="button" class="linkbtn">Show everything</button></div>
</div>''' % (cls, w['intro'], w['also'])

WORK_CSS = '''
.chips{display:flex;flex-wrap:wrap;gap:.5rem}
.chip{min-height:44px;padding:0 1rem;border-radius:var(--r-pill,999px);border:1px solid var(--chip-line,var(--line));background:var(--chip-bg,#fff);color:var(--chip-fg,var(--ink));font:600 1rem var(--f-body);cursor:pointer}
.chip[aria-pressed="true"]{background:var(--chip-on-bg,var(--ink));border-color:var(--chip-on-bg,var(--ink));color:var(--chip-on-fg,var(--paper))}
.chip small{font-size:.8125rem;opacity:.75}
.flabel{display:block;margin:0 0 .5rem;font-size:.875rem;font-weight:700;letter-spacing:.06em;text-transform:uppercase;color:var(--muted)}
#clientSelect{min-height:44px;width:100%;max-width:22rem;border:1px solid var(--chip-line,var(--line));border-radius:var(--r-s,10px);padding:0 .75rem;background:#fff;color:#111;font:600 1rem var(--f-body)}
.linkbtn{min-height:44px;padding:0;border:0;background:none;color:var(--link);font:700 1rem var(--f-body);text-decoration:underline;cursor:pointer}
.filters{display:flex;flex-direction:column;gap:1.25rem;margin:1.5rem 0}
.fcount{display:flex;flex-wrap:wrap;align-items:center;justify-content:space-between;gap:.5rem 1rem}
.fcount p{margin:0;color:var(--muted)}
#results{display:grid;grid-template-columns:repeat(auto-fill,minmax(min(100%,22rem),1fr));gap:1rem}
.wcard{display:flex;flex-direction:column;gap:.75rem;background:var(--wcard-bg,#fff);color:#1b1b1b;border:1px solid var(--wcard-line,var(--line));border-radius:var(--r-m,12px);padding:1.5rem;box-sizing:border-box;min-width:0}
.wcard h3{margin:0;font-family:var(--f-display);font-weight:700;font-size:1.5rem;line-height:1.15;color:#111}
.wcard p{margin:0;color:#333}
.wcard .client{font-weight:700;color:var(--wlink,var(--link))}
.badges{display:flex;flex-wrap:wrap;gap:.5rem}
.badge{font-size:.8125rem;font-weight:700;padding:.2rem .6rem;border-radius:6px}
.badge.published{background:#DCE8F8;color:#183B6B}.badge.prototype{background:#EFE6F9;color:#3F2A5C}.badge.tag{background:#E9EEF8;color:#1E4580}
.looks{display:flex;flex-wrap:wrap;gap:.5rem}
.look{min-height:44px;display:inline-flex;align-items:center;gap:.5rem;padding:0 1rem;border-radius:var(--r-pill,999px);border:2px solid var(--wlink,var(--link));color:var(--wlink,var(--link));font-weight:700;text-decoration:none;box-sizing:border-box;background:#fff}
.look small{font-size:.75rem;text-transform:uppercase;letter-spacing:.04em;opacity:.85}
#emptyState{text-align:center;padding:2.5rem 1rem;border:2px dashed var(--muted);border-radius:var(--r-m,12px)}
#emptyState p{margin:0 0 .5rem;color:var(--muted)}
#cal-embed{background:#fff;border-radius:var(--r-m,12px);padding:.5rem;margin:1.5rem 0 1rem;min-height:12rem;color:#111}
.focus a:focus-visible,a:focus-visible,button:focus-visible,select:focus-visible,summary:focus-visible{outline:3px solid var(--focus,#1a56db);outline-offset:3px}
html{scroll-behavior:smooth}@media (prefers-reduced-motion:reduce){html{scroll-behavior:auto}}
'''

def book_block():
    b = C['book']
    return '''<h2>%s</h2><p>%s</p><p>%s</p>
<div id="cal-embed"></div>
<p>Calendar not showing? <a id="cal-fallback" href="%s" target="_blank" rel="noopener">Open it in a new tab</a>.</p>
<noscript><p><a href="%s">Open the booking calendar</a></p></noscript>''' % (b['h2'], b['p1'], b['p2'], b['fallback'], b['fallback'])

def page(n, fam, css, body, extra_js=''):
    return '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Small Business Studio of Willow Creek</title>
<meta name="description" content="%s">
<link rel="canonical" href="https://sydneyballam.github.io/webdesign/">
%s
<style>
%s
%s
%s
</style>
</head>
<body>
%s
%s
<script>%s</script>
<script>%s</script>
%s
</body>
</html>
''' % (DESC, fonts(*fam), css, WORK_CSS, PICK_CSS, body, '', C['cal_js'], work_js(), picker(n) + extra_js)

def li(items): return ''.join(items)
def plist(paras): return ''.join('<p>%s</p>' % p for p in paras)
def links(ls, cls='btn', first_alt=False):
    out = []
    for i, (h, t) in enumerate(ls):
        out.append('<a class="%s%s" href="%s">%s</a>' % (cls, ' alt' if i else '', h, t))
    return ''.join(out)

# =====================================================================
# DESIGN 2: Zine  (cream paper, huge serif type, ruled rows, numbered chapters)
# =====================================================================
def zine():
    css = '''
:root{--ink:#141414;--paper:#F4EEDF;--line:#141414;--muted:#4a4538;--link:#A32D14;--accent:#A32D14;--f-display:'Fraunces',Georgia,serif;--f-body:'Source Sans 3',system-ui,sans-serif;--r-pill:0;--r-s:0;--r-m:0;--chip-line:#141414;--chip-bg:#F4EEDF;--wcard-bg:#FBF8F0;--wcard-line:#141414;--focus:#A32D14}
*{box-sizing:border-box}body{margin:0;background:var(--paper);color:var(--ink);font:1.1875rem/1.6 var(--f-body)}
.wrap{max-width:74rem;margin:0 auto;padding:0 1.5rem}
.mast{border-bottom:4px double var(--ink)}
.mast .wrap{display:flex;flex-wrap:wrap;justify-content:space-between;align-items:baseline;gap:.25rem 2rem;padding-top:1rem;padding-bottom:.75rem}
.mast a.brand{font-family:var(--f-display);font-weight:800;font-style:italic;font-size:1.5rem;color:var(--ink);text-decoration:none}
.mast .place{font-size:.9375rem;letter-spacing:.14em;text-transform:uppercase;font-weight:700}
.tabs{border-bottom:1px solid var(--ink)}
.tabs .wrap{display:flex;flex-wrap:wrap;gap:0 1.5rem}
.tabs a{min-height:44px;display:inline-flex;align-items:center;color:var(--ink);font-weight:700;font-size:.9375rem;letter-spacing:.08em;text-transform:uppercase;text-decoration:none;border-bottom:3px solid transparent}
.tabs a:hover{border-bottom-color:var(--accent)}
.hero{padding:3rem 0 2.5rem;border-bottom:1px solid var(--ink)}
.hero h1{margin:0 0 2rem;font-family:var(--f-display);font-weight:800;font-size:clamp(2.75rem,9.5vw,7.5rem);line-height:.95;letter-spacing:-.03em}
.hero .cols{display:grid;grid-template-columns:3fr 2fr;gap:3rem}
.hero .lead{font-size:1.375rem;margin:0 0 1.5rem}
.hero .lead::first-letter{font-family:var(--f-display);font-weight:800;font-size:4.2rem;float:left;line-height:.8;padding:.3rem .5rem 0 0;color:var(--accent)}
.hero aside{border:2px solid var(--ink);padding:1.5rem;background:#FBF8F0}
.hero aside p{margin:0 0 .75rem}.hero aside p:first-child{font-family:var(--f-display);font-weight:700;font-size:1.5rem;line-height:1.2}
.btn{display:inline-flex;align-items:center;min-height:52px;padding:0 1.5rem;background:var(--ink);color:var(--paper);font-weight:700;text-decoration:none;border:2px solid var(--ink);margin:0 .75rem .75rem 0}
.btn.alt{background:transparent;color:var(--ink)}
.btn:hover{background:var(--accent);border-color:var(--accent);color:#fff}
.band{background:var(--ink);color:var(--paper);padding:.75rem 0;font-weight:700;letter-spacing:.04em}
.band a{color:#F2C14E;margin-left:1rem}
section.chap{padding:4rem 0;border-bottom:1px solid var(--ink)}
.chap-head{display:grid;grid-template-columns:7rem 1fr;gap:1rem 2rem;margin-bottom:2.5rem}
.chap-no{font-family:var(--f-display);font-weight:800;font-size:5.5rem;line-height:.8;color:transparent;-webkit-text-stroke:2px var(--ink)}
.kick{margin:0 0 .5rem;font-weight:700;letter-spacing:.14em;text-transform:uppercase;font-size:.875rem;color:var(--accent)}
.chap h2{margin:0 0 1rem;font-family:var(--f-display);font-weight:800;font-size:clamp(2rem,4.6vw,3.5rem);line-height:1.02;letter-spacing:-.02em;max-width:50rem}
.chap .intro{max-width:46rem;margin:0 0 .75rem}
.rows .row{display:grid;grid-template-columns:1fr 2fr;gap:.5rem 2.5rem;padding:1.25rem 0;border-top:1px solid var(--ink)}
.rows .row:first-child{border-top:3px solid var(--ink)}
.rows h3{margin:0;font-family:var(--f-display);font-weight:700;font-size:1.5rem;line-height:1.15}
.rows p{margin:0 0 .5rem}.rows p:last-child{margin:0}
.steps{display:grid;grid-template-columns:repeat(3,1fr);border-top:3px solid var(--ink)}
.steps .step{padding:1.5rem 1.5rem 1.5rem 0;border-right:1px solid var(--ink);margin-right:1.5rem}.steps .step:last-child{border:0}
.steps .no{font-family:var(--f-display);font-weight:800;font-size:5rem;line-height:1;color:var(--accent)}
.steps h3{margin:.25rem 0 .5rem;font-family:var(--f-display);font-size:1.5rem}.steps p{margin:0}
.cols3{display:grid;grid-template-columns:repeat(3,1fr);border-top:3px solid var(--ink)}
.cols3>div{padding:1.5rem 1.5rem 1rem 0;margin-right:1.5rem;border-right:1px solid var(--ink)}.cols3>div:last-child{border:0}
.cols3 h3{margin:0 0 .75rem;font-family:var(--f-display);font-size:1.5rem}.cols3 p{margin:0 0 .6rem}
.cta{margin-top:2rem}
.note{max-width:46rem;margin:2rem 0 0;font-style:italic;color:var(--muted)}
.own{background:var(--ink);color:var(--paper);padding:4rem 0}
.own .grid{display:grid;grid-template-columns:1fr 1fr;gap:3rem}
.own h2{margin:0 0 .75rem;font-family:var(--f-display);font-weight:800;font-size:clamp(2rem,4.6vw,3.5rem);line-height:1.02}
.own p{margin:0 0 .9rem}.own strong{color:#F2C14E}
.book{background:var(--ink);color:var(--paper);padding:4rem 0}
.book h2{margin:0 0 1rem;font-family:var(--f-display);font-weight:800;font-size:clamp(2.25rem,6vw,4.5rem);line-height:1}
.book a{color:#F2C14E}
footer{padding:2rem 0 5rem;font-size:.9375rem}footer .wrap{display:flex;flex-wrap:wrap;justify-content:space-between;gap:.5rem 2rem}
.workwrap .lede{max-width:46rem;margin:0 0 .75rem}
@media (max-width:760px){.hero .cols,.own .grid{grid-template-columns:1fr}.rows .row{grid-template-columns:1fr}.steps,.cols3{grid-template-columns:1fr}.steps .step,.cols3>div{border:0;margin:0;border-bottom:1px solid var(--ink);padding-right:0}.chap-head{grid-template-columns:1fr}.chap-no{font-size:3.5rem}}
'''
    h = C['hero']
    def head(d, i):
        return '<div class="chap-head"><div class="chap-no" aria-hidden="true">%02d</div><div><p class="kick">%s</p><h2>%s</h2>%s</div></div>' % (i, d['kicker'], d['title'], ''.join('<p class="intro">%s</p>' % p for p in d['intro']))
    def rows(d):
        return '<div class="rows">' + ''.join('<div class="row"><h3>%s</h3><div>%s</div></div>' % (c['h3'], plist(c['paras'])) for c in d['cards']) + '</div>'
    def cta(d):
        return '<div class="cta">%s</div>' % links(d['links']) if d['links'] else ''
    def note(d): return '<p class="note">%s</p>' % d['note'] if d['note'] else ''
    secs = []
    i = 0
    for key in ['modernize', 'events', 'problems', 'services']:
        i += 1; d = C[key]
        secs.append('<section class="chap" id="%s"><div class="wrap">%s%s%s%s</div></section>' % (d['id'], head(d, i), rows(d), cta(d), note(d)))
    d = C['how']; i += 1
    secs.append('<section class="chap" id="how"><div class="wrap">%s<div class="steps">%s</div></div></section>' % (head(d, i), ''.join('<div class="step"><div class="no">%s</div><h3>%s</h3>%s</div>' % (c['num'], c['h3'], plist(c['paras'])) for c in d['cards'])))
    d = C['free']; i += 1
    secs.append('<section class="chap" id="free"><div class="wrap">%s<div class="cols3">%s</div>%s</div></section>' % (head(d, i), ''.join('<div><h3>%s</h3>%s</div>' % (c['h3'], plist(c['paras'])) for c in d['cards']), cta(d)))
    d = C['start']; i += 1
    secs.append('<section class="chap" id="start"><div class="wrap">%s%s%s</div></section>' % (head(d, i), rows(d), note(d)))
    o = C['own']
    secs.append('<section class="own"><div class="wrap grid"><div><h2>%s</h2><p>%s</p></div><div>%s</div></div></section>' % (o['h2'], o['lead'], plist(o['items'])))
    w = C['work']; i += 1
    secs.append('<section class="chap" id="work"><div class="wrap"><div class="chap-head"><div class="chap-no" aria-hidden="true">%02d</div><div><p class="kick">%s</p><h2>%s</h2></div></div>%s</div></section>' % (i, w['kicker'], w['title'], work_block()))
    d = C['learn']; i += 1
    secs.append('<section class="chap" id="learn"><div class="wrap">%s<div class="cols3">%s</div></div></section>' % (head(d, i), ''.join('<div><h3>%s</h3>%s</div>' % (c['h3'], plist(c['paras'])) for c in d['cards'])))
    secs.append('<section class="book" id="book"><div class="wrap">%s</div></section>' % book_block())
    body = '''<header class="mast"><div class="wrap"><a class="brand" href="#top">%s</a><span class="place">Willow Creek, California</span></div></header>
<nav class="tabs" aria-label="Main"><div class="wrap">%s</div></nav>
<main id="top"><section class="hero"><div class="wrap"><h1>%s</h1><div class="cols"><div><p class="lead">%s</p><div>%s</div></div><aside>%s</aside></div></div></section>
<div class="band"><div class="wrap">%s<a href="%s">%s</a></div></div>
%s</main>
<footer><div class="wrap"><span>%s</span><span>%s</span></div></footer>''' % (
        C['brand'], ''.join('<a href="%s">%s</a>' % x for x in C['nav']), h['h1'], h['lead'], links(h['links']), plist(h['card']),
        C['band']['text'], C['band']['href'], C['band']['link'], '\n'.join(secs), C['footer'][0], C['footer'][1])
    return page(2, ['Fraunces:ital,opsz,wght@0,9..144,600;0,9..144,800;1,9..144,800', 'Source+Sans+3:wght@400;600;700'], css, body)

if __name__ == '__main__':
    import sys
    from designs_rest import console, letter, bento, harbor
    outs = {1: harbor(C, picker, PICK_CSS), 2: zine(), 3: console(), 4: letter(), 5: bento()}
    for n, html in outs.items():
        open(os.path.join(ROOT, FILES[n]), 'w', encoding='utf-8').write(html)
        print(FILES[n], len(html))
