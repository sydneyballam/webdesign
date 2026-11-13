"""Builds the studio site's five designs from one set of words (harbor-source.html).
index.html = Design 1 (Harbor). studio-2.html .. studio-5.html = Designs 2 to 5.
Run: python3 tools/build_studio.py"""
import os, re
import content

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
C = content.load()
NAMES = {1: 'Gazette', 2: 'Shop Row', 3: 'Ledger', 4: 'Pinboard', 5: 'Terminal', 6: 'Glow-up', 7: 'Site Maker', 8: 'Phone Story'}
FILES = {1: 'index.html', 2: 'studio-2.html', 3: 'studio-3.html', 4: 'studio-4.html', 5: 'studio-5.html', 6: 'studio-6.html', 7: 'studio-7.html', 8: 'studio-8.html'}
N = len(FILES)
DESC = "Websites, online booking, new-equipment setup and simple systems, explained in plain English for Willow Creek small businesses. Book a free first conversation."

def fonts(*fams):
    return '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?' + '&'.join('family=' + f for f in fams) + '&display=swap" rel="stylesheet">'

def picker(n):
    files = ','.join("'%s'" % FILES[i] for i in range(1, N + 1))
    return '''<div id="designPick" role="group" aria-label="Page design"><span>Design %d of %d &middot; %s</span><button type="button" id="designNext">Shuffle design</button></div>
<script>
(function(){var F=[%s],me=%d;try{localStorage.setItem('design',me)}catch(e){}
document.getElementById('designNext').addEventListener('click',function(){var d;do{d=1+Math.floor(Math.random()*%d)}while(d===me);
try{localStorage.setItem('design',d)}catch(e){}location.href=F[d-1]+(d===1?'?design=1':'')+location.hash})})();
</script>''' % (n, N, NAMES[n], files, n, N)

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
.booking{position:relative;margin:1.5rem 0 1rem;border-radius:26px;padding:3px;background:linear-gradient(135deg,#FFC93C,#FF7AA8 45%,#7B6CFF);box-shadow:0 22px 50px rgba(21,26,60,.35);color:#E6E9FF}
.booking>*{position:relative}
.booking::before{content:"";position:absolute;inset:3px;border-radius:23px;background:#151A3C}
.bk-head{display:flex;flex-wrap:wrap;align-items:center;gap:.4rem .9rem;padding:1rem 1.4rem .4rem;font:600 .9375rem system-ui,sans-serif;color:#B4BBE8}
.bk-head b{color:#fff;font-size:1.15rem;font-weight:800}
.bk-ico{width:30px;height:30px;border-radius:9px;background:#FFC93C;position:relative;flex:0 0 auto}
.bk-ico::before{content:"";position:absolute;left:7px;right:7px;top:10px;bottom:6px;border:2px solid #151A3C;border-radius:3px}
.bk-ico::after{content:"";position:absolute;left:10px;right:10px;top:6px;height:5px;border-left:2px solid #151A3C;border-right:2px solid #151A3C}
#cal-embed{background:transparent;border-radius:23px;padding:.25rem .5rem .6rem;min-height:14rem;color:#E6E9FF}
.focus a:focus-visible,a:focus-visible,button:focus-visible,select:focus-visible,summary:focus-visible{outline:3px solid var(--focus,#1a56db);outline-offset:3px}
html{scroll-behavior:smooth}@media (prefers-reduced-motion:reduce){html{scroll-behavior:auto}}
'''

def book_block():
    b = C['book']
    return '''<h2>%s</h2><p>%s</p><p>%s</p>
<div class="booking"><div class="bk-head"><span class="bk-ico" aria-hidden="true"></span><b>Free first conversation</b><span>Pick any time that works for you</span></div><div id="cal-embed"></div></div>
<p>Calendar not showing? <a id="cal-fallback" href="%s" target="_blank" rel="noopener">Open it in a new tab</a>.</p>
<noscript><p><a href="%s">Open the booking calendar</a></p></noscript>''' % (b['h2'], b['p1'], b['p2'], b['fallback'], b['fallback'])

CAL_UI = 'Cal.ns["chat"]("ui", { theme: "dark", hideEventTypeDetails: false, layout: "month_view", cssVarsPerTheme: { dark: { "cal-bg": "#151A3C", "cal-bg-subtle": "#1F2656", "cal-bg-emphasis": "#2B3375", "cal-bg-muted": "#1A2048", "cal-text": "#E6E9FF", "cal-text-emphasis": "#FFFFFF", "cal-text-subtle": "#B4BBE8", "cal-text-muted": "#8A93CF", "cal-border": "#323B86", "cal-border-subtle": "#2A3278", "cal-border-muted": "#232A66", "cal-border-emphasis": "#FFC93C", "cal-border-booker": "#151A3C", "cal-border-booker-width": "0px", "cal-brand": "#FFC93C", "cal-brand-emphasis": "#FFD95E", "cal-brand-text": "#151A3C", "radius": "1rem" } } });'

def cal_js():
    js = C['cal_js']
    a = js.index('        Cal.ns["chat"]("ui", { theme: "light"')
    z = js.index('        Cal.ns["chat"]("inline"')
    js = js[:a] + '        ' + CAL_UI + '\n' + js[z:]
    a = js.rindex('        Cal.ns["chat"]("ui", { theme: "light"')
    z = js.index('    }\n    var box')
    js = js[:a] + js[z:]
    js = js.replace('        Cal.ns["chat"]("inline"', '        Cal.ns["chat"]("inline"')
    k = js.index('calLink: link });') + len('calLink: link });')
    js = js[:k] + '\n        ' + CAL_UI + js[k:]
    return js.replace('config: { layout: "month_view", theme: "light" }', 'config: { layout: "month_view", theme: "dark" }')

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
''' % (DESC, fonts(*fam), css, WORK_CSS, PICK_CSS, body, '', cal_js(), work_js(), picker(n) + extra_js)

def li(items): return ''.join(items)
def plist(paras): return ''.join('<p>%s</p>' % p for p in paras)
def links(ls, cls='btn', first_alt=False):
    out = []
    for i, (h, t) in enumerate(ls):
        out.append('<a class="%s%s" href="%s">%s</a>' % (cls, ' alt' if i else '', h, t))
    return ''.join(out)

def fill(t, **kw):
    for k, v in kw.items():
        t = t.replace('[[%s]]' % k, v)
    return t

if __name__ == '__main__':
    from designs_rest import REDIRECT
    import designs_new as DN
    import designs_conv as K
    outs = {1: DN.gazette(), 2: DN.shoprow(), 3: DN.ledger(), 4: DN.pinboard(), 5: DN.terminal(), 6: K.glowup(), 7: K.sitemaker(), 8: K.phonestory()}
    outs[1] = outs[1].replace('<head>\n', '<head>\n' + REDIRECT, 1)
    for n, html in outs.items():
        open(os.path.join(ROOT, FILES[n]), 'w', encoding='utf-8').write(html)
        print(FILES[n], len(html))
    # the original design stays available, outside the random rotation
    classic = open(os.path.join(ROOT, 'tools', 'harbor-source.html'), encoding='utf-8').read()
    classic = classic.replace('<head>\n', '<head>\n<link rel="canonical" href="https://sydneyballam.github.io/webdesign/">\n', 1)
    open(os.path.join(ROOT, 'classic.html'), 'w', encoding='utf-8').write(classic)
