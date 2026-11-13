import os
from build_studio import *   # helpers: C, page, picker, links, plist, work_block, book_block, ...
import build_studio as B

REDIRECT = '''<script>
/* Pick one of the five designs at random on each visit (never the same twice in a row). ?design=1 stays on this page. */
(function(){var q=/[?&]design=([1-5])/.exec(location.search),d=q?+q[1]:0,last=0,F=['index.html','studio-2.html','studio-3.html','studio-4.html','studio-5.html'];
try{last=+localStorage.getItem('design')||0}catch(e){}
if(!d){do{d=1+Math.floor(Math.random()*5)}while(d===last)}
try{localStorage.setItem('design',d)}catch(e){}
if(d>1){var s=location.search.replace(/[?&]design=\\d/,'');location.replace(F[d-1]+s+location.hash)}
})();
</script>
'''

def harbor(C, picker, PICK_CSS):
    s = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'harbor-source.html'), encoding='utf-8').read()
    s = s.replace('<head>\n', '<head>\n' + REDIRECT + '<link rel="canonical" href="https://sydneyballam.github.io/webdesign/">\n', 1)
    s = s.replace('</style>', PICK_CSS + '</style>', 1)
    s = s.replace('</body>', picker(1) + '\n</body>', 1)
    return s

# =====================================================================
# DESIGN 3: Console (fixed sidebar, dense panels, mono labels)
# =====================================================================
def console():
    css = '''
:root{--ink:#10222a;--paper:#EEF3F3;--line:#CBD8D8;--muted:#40585e;--link:#0B6472;--accent:#0B6472;--f-display:'Space Grotesk',system-ui,sans-serif;--f-body:'IBM Plex Sans',system-ui,sans-serif;--f-mono:'IBM Plex Mono',ui-monospace,monospace;--r-pill:6px;--r-s:6px;--r-m:8px;--chip-on-bg:#0B6472;--chip-on-fg:#fff;--wcard-line:#CBD8D8;--focus:#0B6472}
*{box-sizing:border-box}body{margin:0;background:var(--paper);color:var(--ink);font:1.0625rem/1.55 var(--f-body)}
.shell{display:grid;grid-template-columns:17rem 1fr;min-height:100vh}
.side{position:sticky;top:0;height:100vh;overflow:auto;background:#0E2A33;color:#E4F0F1;padding:1.5rem 1.25rem;display:flex;flex-direction:column;gap:1.5rem}
.side .brand{font-family:var(--f-display);font-weight:700;font-size:1.25rem;line-height:1.2;color:#fff;text-decoration:none}
.side .sub{font:500 .8125rem var(--f-mono);color:#9FC3C8;letter-spacing:.04em;text-transform:uppercase;margin-top:.35rem;display:block}
.side nav{display:flex;flex-direction:column;gap:2px}
.side nav a{min-height:44px;display:flex;align-items:center;gap:.6rem;padding:0 .75rem;border-radius:6px;color:#D5E6E8;text-decoration:none;font-weight:500;border-left:3px solid transparent}
.side nav a:hover{background:#16404c}
.side nav a.on{background:#16404c;border-left-color:#7FE0D0;color:#fff}
.side .cta{margin-top:auto;display:flex;min-height:48px;align-items:center;justify-content:center;border-radius:6px;background:#7FE0D0;color:#06242a;font-weight:700;text-decoration:none}
main{min-width:0}
.sec{padding:3.25rem 3rem;border-bottom:1px solid var(--line);max-width:80rem}
.tag{font:500 .8125rem var(--f-mono);letter-spacing:.06em;text-transform:uppercase;color:var(--accent);margin:0 0 .6rem}
.sec h2{margin:0 0 .75rem;font-family:var(--f-display);font-weight:700;font-size:clamp(1.6rem,3vw,2.25rem);line-height:1.12;letter-spacing:-.01em;max-width:46rem}
.sec>p.intro{max-width:44rem;margin:0 0 1rem}
.hero{padding:3.5rem 3rem;background:linear-gradient(180deg,#fff,#EEF3F3);border-bottom:1px solid var(--line)}
.hero .g{display:grid;grid-template-columns:1.5fr 1fr;gap:2.5rem;align-items:start;max-width:80rem}
.hero h1{margin:0 0 1rem;font-family:var(--f-display);font-weight:700;font-size:clamp(2rem,4.2vw,3.25rem);line-height:1.05;letter-spacing:-.02em}
.hero .lead{font-size:1.2rem;max-width:40rem;margin:0 0 1.5rem}
.panel{background:#fff;border:1px solid var(--line);border-radius:8px;padding:1.25rem}
.hero .panel{border-left:4px solid var(--accent)}
.hero .panel p{margin:0 0 .6rem}.hero .panel p:first-child{font-family:var(--f-display);font-weight:700;font-size:1.25rem;line-height:1.2}
.btn{display:inline-flex;align-items:center;min-height:48px;padding:0 1.25rem;border-radius:6px;background:var(--accent);color:#fff;font-weight:700;text-decoration:none;margin:0 .6rem .6rem 0;border:2px solid var(--accent)}
.btn.alt{background:#fff;color:var(--accent)}
.status{display:flex;flex-wrap:wrap;align-items:center;gap:.5rem 1rem;padding:.75rem 3rem;background:#DDF3EE;border-bottom:1px solid #b9dcd4;font-weight:600;color:#0a3d37}
.status::before{content:"";width:10px;height:10px;border-radius:50%;background:#12906f}
.status a{color:#0a3d37;font-weight:700}
.cards{display:grid;grid-template-columns:repeat(auto-fill,minmax(min(100%,17rem),1fr));gap:1rem;margin-top:1.5rem}
.cards .panel h3{margin:0 0 .5rem;font-family:var(--f-display);font-weight:700;font-size:1.15rem;line-height:1.2}
.cards .panel p{margin:0 0 .5rem;color:#2a3d42}.cards .panel p:last-child{margin:0}
.cards .panel .i{display:inline-flex;align-items:center;justify-content:center;min-width:2rem;height:2rem;padding:0 .4rem;border-radius:6px;background:#DDF0F2;color:#0B5260;font:600 .875rem var(--f-mono);margin-bottom:.6rem}
.cards.two{grid-template-columns:repeat(auto-fill,minmax(min(100%,24rem),1fr))}
.flow{display:grid;grid-template-columns:repeat(3,1fr);gap:1.25rem;margin-top:1.5rem;counter-reset:s}
.flow .panel{position:relative}
.flow .panel .n{display:inline-flex;width:2.5rem;height:2.5rem;border-radius:50%;background:var(--accent);color:#fff;align-items:center;justify-content:center;font-weight:700;margin-bottom:.6rem}
.flow .panel:not(:last-child)::after{content:"";position:absolute;top:2.2rem;right:-1.25rem;width:1.25rem;border-top:2px dashed var(--accent)}
.flow h3{margin:0 0 .4rem;font-family:var(--f-display);font-size:1.2rem}.flow p{margin:0}
.cta-row{margin-top:1.5rem}.note{max-width:44rem;margin:1.5rem 0 0;color:var(--muted)}
.own .panel{background:#0E2A33;color:#E4F0F1;border:0}.own h2{color:#fff}.own p{margin:0 0 .6rem}.own strong{color:#7FE0D0}
.own .panel .g{display:grid;grid-template-columns:1fr 1.4fr;gap:2rem}
.book{background:#fff}
.workwrap .lede{max-width:44rem;margin:0 0 .6rem}
foot{display:block}
.foot{padding:1.5rem 3rem 5rem;color:var(--muted);font-size:.9375rem;display:flex;flex-wrap:wrap;gap:.5rem 2rem;justify-content:space-between}
@media (max-width:900px){.shell{display:block}.side{position:sticky;height:auto;flex-direction:row;align-items:center;gap:.75rem;padding:.5rem .75rem;z-index:40;overflow:visible}.side .brand{font-size:1rem;flex:0 0 auto;max-width:8rem}.side .sub{display:none}.side nav{flex-direction:row;overflow-x:auto;flex:1}.side nav a{white-space:nowrap;border-left:0;border-bottom:3px solid transparent;border-radius:0}.side nav a.on{border-bottom-color:#7FE0D0}.side .cta{display:none}.sec,.hero,.status,.foot{padding-left:1.25rem;padding-right:1.25rem}.hero .g,.own .panel .g{grid-template-columns:1fr}.flow{grid-template-columns:1fr}.flow .panel::after{display:none}}
'''
    h = C['hero']
    def sec(d, inner, extra='', cls=''):
        return '<section class="sec %s" id="%s"><p class="tag">%s</p><h2>%s</h2>%s%s%s%s</section>' % (cls, d['id'], d['kicker'], d['title'], ''.join('<p class="intro">%s</p>' % p for p in d['intro']), inner, ('<div class="cta-row">%s</div>' % links(d['links'])) if d['links'] else '', ('<p class="note">%s</p>' % d['note']) if d['note'] else '')
    def cards(d, two=False, idx=True):
        return '<div class="cards%s">' % (' two' if two else '') + ''.join('<div class="panel">%s<h3>%s</h3>%s</div>' % ('<span class="i">%02d</span>' % (k + 1) if idx else '', c['h3'], plist(c['paras'])) for k, c in enumerate(d['cards'])) + '</div>'
    parts = []
    parts.append(sec(C['modernize'], cards(C['modernize'], True)))
    parts.append(sec(C['events'], cards(C['events'], True)))
    parts.append(sec(C['problems'], cards(C['problems'])))
    parts.append(sec(C['services'], cards(C['services'])))
    d = C['how']
    parts.append(sec(d, '<div class="flow">' + ''.join('<div class="panel"><span class="n">%s</span><h3>%s</h3>%s</div>' % (c['num'], c['h3'], plist(c['paras'])) for c in d['cards']) + '</div>'))
    parts.append(sec(C['free'], cards(C['free'], True, idx=False)))
    parts.append(sec(C['start'], cards(C['start'], idx=False)))
    o = C['own']
    parts.append('<section class="sec own"><div class="panel"><div class="g"><div><h2>%s</h2><p>%s</p></div><div>%s</div></div></div></section>' % (o['h2'], o['lead'], plist(o['items'])))
    w = C['work']
    parts.append('<section class="sec" id="work"><p class="tag">%s</p><h2>%s</h2>%s</section>' % (w['kicker'], w['title'], work_block()))
    parts.append(sec(C['learn'], cards(C['learn'], idx=False)))
    parts.append('<section class="sec book" id="book">%s</section>' % book_block())
    nav = ''.join('<a href="%s">%s</a>' % x for x in C['nav'])
    body = '''<div class="shell"><aside class="side"><div><a class="brand" href="#top">%s</a><span class="sub">Willow Creek, CA</span></div><nav aria-label="Main" id="sidenav">%s</nav><a class="cta" href="#book">Book a free chat</a></aside>
<main id="top"><section class="hero"><div class="g"><div><p class="tag">%s</p><h1>%s</h1><p class="lead">%s</p><div>%s</div></div><div class="panel">%s</div></div></section>
<div class="status"><span>%s</span><a href="%s">%s</a></div>
%s
<div class="foot"><span>%s</span><span>%s</span></div></main></div>''' % (C['brand'], nav, h['kicker'], h['h1'], h['lead'], links(h['links']), plist(h['card']), C['band']['text'], C['band']['href'], C['band']['link'], '\n'.join(parts), C['footer'][0], C['footer'][1])
    js = '''<script>
(function(){var links=[].slice.call(document.querySelectorAll('#sidenav a[href^="#"]')),map={};links.forEach(function(a){var s=document.querySelector(a.getAttribute('href'));if(s)map[a.getAttribute('href')]=s});
if(!('IntersectionObserver' in window))return;
var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){links.forEach(function(a){a.classList.toggle('on',map[a.getAttribute('href')]===e.target)})}})},{rootMargin:'-30% 0px -60% 0px'});
Object.keys(map).forEach(function(k){io.observe(map[k])})})();
</script>'''
    return page(3, ['Space+Grotesk:wght@500;700', 'IBM+Plex+Sans:wght@400;500;600;700', 'IBM+Plex+Mono:wght@500'], css, body, js)

# =====================================================================
# DESIGN 4: Letter (one narrow column, warm, accordions, timeline)
# =====================================================================
def letter():
    css = '''
:root{--ink:#2B1B3D;--paper:#FFF6EC;--line:#EBCFB5;--muted:#5a4868;--link:#B4410A;--accent:#B4410A;--f-display:'Fraunces',Georgia,serif;--f-body:'Nunito',system-ui,sans-serif;--r-pill:999px;--r-s:12px;--r-m:20px;--chip-line:#D8B696;--chip-bg:#fff;--wcard-bg:#fff;--wcard-line:#EBCFB5;--focus:#B4410A}
*{box-sizing:border-box}body{margin:0;background:var(--paper);color:var(--ink);font:1.1875rem/1.65 var(--f-body)}
.col{max-width:44rem;margin:0 auto;padding:0 1.25rem}
.top{padding:1rem 0}.top .col{display:flex;align-items:center;justify-content:space-between;gap:1rem}
.top a.brand{font-family:var(--f-display);font-weight:700;font-size:1.2rem;color:var(--ink);text-decoration:none;line-height:1.2}
.pill{display:inline-flex;align-items:center;justify-content:center;text-align:center;min-height:44px;padding:.4rem 1.25rem;border-radius:999px;background:var(--accent);color:#fff;font-weight:800;text-decoration:none}
.pill.alt{background:#fff;color:var(--accent);border:2px solid var(--accent)}
details.menu{position:relative}details.menu summary{list-style:none;min-height:44px;display:inline-flex;align-items:center;padding:0 1rem;border-radius:999px;border:2px solid var(--ink);font-weight:800;cursor:pointer}
details.menu summary::-webkit-details-marker{display:none}
details.menu nav{position:absolute;right:0;top:calc(100% + 8px);width:15rem;background:#fff;border:1px solid var(--line);border-radius:16px;box-shadow:0 12px 30px rgba(43,27,61,.18);padding:.5rem;z-index:30}
details.menu nav a{display:flex;min-height:44px;align-items:center;padding:0 .75rem;color:var(--ink);text-decoration:none;font-weight:700;border-radius:10px}details.menu nav a:hover{background:#FFEAD6}
.hello{padding:2rem 0 2.5rem;text-align:center}
.hello .sun{width:5.5rem;height:5.5rem;border-radius:50%;margin:0 auto 1.25rem;background:radial-gradient(circle at 35% 35%,#FFD27A,#F59E42);box-shadow:0 0 0 10px #FFE7C4,0 0 0 22px #FFF0DA}
.hello .kick{margin:0 0 .5rem;font-weight:800;letter-spacing:.1em;text-transform:uppercase;font-size:.875rem;color:var(--accent)}
.hello h1{margin:0 0 1rem;font-family:var(--f-display);font-weight:800;font-size:clamp(2.25rem,7vw,3.6rem);line-height:1.05;letter-spacing:-.02em}
.hello .lead{margin:0 0 1.5rem;font-size:1.25rem}
.bubble{position:relative;margin:2.5rem 0 0;background:#fff;border:2px solid var(--ink);border-radius:24px;padding:1.5rem;text-align:left}
.bubble::before{content:"";position:absolute;top:-14px;left:2.5rem;width:24px;height:24px;background:#fff;border-left:2px solid var(--ink);border-top:2px solid var(--ink);transform:rotate(45deg)}
.bubble p{margin:0 0 .6rem}.bubble p:first-child{font-family:var(--f-display);font-weight:700;font-size:1.4rem;line-height:1.2}.bubble p:last-child{margin:0}
.offer{background:#FFE2B8;border-radius:20px;padding:1rem 1.25rem;margin:1.5rem 0 0;text-align:center;font-weight:800}
.offer a{color:var(--ink);margin-left:.5rem}
.chap{padding:3rem 0;border-top:2px dotted var(--line)}
.chap .kick{margin:0 0 .4rem;font-weight:800;letter-spacing:.1em;text-transform:uppercase;font-size:.875rem;color:var(--accent)}
.chap h2{margin:0 0 .75rem;font-family:var(--f-display);font-weight:800;font-size:clamp(1.75rem,5vw,2.4rem);line-height:1.1;letter-spacing:-.01em}
.chap .intro{margin:0 0 1rem}
.acc{margin-top:1.25rem;display:flex;flex-direction:column;gap:.75rem}
.acc details{background:#fff;border:1px solid var(--line);border-radius:18px;overflow:hidden}
.acc summary{list-style:none;display:flex;align-items:center;justify-content:space-between;gap:1rem;min-height:56px;padding:.75rem 1.25rem;cursor:pointer;font-family:var(--f-display);font-weight:700;font-size:1.2rem;line-height:1.25}
.acc summary::-webkit-details-marker{display:none}
.acc summary::after{content:"+";flex:0 0 auto;display:inline-flex;align-items:center;justify-content:center;width:2rem;height:2rem;border-radius:50%;background:#FFE2B8;font-family:var(--f-body);font-weight:800}
.acc details[open] summary::after{content:"\\2212"}
.acc .in{padding:0 1.25rem 1.1rem}.acc .in p{margin:0 0 .6rem}.acc .in p:last-child{margin:0}
.timeline{margin:1.5rem 0 0;padding:0;list-style:none;position:relative}
.timeline::before{content:"";position:absolute;left:1.25rem;top:.5rem;bottom:.5rem;width:3px;background:var(--line)}
.timeline li{position:relative;padding:0 0 1.75rem 4rem}
.timeline .n{position:absolute;left:0;top:0;width:2.6rem;height:2.6rem;border-radius:50%;background:var(--accent);color:#fff;display:flex;align-items:center;justify-content:center;font-weight:800}
.timeline h3{margin:0 0 .25rem;font-family:var(--f-display);font-size:1.35rem}.timeline p{margin:0}
.group{background:#fff;border:1px solid var(--line);border-radius:20px;padding:1.25rem 1.5rem;margin:1rem 0}
.group h3{margin:0 0 .5rem;font-family:var(--f-display);font-size:1.3rem}.group p{margin:0 0 .5rem}
.cta-row{margin-top:1.5rem;display:flex;flex-wrap:wrap;gap:.75rem}.note{margin:1.5rem 0 0;color:var(--muted);font-style:italic}
.own{background:#2B1B3D;color:#FFF6EC;border-radius:28px;padding:2rem 1.5rem;margin:2rem 0}
.own h2{margin:0 0 .5rem;font-family:var(--f-display);font-weight:800;font-size:2rem;line-height:1.1}.own p{margin:0 0 .75rem}.own strong{color:#FFD27A}
.book{padding:3rem 0 6rem;border-top:2px dotted var(--line)}.book h2{margin:0 0 .75rem;font-family:var(--f-display);font-weight:800;font-size:clamp(2rem,6vw,2.8rem);line-height:1.05}
.book a{color:var(--accent);font-weight:700}
footer{padding:0 0 6rem;text-align:center;color:var(--muted);font-size:.9375rem}footer span{display:block}
.workwrap .lede{margin:0 0 .75rem}
.sticky{position:fixed;right:12px;bottom:12px;z-index:55}
@media (max-width:600px){.top .pill{display:none}}
'''
    h = C['hero']
    def acc(d, first_open=True):
        return '<div class="acc">' + ''.join('<details%s><summary>%s</summary><div class="in">%s</div></details>' % (' open' if (k == 0 and first_open) else '', c['h3'], plist(c['paras'])) for k, c in enumerate(d['cards'])) + '</div>'
    def chap(d, inner):
        return '<section class="chap" id="%s"><div class="col"><p class="kick">%s</p><h2>%s</h2>%s%s%s%s</div></section>' % (d['id'], d['kicker'], d['title'], ''.join('<p class="intro">%s</p>' % p for p in d['intro']), inner, ('<div class="cta-row">%s</div>' % ''.join('<a class="pill%s" href="%s">%s</a>' % (' alt' if i else '', h_, t) for i, (h_, t) in enumerate(d['links']))) if d['links'] else '', ('<p class="note">%s</p>' % d['note']) if d['note'] else '')
    parts = []
    parts.append(chap(C['modernize'], acc(C['modernize'])))
    parts.append(chap(C['events'], acc(C['events'])))
    parts.append(chap(C['problems'], acc(C['problems'], False)))
    parts.append(chap(C['services'], acc(C['services'], False)))
    d = C['how']
    parts.append(chap(d, '<ol class="timeline">' + ''.join('<li><span class="n">%s</span><h3>%s</h3>%s</li>' % (c['num'], c['h3'], plist(c['paras'])) for c in d['cards']) + '</ol>'))
    d = C['free']
    parts.append(chap(d, ''.join('<div class="group"><h3>%s</h3>%s</div>' % (c['h3'], plist(c['paras'])) for c in d['cards'])))
    parts.append(chap(C['start'], acc(C['start'], False)))
    o = C['own']
    parts.append('<div class="col"><section class="own"><h2>%s</h2><p>%s</p>%s</section></div>' % (o['h2'], o['lead'], plist(o['items'])))
    w = C['work']
    parts.append('<section class="chap" id="work"><div class="col"><p class="kick">%s</p><h2>%s</h2>%s</div></section>' % (w['kicker'], w['title'], work_block()))
    parts.append(chap(C['learn'], acc(C['learn'], False)))
    parts.append('<section class="book" id="book"><div class="col">%s</div></section>' % book_block())
    body = '''<header class="top"><div class="col"><a class="brand" href="#top">%s</a><span style="display:flex;gap:.5rem;align-items:center"><details class="menu"><summary>Menu</summary><nav aria-label="Main">%s</nav></details><a class="pill" href="#book">Book a chat</a></span></div></header>
<main id="top"><section class="hello"><div class="col"><div class="sun" aria-hidden="true"></div><p class="kick">%s</p><h1>%s</h1><p class="lead">%s</p><div class="cta-row" style="justify-content:center">%s</div>
<div class="bubble">%s</div><div class="offer">%s<a href="%s">%s</a></div></div></section>
%s</main>
<footer><div class="col"><span>%s</span><span>%s</span></div></footer>''' % (
        C['brand'], ''.join('<a href="%s">%s</a>' % x for x in C['nav']), h['kicker'], h['h1'], h['lead'],
        ''.join('<a class="pill%s" href="%s">%s</a>' % (' alt' if i else '', h_, t) for i, (h_, t) in enumerate(h['links'])),
        plist(h['card']), C['band']['text'], C['band']['href'], C['band']['link'], '\n'.join(parts), C['footer'][0], C['footer'][1])
    js = '''<script>document.querySelectorAll('details.menu nav a').forEach(function(a){a.addEventListener('click',function(){a.closest('details').open=false})})</script>'''
    return page(4, ['Fraunces:opsz,wght@9..144,700;9..144,800', 'Nunito:wght@400;600;700;800'], css, body, js)

# =====================================================================
# DESIGN 5: Bento (dark canvas, colourful rounded tiles of different sizes)
# =====================================================================
def bento():
    css = '''
:root{--ink:#0B1020;--paper:#0B1020;--line:#2a3354;--muted:#C5CDE6;--link:#1F4FD8;--wlink:#1F4FD8;--f-display:'Sora',system-ui,sans-serif;--f-body:'Sora',system-ui,sans-serif;--r-pill:999px;--r-s:14px;--r-m:24px;--chip-line:#3a4570;--chip-bg:#fff;--chip-fg:#0B1020;--chip-on-bg:#FFD166;--chip-on-fg:#0B1020;--wcard-bg:#F7F3E8;--wcard-line:transparent;--focus:#FFD166}
*{box-sizing:border-box}body{margin:0;background:#0B1020;color:#F2F4FB;font:1.0625rem/1.6 var(--f-body)}
.wrap{max-width:80rem;margin:0 auto;padding:0 1rem}
.float{position:sticky;top:10px;z-index:40;padding:10px 0}
.float .bar{display:flex;flex-wrap:nowrap;align-items:center;gap:.25rem .5rem;max-width:80rem;margin:0 auto;padding:.4rem .5rem .4rem 1.25rem;background:rgba(27,35,64,.88);backdrop-filter:blur(10px);border:1px solid #2f3a64;border-radius:999px}
.float .brand{font-weight:700;color:#fff;text-decoration:none;margin-right:auto;font-size:.9375rem;line-height:1.2;min-width:0}
.float nav{display:flex;gap:2px;overflow-x:auto}
.float nav a{white-space:nowrap;min-height:44px;display:inline-flex;align-items:center;padding:0 .65rem;border-radius:999px;color:#DCE2F5;text-decoration:none;font-weight:600;font-size:.875rem}
.float nav a:hover{background:#2a3560;color:#fff}
.float .go{background:#FFD166;color:#0B1020!important;font-weight:700}
.bento{display:grid;grid-template-columns:repeat(6,1fr);gap:14px}
.t{border-radius:28px;padding:1.5rem;color:#0B1020;min-width:0}
.t h3{margin:0 0 .5rem;font-weight:700;font-size:1.25rem;line-height:1.2;letter-spacing:-.01em}
.t p{margin:0 0 .6rem}.t p:last-child{margin:0}
.c1{background:#FFD166}.c2{background:#A7D3FF}.c3{background:#FFB3C7}.c4{background:#A8E6CF}.c5{background:#D4C1FF}.c6{background:#F7F3E8}.dark{background:#1B2340;color:#F2F4FB}
.s2{grid-column:span 2}.s3{grid-column:span 3}.s4{grid-column:span 4}.s6{grid-column:span 6}
.hero{padding:2rem 0 1rem}
.hero .bento{grid-auto-rows:minmax(8rem,auto)}
.t.title{grid-column:span 4;grid-row:span 2;background:#F7F3E8;padding:2rem}
.t.title .kick{margin:0 0 1rem;font-weight:700;font-size:.8125rem;letter-spacing:.1em;text-transform:uppercase;color:#7a2d10}
.t.title h1{margin:0 0 1rem;font-weight:800;font-size:clamp(2.1rem,5.2vw,4.1rem);line-height:1.02;letter-spacing:-.035em}
.t.title .lead{font-size:1.125rem;max-width:36rem}
.bigcta{display:flex;flex-direction:column;justify-content:space-between;text-decoration:none;color:#0B1020}
.bigcta b{font-size:1.5rem;line-height:1.15;letter-spacing:-.02em}.bigcta span{font-size:2rem;align-self:flex-end}
.sechead{padding:3.5rem 0 1rem}
.sechead .kick{display:inline-block;margin:0 0 .75rem;padding:.25rem .8rem;border-radius:999px;background:#2a3560;color:#FFD166;font-weight:700;font-size:.8125rem;letter-spacing:.08em;text-transform:uppercase}
.sechead h2{margin:0 0 .5rem;font-weight:800;font-size:clamp(1.9rem,4.6vw,3.2rem);line-height:1.05;letter-spacing:-.03em;color:#fff;max-width:52rem}
.sechead p{margin:0 0 .5rem;color:#D3DAF0;max-width:46rem}
.num{font-size:3.5rem;font-weight:800;line-height:1;letter-spacing:-.04em;margin-bottom:.5rem}
.t .links{display:flex;flex-wrap:wrap;gap:.5rem;margin-top:.75rem}
.chipbtn{display:inline-flex;align-items:center;min-height:48px;padding:0 1.25rem;border-radius:999px;background:#0B1020;color:#fff;font-weight:700;text-decoration:none}
.chipbtn.alt{background:transparent;border:2px solid #0B1020;color:#0B1020}
.cta-row{display:flex;flex-wrap:wrap;gap:.6rem;margin-top:1.25rem}
.cta-row .chipbtn{background:#FFD166;color:#0B1020}.cta-row .chipbtn.alt{background:transparent;border:2px solid #FFD166;color:#FFD166}
.note{color:#C5CDE6;margin:1rem 0 0;max-width:46rem}
.band{padding:.5rem 0}.band .t{display:flex;flex-wrap:wrap;align-items:center;justify-content:space-between;gap:.5rem 1rem;font-weight:700;padding:1rem 1.5rem}.band a{color:#0B1020}
.own .t strong{color:#0B1020}
.workbox .t,.bookbox .t{background:#F7F3E8;padding:1.75rem}
.workbox .t,.workbox .t p{color:#222}.workbox .flabel{color:#44485a}.workbox .fcount p{color:#44485a}.workbox .lede{max-width:46rem}
.workbox .linkbtn{color:#1F4FD8}.workbox #emptyState{border-color:#9a9eb8}.workbox #emptyState p{color:#44485a}
.bookbox .t{color:#0B1020}.bookbox h2{margin:0 0 .75rem;font-weight:800;font-size:clamp(1.9rem,4.4vw,3rem);line-height:1.05;letter-spacing:-.03em}.bookbox a{color:#1F4FD8;font-weight:700}
footer{padding:2.5rem 0 6rem;color:#B9C2DE;font-size:.9375rem}footer .wrap{display:flex;flex-wrap:wrap;justify-content:space-between;gap:.5rem 2rem}
@media (max-width:1340px){.float .bar{flex-wrap:wrap;border-radius:24px;padding-left:1rem}.float nav{order:3;width:100%;padding-bottom:.25rem}}
@media (max-width:860px){.t.title,.s4,.s3,.s2{grid-column:span 6}.t.title{grid-row:auto}.float nav{order:3;width:100%;padding-bottom:.25rem}.float .bar{border-radius:24px;padding-left:1rem}.bento{gap:10px}}
@media (min-width:861px) and (max-width:1100px){.s2{grid-column:span 3}}
'''
    h = C['hero']
    pattern = ['s2 c2', 's2 c3', 's2 c4', 's3 c5', 's3 c1', 's2 c6', 's2 c2', 's2 c3', 's4 c4', 's2 c5', 's3 c1', 's3 c2']
    cycle = {2: ['c2', 'c3'], 3: ['c2', 'c3', 'c4'], 4: ['c2', 'c3', 'c4', 'c5']}
    def tiles(d, spans, colors=None, numbers=False):
        out = []
        for k, c in enumerate(d['cards']):
            cl = (colors or ['c2', 'c3', 'c4', 'c5', 'c1', 'c6'])[k % len(colors or ['c2', 'c3', 'c4', 'c5', 'c1', 'c6'])]
            sp = spans[k % len(spans)]
            num = '<div class="num" aria-hidden="true">%s</div>' % c['num'] if numbers and c['num'] else ''
            out.append('<div class="t %s %s">%s<h3>%s</h3>%s</div>' % (sp, cl, num, c['h3'], plist(c['paras'])))
        return '<div class="bento">' + ''.join(out) + '</div>'
    def head(d):
        return '<div class="sechead"><span class="kick">%s</span><h2>%s</h2>%s</div>' % (d['kicker'], d['title'], ''.join('<p>%s</p>' % p for p in d['intro']))
    def tail(d):
        s = ''
        if d['links']: s += '<div class="cta-row">%s</div>' % ''.join('<a class="chipbtn%s" href="%s">%s</a>' % (' alt' if i else '', h_, t) for i, (h_, t) in enumerate(d['links']))
        if d['note']: s += '<p class="note">%s</p>' % d['note']
        return s
    def sec(d, spans, **kw):
        return '<section id="%s"><div class="wrap">%s%s%s</div></section>' % (d['id'], head(d), tiles(d, spans, **kw), tail(d))
    parts = []
    parts.append(sec(C['modernize'], ['s3', 's3', 's3', 's3'], colors=['c1', 'c2', 'c3', 'c4']))
    parts.append(sec(C['events'], ['s2', 's2', 's2'], colors=['c5', 'c4', 'c1']))
    parts.append(sec(C['problems'], ['s2', 's2', 's2', 's3', 's3', 's2'][:0] or ['s2'], colors=['c2', 'c3', 'c4', 'c5', 'c1', 'c6']))
    parts.append(sec(C['services'], ['s3', 's3', 's2', 's2', 's2', 's3', 's3'], colors=['c4', 'c1', 'c5', 'c2', 'c3', 'c6', 'c1']))
    parts.append(sec(C['how'], ['s2'], colors=['c1', 'c2', 'c3'], numbers=True))
    parts.append(sec(C['free'], ['s2'], colors=['c4', 'c5', 'c1']))
    parts.append(sec(C['start'], ['s2'], colors=['c6', 'c2', 'c3', 'c4', 'c5', 'c1']))
    o = C['own']
    parts.append('<section class="own"><div class="wrap"><div class="sechead"><span class="kick">Yours to keep</span><h2>%s</h2><p>%s</p></div><div class="bento">%s</div></div></section>' % (o['h2'], o['lead'], ''.join('<div class="t s2 %s">%s</div>' % (cl, '<p>%s</p>' % p) for cl, p in zip(['c4', 'c1', 'c5'], o['items']))))
    w = C['work']
    parts.append('<section id="work"><div class="wrap"><div class="sechead"><span class="kick">%s</span><h2>%s</h2></div><div class="workbox"><div class="t">%s</div></div></div></section>' % (w['kicker'], w['title'], work_block()))
    parts.append(sec(C['learn'], ['s2'], colors=['c2', 'c3', 'c4']))
    parts.append('<section id="book"><div class="wrap"><div class="sechead"></div><div class="bookbox"><div class="t">%s</div></div></div></section>' % book_block())
    nav = ''.join('<a href="%s">%s</a>' % x for x in C['nav'][:-1])
    body = '''<div class="float"><div class="wrap"><div class="bar"><a class="brand" href="#top">%s</a><nav aria-label="Main">%s</nav><a class="go" href="#book" style="white-space:nowrap;display:inline-flex;min-height:44px;align-items:center;padding:0 1.1rem;border-radius:999px;text-decoration:none;font-weight:700;background:#FFD166;color:#0B1020">Book a chat</a></div></div></div>
<main id="top"><section class="hero"><div class="wrap"><div class="bento">
<div class="t title"><p class="kick">%s</p><h1>%s</h1><p class="lead">%s</p></div>
<div class="t s2 c5"><div>%s</div></div>
<a class="t s2 c1 bigcta" href="%s"><b>%s</b><span aria-hidden="true">&rarr;</span></a>
<a class="t s2 c4 bigcta" href="%s"><b>%s</b><span aria-hidden="true">&darr;</span></a>
<div class="t s4 dark"><p>%s</p><p><a href="%s" style="color:#FFD166;font-weight:700">%s</a></p></div>
</div></div></section>
%s</main>
<footer><div class="wrap"><span>%s</span><span>%s</span></div></footer>''' % (
        C['brand'], nav, h['kicker'], h['h1'], h['lead'], plist(h['card']), h['links'][0][0], h['links'][0][1], h['links'][1][0], h['links'][1][1],
        C['band']['text'], C['band']['href'], C['band']['link'], '\n'.join(parts), C['footer'][0], C['footer'][1])
    return page(5, ['Sora:wght@400;600;700;800'], css, body)
