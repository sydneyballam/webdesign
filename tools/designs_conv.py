"""Three designs built to bring in website customers: 6 Glow-up (before/after slider + cost calculator),
7 Site Maker (build a sample site live), 8 Phone Story (scroll through a customer's evening)."""
from build_studio import *

def sec_html(d, extra='', cls=''):
    cards = ''.join('<div class="c"><h3>%s</h3>%s</div>' % (c['h3'], plist(c['paras'])) for c in d['cards'])
    return '<section class="sec %s" id="%s"><header><p class="kick">%s</p><h2>%s</h2>%s</header><div class="cards">%s</div>%s%s%s</section>' % (
        cls, d['id'], d['kicker'], d['title'], ''.join('<p class="intro">%s</p>' % p for p in d['intro']), cards, extra,
        ('<div class="cta">%s</div>' % links(d['links'])) if d['links'] else '', ('<p class="note">%s</p>' % d['note']) if d['note'] else '')

def steps_html(d):
    return '<section class="sec how" id="how"><header><p class="kick">%s</p><h2>%s</h2></header><div class="cards steps">%s</div></section>' % (
        d['kicker'], d['title'], ''.join('<div class="c"><span class="no">%s</span><h3>%s</h3>%s</div>' % (c['num'], c['h3'], plist(c['paras'])) for c in d['cards']))

def all_sections():
    o = C['own']; w = C['work']
    out = [sec_html(C['modernize']), sec_html(C['events']), sec_html(C['problems']), sec_html(C['services']), steps_html(C['how']), sec_html(C['free']), sec_html(C['start'])]
    out.append('<section class="sec own"><header><p class="kick">Yours to keep</p><h2>%s</h2><p class="intro">%s</p></header><div class="cards">%s</div></section>' % (o['h2'], o['lead'], ''.join('<div class="c">%s</div>' % ('<p>%s</p>' % p) for p in o['items'])))
    out.append('<section class="sec" id="work"><header><p class="kick">%s</p><h2>%s</h2></header><div class="workbox">%s</div></section>' % (w['kicker'], w['title'], work_block()))
    out.append(sec_html(C['learn']))
    out.append('<section class="sec book" id="book"><div class="workbox">%s</div></section>' % book_block())
    return '\n'.join(out)

STALE = '''<div class="stale"><div class="s-top">WELCOME TO OUR WEBSITE!!!</div>
<div class="s-nav"><a>Home</a> | <a>About Us</a> | <a>Services</a> | <a>Events</a> | <a>Contact</a> | <a>Links</a> | <a>Guestbook</a></div>
<div class="s-body"><div class="s-col"><p>Page last updated: <b>2019</b></p><p>Hours: <i>call for hours</i></p><p>Email us at info(at)example(dot)com</p><p class="s-blink">** UNDER CONSTRUCTION **</p></div>
<div class="s-main"><p>Welcome to our website. We are a local business serving the community since many years. Please check back soon for updates.</p><p><a>Upcoming Events (see flyer.pdf)</a></p><p class="s-box">Event: ???<br>Date: ???<br>Time: ???</p><p class="s-count">You are visitor #004211</p></div></div></div>'''
FRESH = '''<div class="fresh"><div class="f-nav"><b>Your Business</b><span>Menu</span><span>Events</span><span>About</span><em>Book now</em></div>
<div class="f-hero"><div><span class="f-chip">Open today, 9 to 5</span><h4>Friendly service, easy to reach.</h4><p>Hours, photos, events and booking, all in one place and always current.</p><span class="f-btn">Book a visit</span></div><div class="f-art"><i></i><i></i><i></i></div></div>
<div class="f-ev"><div><b>12</b><span>NOV</span><p>Open house</p></div><div><b>20</b><span>NOV</span><p>Evening event</p></div><div><b>05</b><span>DEC</span><p>Holiday market</p></div></div></div>'''

# =====================================================================
# 6 GLOW-UP
# =====================================================================
def glowup():
    css = '''
:root{--ink:#1A1033;--paper:#F6F3FF;--line:#D9D1F3;--muted:#4b3f6b;--link:#4B2FD6;--wlink:#4B2FD6;--f-display:'Plus Jakarta Sans',system-ui,sans-serif;--f-body:'Plus Jakarta Sans',system-ui,sans-serif;--r-pill:999px;--r-s:12px;--r-m:20px;--chip-line:#bdb2e8;--chip-bg:#fff;--chip-on-bg:#4B2FD6;--chip-on-fg:#fff;--wcard-line:#D9D1F3;--focus:#FF5C8A}
*{box-sizing:border-box}body{margin:0;background:var(--paper);color:var(--ink);font:1.125rem/1.6 var(--f-body);overflow-x:clip}
.top{position:sticky;top:0;z-index:40;display:flex;align-items:center;gap:1rem;padding:.5rem 2.5vw;background:rgba(26,16,51,.92);backdrop-filter:blur(8px);color:#fff}
.top a.brand{font-weight:800;color:#fff;text-decoration:none;margin-right:auto;line-height:1.2}
.top nav{display:flex;gap:.25rem;overflow-x:auto}.top nav a{white-space:nowrap;min-height:44px;display:inline-flex;align-items:center;padding:0 .8rem;border-radius:999px;color:#E6DFFF;text-decoration:none;font-weight:600;font-size:.9375rem}.top nav a:hover{background:#3a2a73}
.top .go{display:inline-flex;min-height:44px;align-items:center;padding:0 1.2rem;border-radius:999px;background:#FFC93C;color:#1A1033;font-weight:800;text-decoration:none;white-space:nowrap}
.hero{background:radial-gradient(1200px 500px at 85% -10%,#5B3DF5,transparent 60%),radial-gradient(900px 500px at 0% 110%,#FF5C8A55,transparent 60%),#1A1033;color:#fff;padding:3.5rem 2.5vw 3rem}
.hero .kick{margin:0 0 .75rem;font-weight:800;letter-spacing:.12em;text-transform:uppercase;font-size:.875rem;color:#FFC93C}
.hero h1{margin:0 0 1rem;font-weight:800;font-size:clamp(2.2rem,4.8vw,4.6rem);line-height:1;letter-spacing:-.04em;max-width:75rem}
.hero .lead{font-size:1.3rem;max-width:60rem;color:#E6DFFF;margin:0 0 1.5rem}
.btn{display:inline-flex;align-items:center;min-height:52px;padding:0 1.5rem;border-radius:999px;background:#FFC93C;color:#1A1033;font-weight:800;text-decoration:none;margin:0 .7rem .7rem 0;border:3px solid #FFC93C}.btn.alt{background:transparent;color:#fff;border-color:#fff}
.demo{margin-top:2.5rem}
.demo .cap{display:flex;flex-wrap:wrap;justify-content:space-between;gap:.5rem 1rem;margin:0 0 .75rem;font-weight:800}
.demo .cap span:first-child{color:#FF9BB5}.demo .cap span:last-child{color:#7DF0DC}
.stage{position:relative;width:100%;aspect-ratio:16/8.4;border-radius:18px;overflow:hidden;box-shadow:0 30px 70px rgba(0,0,0,.5);border:4px solid #fff;background:#fff;user-select:none;touch-action:pan-y}
.pane{position:absolute;inset:0;overflow:hidden}.pane.after{clip-path:inset(0 0 0 var(--x,50%))}
.inner{width:1000px;height:524px;transform-origin:0 0;transform:scale(var(--s,1))}
.stage input[type=range]{position:absolute;inset:0;width:100%;height:100%;opacity:0;cursor:ew-resize;margin:0;z-index:5}
.handle{position:absolute;top:0;bottom:0;left:var(--x,50%);width:4px;margin-left:-2px;background:#fff;z-index:4;pointer-events:none;box-shadow:0 0 12px rgba(0,0,0,.4)}
.handle::after{content:"\\2194";position:absolute;top:50%;left:50%;width:48px;height:48px;margin:-24px 0 0 -24px;border-radius:50%;background:#FFC93C;color:#1A1033;font:800 1.4rem/48px system-ui;text-align:center;box-shadow:0 4px 14px rgba(0,0,0,.4)}
.stage:focus-within .handle::after{outline:3px solid #fff;outline-offset:3px}
.tag-b,.tag-a{position:absolute;top:12px;z-index:3;padding:.2rem .7rem;border-radius:999px;font-weight:800;font-size:.8125rem;letter-spacing:.06em;text-transform:uppercase}
.tag-b{left:12px;background:#7a1f3d;color:#fff}.tag-a{right:12px;background:#0b6b5c;color:#fff}
.stale{width:1000px;height:524px;background:#c9c9c9 url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='6' height='6'%3E%3Crect width='3' height='3' fill='%23bbb'/%3E%3C/svg%3E");font:16px/1.4 'Times New Roman',serif;color:#000}
.s-top{background:#000080;color:#ff0;text-align:center;font:bold 34px 'Times New Roman',serif;padding:18px;text-shadow:2px 2px #f00}
.s-nav{background:#ddd;border:2px outset #fff;padding:6px 12px;font-size:15px}.s-nav a{color:#00e;text-decoration:underline}
.s-body{display:flex;gap:14px;padding:14px}.s-col{width:240px;background:#eee;border:2px inset #888;padding:10px;font-size:13px}
.s-main{flex:1;font-size:14px}.s-main a{color:#00e;text-decoration:underline}.s-blink{color:#c00;font-weight:bold;text-align:center}.s-box{border:1px dashed #000;padding:8px;background:#ffc;width:220px}.s-count{font:12px monospace;color:#444}
.fresh{width:1000px;height:524px;background:#fff;font:16px/1.5 'Plus Jakarta Sans',system-ui,sans-serif;color:#1A1033}
.f-nav{display:flex;gap:28px;align-items:center;padding:22px 40px;border-bottom:1px solid #eee}.f-nav b{margin-right:auto;font-size:20px}.f-nav em{font-style:normal;background:#5B3DF5;color:#fff;padding:9px 18px;border-radius:999px;font-weight:700}
.f-hero{display:flex;gap:30px;padding:36px 40px;align-items:center;background:linear-gradient(120deg,#F6F3FF,#fff)}.f-hero>div:first-child{flex:1}
.f-chip{display:inline-block;background:#DDF8F2;color:#0b6b5c;font-weight:700;font-size:13px;padding:4px 12px;border-radius:999px;margin-bottom:12px}
.f-hero h4{margin:0 0 8px;font-size:40px;line-height:1.05;letter-spacing:-.03em}.f-hero p{margin:0 0 16px;max-width:430px}
.f-btn{display:inline-block;background:#5B3DF5;color:#fff;padding:12px 24px;border-radius:999px;font-weight:700}
.f-art{position:relative;width:300px;height:210px}.f-art i{position:absolute;border-radius:24px}.f-art i:nth-child(1){inset:0 60px 40px 0;background:linear-gradient(135deg,#5B3DF5,#8d77ff)}.f-art i:nth-child(2){right:0;top:50px;width:150px;height:140px;background:#FFC93C}.f-art i:nth-child(3){left:40px;bottom:0;width:120px;height:90px;background:#FF5C8A}
.f-ev{display:flex;gap:18px;padding:10px 40px}.f-ev div{flex:1;border:1px solid #e6e1f7;border-radius:16px;padding:14px;display:grid;grid-template-columns:auto 1fr;gap:0 12px;align-items:center}.f-ev b{font-size:34px;grid-row:span 2;color:#5B3DF5}.f-ev span{font-size:12px;font-weight:700;letter-spacing:.1em}.f-ev p{margin:0;font-weight:600}
.calc{margin-top:2rem;display:grid;grid-template-columns:1.1fr 1fr;gap:1.5rem;background:#fff;color:var(--ink);border-radius:24px;padding:1.75rem;box-shadow:0 20px 50px rgba(0,0,0,.35)}
.calc h2{margin:0 0 .5rem;font-size:clamp(1.5rem,2.6vw,2.2rem);letter-spacing:-.02em;line-height:1.1}
.calc label{display:block;font-weight:700;margin:1rem 0 .3rem}.calc input[type=range]{width:100%;accent-color:#4B2FD6;min-height:32px}
.calc input[type=number]{min-height:48px;width:9rem;border:2px solid #bdb2e8;border-radius:10px;padding:0 .75rem;font:700 1.1rem var(--f-body);color:var(--ink)}
.calc .out{background:#1A1033;color:#fff;border-radius:18px;padding:1.5rem;display:flex;flex-direction:column;justify-content:center}
.calc .out b{font-size:clamp(2.4rem,5vw,4.2rem);line-height:1;letter-spacing:-.03em;color:#FFC93C}.calc .out p{margin:.5rem 0 0;color:#E6DFFF}
.sec{padding:4.5rem 2.5vw}.sec:nth-of-type(even){background:#fff}
.sec header{max-width:62rem;margin-bottom:2rem}
.kick{margin:0 0 .5rem;font-weight:800;letter-spacing:.12em;text-transform:uppercase;font-size:.875rem;color:#4B2FD6}
.sec h2{margin:0 0 .75rem;font-weight:800;font-size:clamp(2rem,4.4vw,4rem);line-height:1.02;letter-spacing:-.035em}
.cards{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,19rem),1fr));gap:1.25rem;counter-reset:c}
.c{position:relative;background:#fff;border:2px solid var(--line);border-radius:24px;padding:1.6rem 1.5rem 1.5rem;overflow:hidden}
.sec:nth-of-type(even) .c{background:var(--paper)}
.c::before{counter-increment:c;content:counter(c,decimal-leading-zero);position:absolute;right:1rem;top:.25rem;font-weight:800;font-size:4rem;line-height:1;color:#EAE4FF}
.c h3{position:relative;margin:0 0 .5rem;font-weight:800;font-size:1.35rem;line-height:1.2;max-width:85%}.c p{position:relative;margin:0 0 .6rem}
.steps .c::before{display:none}.steps .no{display:inline-flex;width:3rem;height:3rem;border-radius:50%;background:linear-gradient(135deg,#5B3DF5,#FF5C8A);color:#fff;font-weight:800;align-items:center;justify-content:center;margin-bottom:.6rem}
.own{background:linear-gradient(120deg,#1A1033,#3a1f86)!important;color:#fff}.own .kick{color:#FFC93C}.own .c{background:rgba(255,255,255,.1)!important;border-color:rgba(255,255,255,.25)}.own .c::before{display:none}.own .intro{color:#E6DFFF}
.cta{margin-top:1.5rem}.cta .btn{background:#4B2FD6;color:#fff;border-color:#4B2FD6}.cta .btn.alt{background:transparent;color:#4B2FD6}.note{margin:1.5rem 0 0;max-width:56rem;color:var(--muted);font-style:italic}
.intro{max-width:56rem;margin:0 0 .5rem}
.workbox{background:#fff;border:2px solid var(--line);border-radius:24px;padding:1.5rem}.workbox .lede{max-width:80rem;margin:0 0 .6rem}.workbox h2{margin:0 0 .75rem;font-size:clamp(1.8rem,3.4vw,3rem)}
.book{background:linear-gradient(120deg,#F6F3FF,#EAE4FF)!important}
.foot{padding:2rem 2.5vw 5rem;display:flex;flex-wrap:wrap;justify-content:space-between;gap:.5rem 2rem;font-size:.9375rem;color:var(--muted)}
@media (max-width:900px){.calc{grid-template-columns:1fr}.top nav{display:none}.stage{aspect-ratio:4/3}}
'''
    h = C['hero']
    body = fill('''<header class="top"><a class="brand" href="#top">[[brand]]</a><nav aria-label="Main">[[nav]]</nav><a class="go" href="#book">Book a free chat</a></header>
<main id="top"><section class="hero"><p class="kick">[[kicker]]</p><h1>[[h1]]</h1><p class="lead">[[lead]]</p><div>[[links]]</div>
<div class="demo"><div class="cap"><span>Before: slow to change, easy to ignore</span><span>After: current, clear and yours to edit</span></div>
<div class="stage" id="stage" style="--x:50%"><div class="pane before" aria-hidden="true"><div class="inner">[[stale]]</div></div><div class="pane after" aria-hidden="true"><div class="inner">[[fresh]]</div></div><span class="tag-b" aria-hidden="true">Before</span><span class="tag-a" aria-hidden="true">After</span><div class="handle" aria-hidden="true"></div>
<input type="range" id="cmp" min="0" max="100" value="50" aria-label="Drag to compare an old website with a modernized one"></div>
<p style="margin:.75rem 0 0;color:#cfc6ee;font-size:.9375rem">An illustration, not a real business. Drag the handle.</p></div>
<div class="calc"><div><h2>What do website changes cost you today?</h2><p style="margin:0;color:#4b3f6b">Put in your own numbers. This stays on your device.</p>
<label for="n">Changes a year: <span id="nv">12</span></label><input id="n" type="range" min="1" max="60" value="12">
<label for="fee">Fee per change ($)</label><input id="fee" type="number" min="0" value="50" inputmode="numeric"></div>
<div class="out" aria-live="polite"><p style="margin:0">At that rate, updates cost you</p><b id="tot">$600</b><p>a year. When you edit your own site, that line is $0.</p></div></div></section>
<div class="sec" style="padding:1rem 2.5vw;background:#FFC93C;color:#1A1033;font-weight:800">[[sale]] <a href="[[salehref]]" style="color:#1A1033">[[salelink]]</a></div>
[[sections]]</main><div class="foot"><span>[[f0]]</span><span>[[f1]]</span></div>''', brand=C['brand'], nav=''.join('<a href="%s">%s</a>' % x for x in C['nav']), kicker=h['kicker'], h1=h['h1'], lead=h['lead'], links=links(h['links']),
        stale=STALE, fresh=FRESH, sale=C['band']['text'], salehref=C['band']['href'], salelink=C['band']['link'], sections=all_sections(), f0=C['footer'][0], f1=C['footer'][1])
    js = '''<script>
(function(){var st=document.getElementById('stage'),r=document.getElementById('cmp');
function fit(){var s=st.clientWidth/1000;st.style.setProperty('--s',s);st.style.height=(524*s)+'px'}
function set(v){st.style.setProperty('--x',v+'%')}
fit();addEventListener('resize',fit);r.addEventListener('input',function(){set(r.value)});
if(!matchMedia('(prefers-reduced-motion:reduce)').matches){var t0=null,go=true;r.addEventListener('pointerdown',function(){go=false});r.addEventListener('keydown',function(){go=false});
function tick(t){if(!go)return;if(t0===null)t0=t;var p=(t-t0)/2600;if(p>=1){r.value=50;set(50);return}var v=50+Math.sin(p*Math.PI*2)*(35*(1-p));r.value=v;set(v);requestAnimationFrame(tick)}
setTimeout(function(){requestAnimationFrame(tick)},700)}
var n=document.getElementById('n'),f=document.getElementById('fee'),nv=document.getElementById('nv'),tot=document.getElementById('tot');
function calc(){var x=(+n.value||0)*(+f.value||0);nv.textContent=n.value;tot.textContent='$'+x.toLocaleString('en-US')}
n.addEventListener('input',calc);f.addEventListener('input',calc);calc();
})();
</script>'''
    return page(6, ['Plus+Jakarta+Sans:wght@400;600;700;800'], css, body, js)

# =====================================================================
# 7 SITE MAKER
# =====================================================================
def sitemaker():
    css = '''
:root,:root[data-vibe=warm]{--ink:#3a2412;--paper:#FFF6EA;--line:#EBD3B0;--muted:#5d4630;--link:#9A3412;--wlink:#9A3412;--soft:#F7E2C2;--kick:#9A3412;--btn:#3a2412;--btn-on:#fff;--cta:#F4B860;--cta-on:#3a2412;--c1:#FFE2B8;--c2:#F9CBA6;--c3:#FFEBC9;--c4:#F5D2B0;--c5:#FFDCC2;--dark:#3a2412;--darkc:#55361d;--darkk:#F4B860;--sale:#F4B860;--sale-on:#3a2412;--chip-line:#cdac7d;--chip-bg:#fff;--chip-on-bg:#3a2412;--chip-on-fg:#fff;--wcard-line:#EBD3B0;--focus:#9A3412;--f-display:Georgia,'Times New Roman',serif;--rad:14px}
:root[data-vibe=fresh]{--ink:#10392b;--paper:#F1FBF5;--line:#BFE3CF;--muted:#2f5d4b;--link:#0A6B43;--wlink:#0A6B43;--soft:#D3F0E0;--kick:#0A6B43;--btn:#10392b;--btn-on:#fff;--cta:#BDEBD3;--cta-on:#10392b;--c1:#C9F0DC;--c2:#DDF4B8;--c3:#BFEBE3;--c4:#E3F7C9;--c5:#CFEFD0;--dark:#10392b;--darkc:#1c5240;--darkk:#9BE3BC;--sale:#BDEBD3;--sale-on:#10392b;--chip-line:#8cc7a8;--chip-bg:#fff;--chip-on-bg:#10392b;--chip-on-fg:#fff;--wcard-line:#BFE3CF;--focus:#0A6B43;--f-display:'Outfit',system-ui,sans-serif;--rad:24px}
:root[data-vibe=bold]{--ink:#FFFFFF;--paper:#16122B;--line:#3A3366;--muted:#CFC9EE;--link:#FFD23F;--wlink:#FFD23F;--soft:#2A2450;--kick:#FFD23F;--btn:#FF4F8B;--btn-on:#16122B;--cta:#FFD23F;--cta-on:#16122B;--c1:#FF6FA0;--c2:#FFD23F;--c3:#6FE7EC;--c4:#BBA9FF;--c5:#FFA95A;--dark:#0B0820;--darkc:#1E1842;--darkk:#FFD23F;--sale:#FF4F8B;--sale-on:#16122B;--chip-line:#6c62b0;--chip-bg:#fff;--chip-on-bg:#FFD23F;--chip-on-fg:#16122B;--wcard-line:#3A3366;--focus:#FFD23F;--f-display:'Outfit',system-ui,sans-serif;--rad:4px}
:root[data-vibe=calm]{--ink:#1b2b44;--paper:#F1F5FA;--line:#CAD8EC;--muted:#3f5575;--link:#2B4C8C;--wlink:#2B4C8C;--soft:#DCE6F4;--kick:#2B4C8C;--btn:#1b2b44;--btn-on:#fff;--cta:#C9D8EE;--cta-on:#1b2b44;--c1:#D6E3F5;--c2:#E3EAF3;--c3:#CBDCEC;--c4:#E8E4F3;--c5:#D3E4E8;--dark:#1b2b44;--darkc:#2b4163;--darkk:#AFC6EA;--sale:#C9D8EE;--sale-on:#1b2b44;--chip-line:#9db4d6;--chip-bg:#fff;--chip-on-bg:#1b2b44;--chip-on-fg:#fff;--wcard-line:#CAD8EC;--focus:#2B4C8C;--f-display:'Outfit',system-ui,sans-serif;--rad:28px}
:root{--f-body:'Outfit',system-ui,sans-serif;--r-pill:999px;--r-s:12px;--r-m:var(--rad)}
*{box-sizing:border-box}body{margin:0;background:var(--paper);color:var(--ink);font:1.125rem/1.55 var(--f-body);overflow-x:clip}
html.swap *{transition:background-color .4s,color .4s,border-color .4s,border-radius .4s}
@media (prefers-reduced-motion:reduce){html.swap *{transition:none}}
h1,h2,h3{font-family:var(--f-display)}
.top{display:flex;align-items:center;gap:1rem;padding:.75rem 2.5vw}.top a.brand{font-weight:800;color:var(--ink);text-decoration:none;margin-right:auto;font-size:1.1rem;line-height:1.2}
.top nav{display:flex;gap:.1rem;flex-wrap:wrap}.top nav a{min-height:44px;display:inline-flex;align-items:center;padding:0 .6rem;border-radius:999px;color:var(--ink);text-decoration:none;font-weight:600;font-size:.9375rem}.top nav a:hover{background:var(--soft)}
.go{white-space:nowrap;display:inline-flex;min-height:46px;align-items:center;padding:0 1.3rem;border-radius:999px;background:var(--btn);color:var(--btn-on);font-weight:700;text-decoration:none}
.maker{display:grid;grid-template-columns:minmax(20rem,28rem) 1fr;gap:2rem;padding:1rem 2.5vw 3rem;align-items:start}
.panel h1{margin:0 0 .5rem;font-weight:800;font-size:clamp(2.1rem,3.6vw,3.5rem);line-height:1.02;letter-spacing:-.035em}
.panel .lead{margin:0 0 1.25rem}
.panel fieldset{border:0;padding:0;margin:0 0 1rem}.panel legend{font-weight:800;font-size:.875rem;letter-spacing:.08em;text-transform:uppercase;margin-bottom:.4rem;color:var(--kick);padding:0}
.opts{display:flex;flex-wrap:wrap;gap:.45rem}
.opts label{position:relative}.opts input{position:absolute;opacity:0;inset:0;width:100%;height:100%;margin:0;cursor:pointer}
.opts span{display:inline-flex;align-items:center;min-height:44px;padding:0 1rem;border-radius:999px;border:2px solid var(--chip-line);background:var(--chip-bg);color:#1b1b1b;font-weight:700}
.opts input:checked+span{background:var(--chip-on-bg);border-color:var(--chip-on-bg);color:var(--chip-on-fg)}
.opts input:focus-visible+span{outline:3px solid var(--focus);outline-offset:2px}
.panel input[type=text]{width:100%;min-height:50px;border:2px solid var(--chip-line);border-radius:12px;padding:0 .9rem;font:600 1.1rem var(--f-body);background:#fff;color:#1b1b1b}
.actions{display:flex;flex-wrap:wrap;gap:.6rem;margin-top:1.25rem}
.btn{display:inline-flex;align-items:center;min-height:52px;padding:0 1.4rem;border-radius:999px;background:var(--cta);color:var(--cta-on);font:800 1rem var(--f-body);text-decoration:none;border:3px solid var(--cta-on);cursor:pointer}.btn.alt{background:transparent;color:var(--ink);border-color:var(--ink)}
.hint{font-size:.9375rem;color:var(--muted);margin:.6rem 0 0}
.laptop{position:sticky;top:12px;border-radius:18px;background:#14202B;padding:12px 12px 16px;box-shadow:0 30px 60px rgba(20,32,43,.35)}
.chrome{display:flex;align-items:center;gap:6px;padding:0 4px 8px}.chrome i{width:11px;height:11px;border-radius:50%;background:#ff5f56}.chrome i:nth-child(2){background:#ffbd2e}.chrome i:nth-child(3){background:#27c93f}
.chrome .url{margin-left:10px;flex:1;background:#2a3a48;color:#cfe0ee;border-radius:999px;padding:3px 14px;font-size:.8125rem;overflow:hidden;white-space:nowrap;text-overflow:ellipsis}
.screen{background:var(--pbg,#fff);color:var(--pink,#222);border-radius:8px;min-height:30rem;overflow:hidden;font-family:var(--pfont,'Outfit',sans-serif);transition:background .3s,color .3s}
.p-nav{display:flex;align-items:center;gap:1rem;padding:1rem 1.5rem}.p-nav b{margin-right:auto;font-size:1.2rem}.p-nav span{font-size:.9rem;opacity:.85}.p-nav em{font-style:normal;background:var(--pacc);color:var(--pon);padding:.45rem 1rem;border-radius:999px;font-weight:700;font-size:.9rem}
.p-hero{display:grid;grid-template-columns:1.2fr 1fr;gap:1.5rem;padding:1.5rem;align-items:center}
.p-hero h2{margin:0 0 .5rem;font-size:clamp(1.6rem,3.2vw,3rem);line-height:1.02;letter-spacing:-.03em}.p-hero p{margin:0 0 1rem;max-width:30rem}
.p-btn{display:inline-block;background:var(--pacc);color:var(--pon);padding:.7rem 1.3rem;border-radius:999px;font-weight:800}
.p-art{position:relative;aspect-ratio:1/.8}.p-art i{position:absolute;border-radius:var(--prad,24px)}.p-art i:nth-child(1){inset:0 22% 20% 0;background:var(--pacc)}.p-art i:nth-child(2){right:0;top:18%;width:40%;height:50%;background:var(--pacc2)}.p-art i:nth-child(3){left:12%;bottom:0;width:36%;height:34%;background:var(--pink);opacity:.85}
.p-row{display:grid;grid-template-columns:repeat(auto-fit,minmax(9rem,1fr));gap:.8rem;padding:0 1.5rem 1.5rem}
.p-card{border:2px solid var(--pacc);border-radius:var(--prad,18px);padding:.9rem}.p-card b{display:block;margin-bottom:.15rem}.p-card span{font-size:.9rem;opacity:.85}
.p-ev b{font-size:1.8rem;line-height:1;color:var(--pacc)}
.p-gal{display:grid;grid-template-columns:repeat(4,1fr);gap:.5rem;padding:0 1.5rem 1.5rem}.p-gal i{aspect-ratio:1;border-radius:var(--prad,12px);background:var(--pacc)}.p-gal i:nth-child(2){background:var(--pacc2)}.p-gal i:nth-child(3){background:var(--pink);opacity:.8}.p-gal i:nth-child(4){background:var(--pacc2);opacity:.6}
.p-foot{padding:1rem 1.5rem;font-size:.85rem;opacity:.8;border-top:1px solid color-mix(in srgb,var(--pink) 20%,transparent)}
.sample{margin:.75rem 0 0;color:#9fb3c4;font-size:.875rem;text-align:center}
.strip{display:flex;gap:1rem;overflow-x:auto;scroll-snap-type:x mandatory;padding:.5rem 2.5vw 1.5rem;margin:0;list-style:none}
.sec{padding:3.5rem 0 1rem}.sec header{padding:0 2.5vw;max-width:70rem}
.kick{margin:0 0 .4rem;font-weight:800;letter-spacing:.1em;text-transform:uppercase;font-size:.875rem;color:var(--kick)}
.sec h2{margin:0 0 .6rem;font-weight:800;font-size:clamp(2rem,4.2vw,3.8rem);line-height:1.02;letter-spacing:-.035em}
.intro{max-width:54rem;margin:0 0 .4rem}
.cards{display:flex;gap:1rem;overflow-x:auto;scroll-snap-type:x mandatory;padding:1rem 2.5vw 1.25rem;scrollbar-color:var(--ink) var(--soft)}
.c{flex:0 0 min(86vw,23rem);scroll-snap-align:start;border-radius:calc(var(--rad) + 12px);padding:1.6rem;background:var(--cc,var(--c1));color:#14202B;min-height:15rem}
.c:nth-child(5n+1){--cc:var(--c1)}.c:nth-child(5n+2){--cc:var(--c2)}.c:nth-child(5n+3){--cc:var(--c3)}.c:nth-child(5n+4){--cc:var(--c4)}.c:nth-child(5n+5){--cc:var(--c5)}
.c h3{margin:0 0 .6rem;font-weight:800;font-size:1.45rem;line-height:1.12;letter-spacing:-.02em}.c p{margin:0 0 .6rem}
.steps .no{display:inline-flex;width:3.2rem;height:3.2rem;border-radius:50%;background:#14202B;color:#fff;font-weight:800;align-items:center;justify-content:center;font-size:1.3rem;margin-bottom:.6rem}
.sale{padding:.6rem 2.5vw;background:var(--sale);color:var(--sale-on);font-weight:800}.sale a{color:var(--sale-on)}
.swipe{padding:0 2.5vw;font-size:.875rem;color:var(--muted);margin:.25rem 0 0}
.cta{padding:.5rem 2.5vw 0}.cta .btn{margin:0 .6rem .6rem 0}.note{padding:0 2.5vw;margin:.75rem 0 0;max-width:60rem;color:var(--muted);font-style:italic}
.own{background:var(--dark);color:#fff;margin-top:2.5rem;padding-bottom:2rem}.own .kick{color:var(--darkk)}.own .c{background:var(--darkc);color:#fff}
.workbox{--ink:#14202B;--muted:#4a5a68;--link:#0B5CAD;--wlink:#0B5CAD;--chip-on-bg:#14202B;--chip-on-fg:#fff;--chip-line:#9aa3ad;margin:1rem 2.5vw 0;background:#fff;color:#14202B;border:2px solid var(--line);border-radius:calc(var(--rad) + 12px);padding:1.5rem}.workbox .lede{max-width:80rem;margin:0 0 .5rem}.workbox h2{font-size:clamp(1.8rem,3.4vw,3rem)}
.book{padding-bottom:3rem}
.foot{padding:1.5rem 2.5vw 5rem;display:flex;flex-wrap:wrap;justify-content:space-between;gap:.5rem 2rem;font-size:.9375rem;color:var(--muted)}
@media (max-width:980px){.maker{grid-template-columns:1fr}.laptop{position:static}.p-hero{grid-template-columns:1fr}.top nav{display:none}}
'''
    h = C['hero']
    radio = lambda name, items, first: ''.join('<label><input type="radio" name="%s" value="%s"%s><span>%s</span></label>' % (name, v, ' checked' if i == 0 else '', t) for i, (v, t) in enumerate(items))
    types = [('cafe', 'Cafe or bakery'), ('shop', 'Shop'), ('trades', 'Trades or repair'), ('stay', 'Lodging or guide'), ('studio', 'Studio or services'), ('group', 'Club or nonprofit')]
    vibes = [('warm', 'Warm'), ('fresh', 'Fresh'), ('bold', 'Bold'), ('calm', 'Calm')]
    feats = [('book', 'Online booking'), ('events', 'Events calendar'), ('gallery', 'Photo gallery')]
    body = fill('''<header class="top"><a class="brand" href="#top">[[brand]]</a><nav aria-label="Main">[[nav]]</nav><a class="go" href="#book">Book a free chat</a></header>
<main id="top"><section class="maker"><div class="panel"><h1>[[h1]]</h1><p class="lead">[[lead]]</p>
<form id="mk" onsubmit="return false"><fieldset><legend>Business name</legend><input type="text" id="nm" value="Your Business" maxlength="40" aria-label="Business name" autocomplete="off"></fieldset>
<fieldset><legend>What kind of business?</legend><div class="opts">[[types]]</div></fieldset>
<fieldset><legend>Pick a feel</legend><div class="opts">[[vibes]]</div></fieldset>
<fieldset><legend>Include</legend><div class="opts">[[feats]]</div></fieldset></form>
<div class="actions"><a class="btn" href="#book">Make mine real: book a free chat</a><button class="btn alt" type="button" id="cp">Copy my idea</button></div>
<p class="hint" id="hint">Play with it. Paste your idea into the booking notes and we start from there.</p><div style="margin-top:1rem">[[links]]</div></div>
<div><div class="laptop"><div class="chrome" aria-hidden="true"><i></i><i></i><i></i><span class="url" id="url">yourbusiness.com</span></div><div class="screen" id="screen" aria-live="polite"></div></div><p class="sample">A live sample of what could be built. Wording and shapes are placeholders.</p></div></section>
<section class="sec sale">[[sale]] <a href="[[salehref]]">[[salelink]]</a></section>
[[sections]]</main><div class="foot"><span>[[f0]]</span><span>[[f1]]</span></div>''', brand=C['brand'], nav=''.join('<a href="%s">%s</a>' % x for x in C['nav']), h1=h['h1'], lead=h['lead'], links=links(h['links']),
        types=radio('type', types, 0), vibes=radio('vibe', vibes, 0), feats=''.join('<label><input type="checkbox" name="f" value="%s"%s><span>%s</span></label>' % (v, ' checked' if v != 'gallery' else '', t) for v, t in feats),
        sale=C['band']['text'], salehref=C['band']['href'], salelink=C['band']['link'], sections=all_sections().replace('<div class="cards">', '<div class="cards" tabindex="0" role="region" aria-label="Swipe sideways to see more">'), f0=C['footer'][0], f1=C['footer'][1])
    js = '''<script>
(function(){
var T={cafe:{h:'Good food, made fresh every day.',p:'Come in, say hi, and see what is on today.',cta:'Order or reserve',items:[['Menu','Seasonal favorites'],['Hours','Open today, 7 to 3'],['Catering','Ask about group orders']],ev:['Live music night','Pie and coffee morning']},
shop:{h:'Local finds you will not see anywhere else.',p:'Browse what is new, then stop by the shop.',cta:'Shop what is new',items:[['New arrivals','Fresh this week'],['Hours','Open today, 10 to 6'],['Gift cards','Easy to send']],ev:['Holiday open house','Makers market']},
trades:{h:'Fast, honest work you can count on.',p:'Tell us what you need and get a straight answer.',cta:'Request a visit',items:[['Services','What we handle'],['Service area','Right here at home'],['Estimates','Clear and upfront']],ev:['Free tune-up day','Open shop hours']},
stay:{h:'Your base for the whole adventure.',p:'See the rooms, check dates and plan your stay.',cta:'Check dates',items:[['Rooms','Cozy and comfortable'],['Trips','Guided and self-guided'],['Local tips','Where to eat and go']],ev:['Sunset hike','Guest cookout']},
studio:{h:'Work that helps you move forward.',p:'See what we offer and book a time that suits you.',cta:'Book a session',items:[['Services','Pick what fits'],['About','Who you will work with'],['Hours','Easy online scheduling']],ev:['Open studio night','Beginner workshop']},
group:{h:'Better together, one event at a time.',p:'Find out what is happening and how to join in.',cta:'Join us',items:[['Get involved','There is room for you'],['Donate','Every bit helps'],['Meetings','Open to everyone']],ev:['Community meeting','Fundraiser night']}};
var V={warm:{bg:'#FFF6EA',ink:'#3a2412',acc:'#C2410C',acc2:'#F4B860',on:'#fff',font:"Georgia,'Times New Roman',serif",rad:'14px'},fresh:{bg:'#F2FBF6',ink:'#10392b',acc:'#0E8F5B',acc2:'#BDEBD3',on:'#fff',font:"'Outfit',system-ui,sans-serif",rad:'22px'},bold:{bg:'#16122B',ink:'#fff',acc:'#FF4F8B',acc2:'#FFD23F',on:'#16122B',font:"'Outfit',system-ui,sans-serif",rad:'4px'},calm:{bg:'#F1F5FA',ink:'#1b2b44',acc:'#35599A',acc2:'#C9D8EE',on:'#fff',font:"'Outfit',system-ui,sans-serif",rad:'28px'}};
var f=document.getElementById('mk'),sc=document.getElementById('screen'),url=document.getElementById('url'),root=document.documentElement;
function esc(s){return s.replace(/[&<>"]/g,function(c){return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]})}
function val(n){var e=f.querySelector('input[name='+n+']:checked');return e?e.value:''}
function render(){var name=(document.getElementById('nm').value.trim()||'Your Business'),t=T[val('type')],v=V[val('vibe')],on={};[].forEach.call(f.querySelectorAll('input[name=f]:checked'),function(i){on[i.value]=1});
var vb=val('vibe');if(root.getAttribute('data-vibe')!==vb){root.classList.add('swap');root.setAttribute('data-vibe',vb);setTimeout(function(){root.classList.remove('swap')},600);try{sessionStorage.setItem('vibe',vb)}catch(e){}}
var st=sc.style;st.setProperty('--pbg',v.bg);st.setProperty('--pink',v.ink);st.setProperty('--pacc',v.acc);st.setProperty('--pacc2',v.acc2);st.setProperty('--pon',v.on);st.setProperty('--pfont',v.font);st.setProperty('--prad',v.rad);
var slug=name.toLowerCase().replace(/[^a-z0-9]+/g,'').slice(0,24)||'yourbusiness';url.textContent=slug+'.com';
var h='<div class="p-nav"><b>'+esc(name)+'</b><span>About</span>'+(on.events?'<span>Events</span>':'')+(on.gallery?'<span>Gallery</span>':'')+(on.book?'<em>'+esc(t.cta)+'</em>':'')+'</div>';
h+='<div class="p-hero"><div><h2>'+esc(t.h)+'</h2><p>'+esc(t.p)+'</p>'+(on.book?'<span class="p-btn">'+esc(t.cta)+'</span>':'')+'</div><div class="p-art" aria-hidden="true"><i></i><i></i><i></i></div></div>';
h+='<div class="p-row">'+t.items.map(function(i){return '<div class="p-card"><b>'+esc(i[0])+'</b><span>'+esc(i[1])+'</span></div>'}).join('')+'</div>';
if(on.events)h+='<div class="p-row">'+t.ev.map(function(e,i){return '<div class="p-card p-ev"><b>'+(i?'28':'14')+'</b> <span>'+(i?'NOV':'NOV')+'</span><br><span>'+esc(e)+'</span></div>'}).join('')+'</div>';
if(on.gallery)h+='<div class="p-gal" aria-hidden="true"><i></i><i></i><i></i><i></i></div>';
h+='<div class="p-foot">'+esc(name)+' &middot; Willow Creek, California &middot; Updated by you, any time</div>';sc.innerHTML=h;
sc.dataset.sum='Website idea: '+name+' ('+document.querySelector('input[name=type]:checked+span').textContent+'), feel: '+document.querySelector('input[name=vibe]:checked+span').textContent+', include: '+(Object.keys(on).join(', ')||'just the basics')}
f.addEventListener('input',render);f.addEventListener('change',render);render();
document.getElementById('cp').addEventListener('click',function(){var t=sc.dataset.sum,h=document.getElementById('hint');
function ok(){h.textContent='Copied. Paste it into the booking notes.'}
if(navigator.clipboard&&navigator.clipboard.writeText)navigator.clipboard.writeText(t).then(ok,function(){h.textContent=t});else h.textContent=t})
})();
</script>'''
    return page(7, ['Outfit:wght@400;600;700;800'], css, body, js)

# =====================================================================
# 8 PHONE STORY
# =====================================================================
def phonestory():
    css = '''
:root{--ink:#10243E;--paper:#EAF3FF;--line:#C8DBF3;--muted:#40566F;--link:#0B58C2;--wlink:#0B58C2;--f-display:'Manrope',system-ui,sans-serif;--f-body:'Manrope',system-ui,sans-serif;--r-pill:999px;--r-s:12px;--r-m:20px;--chip-line:#9bb8de;--chip-bg:#fff;--chip-on-bg:#10243E;--chip-on-fg:#fff;--wcard-line:#C8DBF3;--focus:#FF7A2F}
*{box-sizing:border-box}body{margin:0;background:var(--paper);color:var(--ink);font:1.125rem/1.6 var(--f-body);overflow-x:clip}
.top{position:sticky;top:0;z-index:40;display:flex;align-items:center;gap:1rem;padding:.5rem 2.5vw;background:rgba(234,243,255,.92);backdrop-filter:blur(8px);border-bottom:1px solid var(--line)}
.top a.brand{font-weight:800;color:var(--ink);text-decoration:none;margin-right:auto;line-height:1.2}.top nav{display:flex;gap:.2rem;overflow-x:auto}.top nav a{white-space:nowrap;min-height:44px;display:inline-flex;align-items:center;padding:0 .8rem;border-radius:999px;color:var(--ink);text-decoration:none;font-weight:700;font-size:.9375rem}.top nav a:hover{background:#D6E7FB}
.go{display:inline-flex;min-height:44px;align-items:center;padding:0 1.2rem;border-radius:999px;background:#FF7A2F;color:#10243E;font-weight:800;text-decoration:none;white-space:nowrap}
.story{display:grid;grid-template-columns:1fr minmax(18rem,26rem) 1fr;gap:0 3vw;padding:0 2.5vw}
.steps-col{grid-column:1;padding:2rem 0}.phone-col{grid-column:2;grid-row:1}.right-col{grid-column:3;padding:2rem 0}
.phone-col{position:relative}.stick{position:sticky;top:5rem;padding:1rem 0}
.phone{width:100%;max-width:22rem;margin:0 auto;aspect-ratio:9/18.5;border-radius:42px;background:#0b1626;padding:12px;box-shadow:0 30px 60px rgba(16,36,62,.4)}
.scr{position:relative;width:100%;height:100%;border-radius:32px;overflow:hidden;background:#fff}
.scr .s{position:absolute;inset:0;padding:2.2rem 1rem 1rem;opacity:0;transform:translateY(12px);transition:opacity .35s,transform .35s;font-size:1.0625rem;line-height:1.45;overflow:hidden;visibility:hidden}
.scr .s.on{opacity:1;transform:none;visibility:visible}
@media (prefers-reduced-motion:reduce){.scr .s{transition:none}}
.notch{position:absolute;top:8px;left:50%;width:34%;height:18px;margin-left:-17%;border-radius:12px;background:#0b1626;z-index:3}
.s h4{margin:0 0 .7rem;font-size:1.3rem;line-height:1.15}
.sb{background:#F1F3F4;border-radius:999px;padding:.55rem .9rem;font-weight:600;margin-bottom:.8rem}
.res{border-radius:12px;padding:1rem;margin-bottom:.8rem;border:1px solid #e3e6ea}.res.me{border:2px solid #0B58C2;background:#F2F7FF}.res b{display:block;color:#0B58C2}.res span{color:#3b6a43;font-weight:700}.res.dim{opacity:.55}
.mini-hero{background:linear-gradient(135deg,#0B58C2,#6AA6FF);color:#fff;border-radius:16px;padding:1rem;margin-bottom:.7rem}.mini-hero h4{font-size:1.2rem}
.pill{display:inline-block;background:#FF7A2F;color:#10243E;font-weight:800;border-radius:999px;padding:.4rem .9rem;margin-right:.3rem}.pill.o{background:transparent;border:2px solid #fff;color:#fff}
.ev{display:flex;gap:.8rem;align-items:center;border:1px solid #e3e6ea;border-radius:12px;padding:.9rem;margin-bottom:.6rem}.ev b{font-size:1.2rem;color:#0B58C2}
.slots{display:grid;grid-template-columns:repeat(3,1fr);gap:.4rem;margin:.6rem 0}.slots i{font-style:normal;text-align:center;border:1px solid #cfd8e3;border-radius:10px;padding:.9rem 0;font-weight:700}.slots i.sel{background:#0B58C2;color:#fff;border-color:#0B58C2}
.cbtn{display:block;text-align:center;background:#FF7A2F;color:#10243E;font-weight:800;border-radius:12px;padding:.7rem}
.cal{border-left:5px solid #0B58C2;background:#EAF3FF;border-radius:8px;padding:1rem;margin:.6rem 0}
.toast{margin-top:.8rem;background:#10243E;color:#fff;border-radius:12px;padding:.7rem .9rem;font-weight:700}
.field{border:1px solid #cfd8e3;border-radius:10px;padding:.9rem;margin-bottom:.7rem}.field small{display:block;color:#5a6b7d}
.step{min-height:78vh;display:flex;flex-direction:column;justify-content:center;padding:1rem 0;opacity:.35;transition:opacity .3s}
.step.on{opacity:1}
.step .n{font-weight:800;color:#0B58C2;letter-spacing:.1em;text-transform:uppercase;font-size:.875rem}
.step h2{margin:.3rem 0 .6rem;font-weight:800;font-size:clamp(1.8rem,3.4vw,3.2rem);line-height:1.05;letter-spacing:-.035em}.step p{margin:0 0 .6rem;max-width:30rem}
.step .mini{display:none}
.heroblock{padding:3rem 2.5vw 0}.heroblock .kick{margin:0 0 .6rem;font-weight:800;letter-spacing:.1em;text-transform:uppercase;font-size:.875rem;color:#0B58C2}
.heroblock h1{margin:0 0 1rem;font-weight:800;font-size:clamp(2.4rem,6vw,5.6rem);line-height:1;letter-spacing:-.04em;max-width:78rem}
.heroblock .lead{font-size:1.3rem;max-width:56rem;margin:0 0 1.25rem}
.btn{display:inline-flex;align-items:center;min-height:52px;padding:0 1.5rem;border-radius:999px;background:#10243E;color:#fff;font-weight:800;text-decoration:none;margin:0 .7rem .7rem 0;border:3px solid #10243E}.btn.alt{background:transparent;color:#10243E}
.right-col .tip{position:sticky;top:7rem;background:#fff;border:2px solid var(--line);border-radius:20px;padding:1.25rem}.right-col .tip b{display:block;margin-bottom:.4rem}
.sec{display:grid;grid-template-columns:minmax(16rem,26rem) 1fr;gap:1.5rem 4vw;padding:4rem 2.5vw;border-top:1px solid var(--line)}
.sec header{position:sticky;top:5.5rem;align-self:start}
.kick{margin:0 0 .5rem;font-weight:800;letter-spacing:.1em;text-transform:uppercase;font-size:.875rem;color:#0B58C2}
.sec h2{margin:0 0 .6rem;font-weight:800;font-size:clamp(1.9rem,3.6vw,3.2rem);line-height:1.04;letter-spacing:-.035em}
.intro{margin:0 0 .5rem}
.cards{display:grid;gap:0;border-left:3px solid #10243E}
.c{position:relative;padding:.4rem 0 1.6rem 1.6rem}.c::before{content:"";position:absolute;left:-.62rem;top:.6rem;width:1.1rem;height:1.1rem;border-radius:50%;background:#FF7A2F;border:3px solid var(--paper)}
.c h3{margin:0 0 .4rem;font-weight:800;font-size:1.4rem;line-height:1.15}.c p{margin:0 0 .55rem;max-width:44rem}
.steps .no{font-weight:800;color:#0B58C2;font-size:2.2rem;line-height:1;display:block}
.cta,.note{grid-column:2}.cta .btn{margin:0 .6rem .6rem 0}.note{margin:0;color:var(--muted);font-style:italic;max-width:50rem}
.own{background:#10243E;color:#fff;border-top:0}.own .kick{color:#7DBBFF}.own .cards{border-color:#7DBBFF}.own .c::before{border-color:#10243E}.own .intro{color:#CFE0F5}
.workbox{grid-column:1/-1;background:#fff;border:2px solid var(--line);border-radius:22px;padding:1.5rem}.workbox .lede{max-width:80rem;margin:0 0 .5rem}.workbox h2{font-size:clamp(1.8rem,3.4vw,3rem)}
.sec:has(.workbox){display:block}.sec:has(.workbox) header{position:static;margin-bottom:1rem}.book{display:block}
.foot{padding:1.5rem 2.5vw 5rem;display:flex;flex-wrap:wrap;justify-content:space-between;gap:.5rem 2rem;font-size:.9375rem;color:var(--muted)}
@media (max-width:1100px){.story{display:block}.phone-col,.right-col{display:none}.step{min-height:auto;opacity:1;padding:1.5rem 0}.step .mini{display:block;margin-top:1rem}.phone.small{max-width:18rem;aspect-ratio:9/16}.sec{display:block}.sec header{position:static;margin-bottom:1rem}}
'''
    h = C['hero']
    S = [
        ('9 PM', 'Someone is looking for what you do.', 'They pull out their phone and search. A clear website with current hours is the one they tap.',
         '<div class="sb">lunch spot near me</div><div class="res me"><b>Your Business Name</b>yourbusiness.com<br><span>Open now</span> &middot; Closes 5 PM</div><div class="res dim"><b>Old directory listing</b>Hours not confirmed</div><div class="res dim"><b>Another page</b>Last updated 2019</div>'),
        ('Step 2', 'They land on a site that answers the question.', 'Hours, photos, what you offer and what is coming up, readable on any phone.',
         '<div class="mini-hero"><h4>Your Business Name</h4>Open today, 9 to 5<br><br><span class="pill">Book a visit</span><span class="pill o">Call</span></div><h4>Coming up</h4><div class="ev"><b>12</b>Open house</div><div class="ev"><b>20</b>Evening event</div>'),
        ('Step 3', 'They book in a few taps.', 'No phone tag, no waiting for a reply. They pick a time that works for them.',
         '<h4>Pick a time</h4><div>Thursday</div><div class="slots"><i>10:00</i><i>11:30</i><i class="sel">2:00</i><i>3:30</i><i>4:00</i><i>5:00</i></div><span class="cbtn">Confirm booking</span>'),
        ('Step 4', 'It lands in their calendar.', 'Bookings and events can be added to their own calendar app, so they actually show up.',
         '<h4>Thursday</h4><div class="cal"><b>2:00 PM</b><br>Visit Your Business<br>Willow Creek</div><div class="cal" style="border-color:#FF7A2F"><b>6:00 PM</b><br>Evening event</div><div class="toast">Added to your calendar</div>'),
        ('Step 5', 'And you can change anything yourself.', 'New hours, a holiday closure, a special. A few taps, and it is live. No waiting on someone else.',
         '<h4>Edit hours</h4><div class="field"><small>Thursday</small>9:00 AM to 5:00 PM</div><div class="field"><small>Friday</small>Closed for the holiday</div><span class="cbtn">Publish</span><div class="toast">Published. Your site is up to date.</div>')]
    phone = lambda cls='': '<div class="phone %s"><div class="scr"><span class="notch" aria-hidden="true"></span>%s</div></div>'
    def screens(active=None):
        return ''.join('<div class="s%s">%s</div>' % (' on' if i == 0 else '', s[3]) for i, s in enumerate(S))
    steps = ''.join('<div class="step" data-i="%d"><span class="n">%s</span><h2>%s</h2><p>%s</p><div class="mini" aria-hidden="true"><div class="phone small"><div class="scr"><span class="notch"></span><div class="s on" style="position:relative;visibility:visible;opacity:1;transform:none;height:100%%">%s</div></div></div></div></div>' % (i, s[0], s[1], s[2], s[3]) for i, s in enumerate(S))
    body = fill('''<header class="top"><a class="brand" href="#top">[[brand]]</a><nav aria-label="Main">[[nav]]</nav><a class="go" href="#book">Book a free chat</a></header>
<main id="top"><section class="heroblock"><p class="kick">[[kicker]]</p><h1>[[h1]]</h1><p class="lead">[[lead]]</p><div>[[links]]</div></section>
<section class="story" id="story"><div class="steps-col">[[steps]]</div><div class="phone-col"><div class="stick"><div class="phone" aria-hidden="true"><div class="scr"><span class="notch"></span>[[screens]]</div></div></div></div>
<div class="right-col"><div class="tip"><b>[[tipt]]</b>[[tipp]]</div></div></section>
<section class="sec" style="padding:1rem 2.5vw;background:#FF7A2F;color:#10243E;font-weight:800;display:block">[[sale]] <a href="[[salehref]]" style="color:#10243E">[[salelink]]</a></section>
[[sections]]</main><div class="foot"><span>[[f0]]</span><span>[[f1]]</span></div>''', brand=C['brand'], nav=''.join('<a href="%s">%s</a>' % x for x in C['nav']), kicker=h['kicker'], h1=h['h1'], lead=h['lead'], links=links(h['links']),
        steps=steps, screens=screens(), tipt=h['card'][0], tipp=plist(h['card'][1:]), sale=C['band']['text'], salehref=C['band']['href'], salelink=C['band']['link'], sections=all_sections(), f0=C['footer'][0], f1=C['footer'][1])
    js = '''<script>
(function(){var steps=[].slice.call(document.querySelectorAll('.step')),scr=[].slice.call(document.querySelectorAll('.phone-col .s'));
if(!('IntersectionObserver' in window)){steps.forEach(function(s){s.classList.add('on')});return}
var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){var i=+e.target.dataset.i;steps.forEach(function(s,k){s.classList.toggle('on',k===i)});scr.forEach(function(s,k){s.classList.toggle('on',k===i)})}})},{rootMargin:'-40% 0px -40% 0px'});
steps.forEach(function(s){io.observe(s)})})();
</script>'''
    return page(8, ['Manrope:wght@400;600;700;800'], css, body, js)
