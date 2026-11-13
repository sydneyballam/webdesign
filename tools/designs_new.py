"""Five different concepts for the studio page (not five colour schemes):
1 Gazette (broadsheet newspaper), 2 Shop Row (a street of storefronts), 3 Ledger (a spreadsheet),
4 Pinboard (a cork board of notes you can drag), 5 Terminal (a command line with a jump palette)."""
from build_studio import *

def navlinks(sep=''):
    return sep.join('<a href="%s">%s</a>' % x for x in C['nav'])

def heroink():
    return C['hero']

# =====================================================================
# 1 GAZETTE
# =====================================================================
def gazette():
    css = '''
:root{--ink:#161616;--paper:#F1EADB;--line:#161616;--muted:#4a4437;--link:#8A1C0B;--f-display:'Playfair Display',Georgia,'Times New Roman',serif;--f-body:'Source Serif 4',Georgia,serif;--r-pill:0;--r-s:0;--r-m:0;--chip-line:#161616;--chip-bg:#F1EADB;--wcard-bg:#FBF7EC;--wcard-line:#161616;--focus:#8A1C0B}
*{box-sizing:border-box}body{margin:0;background:var(--paper);color:var(--ink);font:1.125rem/1.55 var(--f-body);background-image:radial-gradient(rgba(0,0,0,.05) 1px,transparent 1.2px);background-size:5px 5px}
.pg{padding:0 2.2vw}
a{color:var(--link)}
.ears{display:flex;justify-content:space-between;gap:1rem;border-bottom:1px solid var(--ink);padding:.5rem 0;font:700 .8125rem var(--f-body);letter-spacing:.16em;text-transform:uppercase}
.mast{border-bottom:5px double var(--ink);padding:.5rem 0 1rem;display:grid;grid-template-columns:1fr auto;gap:1rem 2rem;align-items:end}
.mast h1.title{margin:0;font-family:var(--f-display);font-weight:900;font-size:clamp(2.6rem,8.4vw,9rem);line-height:.9;letter-spacing:-.03em}
.mast .tag{font:italic 1.1rem var(--f-display);max-width:16rem;border-left:3px solid var(--ink);padding-left:1rem}
.idx{display:flex;flex-wrap:wrap;gap:0 1.75rem;border-bottom:1px solid var(--ink);padding:.15rem 0}
.idx a{min-height:44px;display:inline-flex;align-items:center;color:var(--ink);font:700 .9375rem var(--f-body);letter-spacing:.06em;text-transform:uppercase;text-decoration:none}
.idx a:hover{color:var(--link);text-decoration:underline}
.front{display:grid;grid-template-columns:repeat(12,1fr);gap:2rem;padding:2rem 0 2.5rem;border-bottom:3px solid var(--ink)}
.lead-story{grid-column:1/9}
.lead-story .rub{display:inline-block;background:var(--ink);color:var(--paper);padding:.2rem .7rem;font:700 .8125rem var(--f-body);letter-spacing:.14em;text-transform:uppercase;margin-bottom:1rem}
.lead-story h2.head{margin:0 0 1.25rem;font-family:var(--f-display);font-weight:900;font-size:clamp(2.4rem,6.2vw,6.5rem);line-height:.98;letter-spacing:-.025em}
.lead-story .body{column-count:2;column-gap:2.25rem;column-rule:1px solid var(--ink);font-size:1.25rem;hyphens:auto}
.lead-story .body p{margin:0 0 1rem}.lead-story .body p:first-child::first-letter{font-family:var(--f-display);font-weight:900;font-size:5.2rem;float:left;line-height:.78;padding:.35rem .5rem 0 0}
.side{grid-column:9/13;display:flex;flex-direction:column;gap:1.5rem}
.box{border:3px solid var(--ink);padding:1.25rem;background:#FBF7EC}
.box h3{margin:0 0 .5rem;font-family:var(--f-display);font-weight:900;font-size:1.6rem;line-height:1.05}
.box p{margin:0 0 .6rem}.box p:last-child{margin:0}
.ad{border:3px dashed var(--ink);padding:1.25rem;background:#FFE9A8}
.ad b{display:block;font-family:var(--f-display);font-weight:900;font-size:2rem;line-height:1;text-transform:uppercase;margin-bottom:.5rem}
.ad a{font-weight:700;color:var(--ink)}
.btn{display:inline-flex;align-items:center;min-height:50px;padding:0 1.4rem;background:var(--ink);color:var(--paper);font:700 1rem var(--f-body);text-decoration:none;border:2px solid var(--ink);margin:0 .75rem .75rem 0}
.btn.alt{background:transparent;color:var(--ink)}.btn:hover{background:var(--link);border-color:var(--link);color:#fff}
.page{padding:2.5rem 0 3rem;border-bottom:3px solid var(--ink)}
.page .rub{display:inline-block;background:var(--ink);color:var(--paper);padding:.2rem .7rem;font:700 .8125rem var(--f-body);letter-spacing:.14em;text-transform:uppercase;margin-bottom:.75rem}
.page h2{margin:0 0 1rem;font-family:var(--f-display);font-weight:900;font-size:clamp(2rem,5vw,4.75rem);line-height:1;letter-spacing:-.02em;max-width:78rem}
.page .deck{font:italic 1.25rem var(--f-display);margin:0 0 1.5rem;column-count:2;column-gap:2.25rem}.page .deck p{margin:0 0 .5rem}
.cols{column-count:3;column-gap:2.25rem;column-rule:1px solid var(--ink)}
.cols .art{break-inside:avoid;margin:0 0 1.5rem;padding-top:.5rem;border-top:3px solid var(--ink)}
.art h3{margin:0 0 .4rem;font-family:var(--f-display);font-weight:800;font-size:1.55rem;line-height:1.1}.art p{margin:0 0 .6rem;hyphens:auto}
.ads{display:grid;grid-template-columns:repeat(auto-fill,minmax(min(100%,17rem),1fr));gap:0}
.ads .cl{border:1px solid var(--ink);margin:-1px 0 0 -1px;padding:1rem}
.cl h3{margin:0 0 .35rem;font:800 .9375rem var(--f-body);letter-spacing:.1em;text-transform:uppercase}.cl p{margin:0 0 .5rem;font-size:1.0625rem}
.steps3{display:grid;grid-template-columns:repeat(3,1fr);gap:0;border:3px solid var(--ink)}
.steps3>div{padding:1.5rem;border-right:1px solid var(--ink)}.steps3>div:last-child{border:0}
.steps3 .no{font-family:var(--f-display);font-weight:900;font-size:7rem;line-height:.8}.steps3 h3{margin:.5rem 0;font-family:var(--f-display);font-size:1.7rem}.steps3 p{margin:0}
.inv{background:var(--ink);color:var(--paper);padding:2rem 2.2vw;margin:0 -2.2vw;border-bottom:3px solid var(--ink)}
.inv .grid{display:grid;grid-template-columns:1fr 2fr;gap:2rem}.inv h2{margin:0;font-family:var(--f-display);font-weight:900;font-size:clamp(2rem,4.5vw,4rem);line-height:1}.inv p{margin:0 0 .7rem}.inv strong{color:#F2C14E}
.cta{margin-top:1.5rem}.note{font:italic 1.1rem var(--f-display);margin:1.5rem 0 0;max-width:60rem}
.foot{padding:1.5rem 0 5rem;display:flex;flex-wrap:wrap;justify-content:space-between;gap:.5rem 2rem;font-size:.9375rem}
.workwrap .lede{max-width:70rem;margin:0 0 .6rem}
.bookbox{border:3px solid var(--ink);padding:1.5rem;background:#FBF7EC}.bookbox h2{font-size:clamp(2rem,4vw,3.5rem);margin:0 0 .75rem}
@media (max-width:900px){.front{display:block}.lead-story .body,.page .deck{column-count:1}.side{margin-top:1.5rem}.cols{column-count:1}.steps3{grid-template-columns:1fr}.steps3>div{border-right:0;border-bottom:1px solid var(--ink)}.inv .grid{grid-template-columns:1fr}.mast{grid-template-columns:1fr}.ears span:nth-child(2){display:none}}
@media (min-width:901px) and (max-width:1250px){.cols{column-count:2}}
'''
    h = C['hero']
    def page_(d, inner, n=None):
        return '<section class="page" id="%s"><span class="rub">%s</span><h2>%s</h2>%s%s%s%s</section>' % (d['id'], d['kicker'], d['title'], ('<div class="deck">%s</div>' % plist(d['intro'])) if d['intro'] else '', inner,
            ('<div class="cta">%s</div>' % links(d['links'])) if d['links'] else '', ('<p class="note">%s</p>' % d['note']) if d['note'] else '')
    def arts(d): return '<div class="cols">' + ''.join('<article class="art"><h3>%s</h3>%s</article>' % (c['h3'], plist(c['paras'])) for c in d['cards']) + '</div>'
    parts = [page_(C['modernize'], arts(C['modernize'])), page_(C['events'], arts(C['events'])), page_(C['problems'], arts(C['problems']))]
    d = C['services']
    parts.append(page_(d, '<div class="ads">' + ''.join('<div class="cl"><h3>%s</h3>%s</div>' % (c['h3'], plist(c['paras'])) for c in d['cards']) + '</div>'))
    d = C['how']
    parts.append(page_(d, '<div class="steps3">' + ''.join('<div><div class="no">%s</div><h3>%s</h3>%s</div>' % (c['num'], c['h3'], plist(c['paras'])) for c in d['cards']) + '</div>'))
    parts.append(page_(C['free'], arts(C['free'])))
    parts.append(page_(C['start'], arts(C['start'])))
    o = C['own']
    parts.append('<section class="inv"><div class="grid"><div><h2>%s</h2><p style="margin-top:.75rem">%s</p></div><div class="cols" style="column-rule-color:#F1EADB">%s</div></div></section>' % (o['h2'], o['lead'], ''.join('<div class="art" style="border-color:#F1EADB">%s</div>' % ('<p>%s</p>' % p) for p in o['items'])))
    w = C['work']
    parts.append('<section class="page" id="work"><span class="rub">%s</span><h2>%s</h2>%s</section>' % (w['kicker'], w['title'], work_block()))
    parts.append(page_(C['learn'], arts(C['learn'])))
    parts.append('<section class="page" id="book"><div class="bookbox">%s</div></section>' % book_block())
    body = fill('''<div class="pg"><div class="ears"><span>Vol. 1 &middot; Willow Creek, California</span><span>Practical help. Plain English. Every question welcome.</span><span>Free first conversation</span></div>
<header class="mast"><h1 class="title">[[brand]]</h1><p class="tag">Websites, booking, events calendars and new-equipment setup, explained in plain English.</p></header>
<nav class="idx" aria-label="Main">[[nav]]</nav>
<main id="top"><section class="front"><article class="lead-story"><span class="rub">[[kicker]]</span><h2 class="head">[[h1]]</h2><div class="body"><p>[[lead]]</p>[[card]]</div><div style="margin-top:1.25rem">[[links]]</div></article>
<aside class="side"><div class="box">[[box]]</div><div class="ad"><b>[[adtext]]</b><a href="[[adhref]]">[[adlink]]</a></div></aside></section>
[[parts]]</main>
<div class="foot"><span>[[f0]]</span><span>[[f1]]</span></div></div>''', brand=C['brand'], nav=navlinks(), kicker=h['kicker'], h1=h['h1'], lead=h['lead'], card='', links=links(h['links']),
        box='<h3>%s</h3>%s' % (h['card'][0], plist(h['card'][1:])), adtext=C['band']['text'], adhref=C['band']['href'], adlink=C['band']['link'], parts='\n'.join(parts), f0=C['footer'][0], f1=C['footer'][1])
    return page(1, ['Playfair+Display:wght@700;800;900', 'Source+Serif+4:ital,wght@0,400;0,600;0,700;1,400'], css, body)

# =====================================================================
# 2 SHOP ROW
# =====================================================================
def shoprow():
    css = '''
:root{--ink:#1d1d1d;--paper:#16213a;--line:#caa66b;--muted:#e3e8f6;--link:#0B5CAD;--wlink:#0B5CAD;--f-display:'Bowlby One','Arial Black',Impact,sans-serif;--f-body:'Nunito',system-ui,sans-serif;--r-pill:999px;--r-s:10px;--r-m:12px;--chip-line:#caa66b;--chip-bg:#fff;--chip-fg:#1d1d1d;--chip-on-bg:#1d1d1d;--chip-on-fg:#fff;--wcard-bg:#fff;--wcard-line:#caa66b;--focus:#FFD54A}
*{box-sizing:border-box}body{margin:0;color:#1d1d1d;font:1.125rem/1.55 var(--f-body);background:linear-gradient(#0e1730,#26365e 40%,#3a4a73);min-height:100vh;overflow-x:clip}
.signs{display:flex;flex-wrap:wrap;gap:.6rem;padding:1rem 2vw 0}
.signs a.brand{flex:1 1 100%;color:#fff;text-decoration:none;font:400 1.1rem var(--f-display);letter-spacing:.02em}
.signs nav{display:flex;flex-wrap:wrap;gap:.6rem}
.signs nav a{min-height:44px;display:inline-flex;align-items:center;padding:0 1rem;background:#0F7B4B;color:#fff;font-weight:800;text-decoration:none;border:3px solid #fff;border-radius:6px;box-shadow:0 0 0 3px #0F7B4B,0 4px 8px rgba(0,0,0,.4)}
.signs nav a:hover{background:#0b6139}
.shop{--a:#C8452D;--b:#F7EFE0;margin:2.5rem 2vw 0;position:relative}
.awning{position:relative;height:84px;background:repeating-linear-gradient(90deg,var(--a) 0 60px,var(--b) 60px 120px);border-radius:10px 10px 0 0;box-shadow:0 6px 0 rgba(0,0,0,.18)}
.awning::after{content:"";position:absolute;left:0;right:0;top:100%;height:30px;background:radial-gradient(circle at 30px 0,var(--a) 30px,transparent 31px) 0 0/120px 30px repeat-x,radial-gradient(circle at 90px 0,var(--b) 30px,transparent 31px) 0 0/120px 30px repeat-x;filter:drop-shadow(0 4px 0 rgba(0,0,0,.18))}
.front{background:#8f3b2a;background-image:linear-gradient(rgba(0,0,0,.18) 2px,transparent 2px),linear-gradient(90deg,rgba(0,0,0,.18) 2px,transparent 2px);background-size:100% 26px,64px 26px;padding:56px 1.5rem 1.5rem;display:grid;grid-template-columns:1fr 15rem;gap:1.5rem;border-radius:0 0 8px 8px}
.board{grid-column:1/-1;justify-self:start;background:#2b1b10;color:#FFE8B3;border:6px solid #caa66b;border-radius:8px;padding:.6rem 1.25rem;box-shadow:0 4px 0 rgba(0,0,0,.35)}
.board .kick{margin:0;font-weight:900;letter-spacing:.14em;text-transform:uppercase;font-size:.8125rem;color:#FFD27A}
.board h2{margin:.1rem 0 0;font:400 clamp(1.6rem,3.4vw,3rem)/1.05 var(--f-display);letter-spacing:.01em}
.window{position:relative;background:linear-gradient(135deg,#fff8e1,#ffeab0);border:10px solid #5a3a1e;border-radius:6px;padding:1.25rem;box-shadow:inset 0 0 0 4px rgba(255,255,255,.5),0 6px 0 rgba(0,0,0,.3);overflow:hidden}
.window::before{content:"";position:absolute;inset:0;background:linear-gradient(115deg,transparent 0 40%,rgba(255,255,255,.55) 40% 46%,transparent 46% 52%,rgba(255,255,255,.4) 52% 55%,transparent 55%);pointer-events:none}
.window .intro{position:relative;margin:0 0 1rem;font-weight:700;max-width:80rem}
.items{position:relative;display:grid;grid-template-columns:repeat(auto-fill,minmax(min(100%,17rem),1fr));gap:1.25rem 1rem}
.item{background:#fff;border:2px solid #caa66b;border-radius:8px;padding:1rem;box-shadow:0 8px 0 #5a3a1e;position:relative}
.item::before{content:"";position:absolute;top:-14px;left:50%;width:2px;height:14px;background:#5a3a1e}
.item h3{margin:0 0 .4rem;font:400 1.15rem/1.2 var(--f-display)}.item p{margin:0 0 .5rem}.item p:last-child{margin:0}
.item .no{display:inline-flex;align-items:center;justify-content:center;width:2.6rem;height:2.6rem;border-radius:50%;background:var(--a);color:#fff;font:400 1.3rem var(--f-display);margin-bottom:.5rem}
.door{position:relative;align-self:end;min-height:19rem;background:linear-gradient(#6b4423,#4d2f15);border:8px solid #2b1b10;border-radius:90px 90px 0 0;padding:3.5rem .75rem 1rem;display:flex;flex-direction:column;gap:.6rem;justify-content:flex-end;box-shadow:0 6px 0 rgba(0,0,0,.35)}
.door::before{content:"OPEN";position:absolute;top:1rem;left:50%;transform:translateX(-50%);padding:.1rem .8rem;border:3px solid #ff5a6e;border-radius:6px;color:#ff8fa0;font:400 1.3rem var(--f-display);letter-spacing:.12em;text-shadow:0 0 8px #ff3b57,0 0 18px #ff3b57;box-shadow:0 0 10px #ff3b5780;background:#220a10}
.door a{display:flex;min-height:48px;align-items:center;justify-content:center;text-align:center;padding:.5rem .6rem;background:#FFD54A;color:#2b1b10;font-weight:900;text-decoration:none;border-radius:8px;line-height:1.2;border:3px solid #2b1b10}
.door a.alt{background:#fff6d6}
.walk{height:22px;background:repeating-linear-gradient(90deg,#9aa0ab 0 100px,#868c98 100px 102px);margin:0 -2vw;box-shadow:inset 0 4px 0 rgba(0,0,0,.2)}
.hero .front{grid-template-columns:1fr 15rem}
.hero h1{margin:0;font:400 clamp(2.2rem,6vw,5.6rem)/1 var(--f-display);color:#FFE8B3;text-shadow:0 4px 0 #2b1b10}
.hero .kick{margin:0 0 .5rem;font-weight:900;letter-spacing:.14em;text-transform:uppercase;font-size:.9rem;color:#FFD27A}
.hero .sign{grid-column:1;background:#2b1b10;border:6px solid #caa66b;border-radius:8px;padding:1.25rem 1.5rem;color:#fff2d0;box-shadow:0 5px 0 rgba(0,0,0,.35)}
.hero .sign .lead{font-size:1.25rem;margin:.75rem 0 1rem;max-width:60rem}
.hero .btn{display:inline-flex;align-items:center;min-height:50px;padding:0 1.4rem;background:#FFD54A;color:#2b1b10;font-weight:900;text-decoration:none;border-radius:999px;border:3px solid #fff2d0;margin:0 .6rem .6rem 0}.hero .btn.alt{background:transparent;color:#fff2d0}
.hero .window .note{position:relative;background:#FFF59D;padding:1rem 1.25rem;transform:rotate(-1.2deg);box-shadow:0 6px 12px rgba(0,0,0,.25);max-width:46rem}
.hero .window .note p{margin:0 0 .5rem}.hero .window .note p:first-child{font:400 1.3rem/1.2 var(--f-display)}
.sale{margin:1.25rem 2vw 0;background:repeating-linear-gradient(45deg,#fff 0 14px,#ffe0e0 14px 28px);border:4px solid #C8452D;border-radius:10px;padding:.8rem 1.25rem;font-weight:900;display:flex;flex-wrap:wrap;gap:.5rem 1rem;align-items:center;justify-content:space-between;color:#7a1f10}
.sale a{color:#7a1f10}
.cta2{display:flex;flex-wrap:wrap;gap:.6rem;margin-top:1rem}
.cta2 a{min-height:48px;display:inline-flex;align-items:center;padding:0 1.2rem;background:var(--a);color:#fff;font-weight:900;text-decoration:none;border-radius:999px;border:3px solid #2b1b10}
.note2{position:relative;margin:1rem 0 0;font-weight:700}
.three{position:relative;display:grid;grid-template-columns:repeat(3,1fr);gap:1.25rem}
.workshop .window,.book .window{background:#fff8e1}
.workwrap .lede{margin:0 0 .6rem}
.foot{padding:1.5rem 2vw 5rem;color:#e3e8f6;display:flex;flex-wrap:wrap;justify-content:space-between;gap:.5rem 2rem;font-size:.9375rem}
.book h2{margin:0 0 .75rem;font:400 clamp(1.8rem,3.6vw,3rem)/1.05 var(--f-display)}
@media (max-width:900px){.front,.hero .front{grid-template-columns:1fr}.door{min-height:12rem;border-radius:60px 60px 0 0}.three{grid-template-columns:1fr}.awning{height:60px}.hero .sign{grid-column:1}}
@media (prefers-reduced-motion:no-preference){.door::before{animation:flick 5s infinite}@keyframes flick{0%,92%,100%{opacity:1}94%{opacity:.5}96%{opacity:.9}98%{opacity:.4}}}
'''
    colors = [('#C8452D', '#F7EFE0'), ('#1F5FA8', '#F7EFE0'), ('#1E7B4C', '#F7EFE0'), ('#B7791F', '#FFF7E0'), ('#6B46C1', '#F7EFE0'), ('#C05621', '#FFF3E0')]
    cnt = [0]
    def shop(d, inner, door_links=None, cls=''):
        a, b = colors[cnt[0] % len(colors)]; cnt[0] += 1
        dl = door_links if door_links is not None else (d['links'] or [('#book', 'Come in: book a free chat')])
        door = ''.join('<a class="%s" href="%s">%s</a>' % ('alt' if i else '', h_, t) for i, (h_, t) in enumerate(dl))
        return '<section class="shop %s" id="%s" style="--a:%s;--b:%s"><div class="awning"></div><div class="front"><div class="board"><p class="kick">%s</p><h2>%s</h2></div><div class="window">%s%s%s</div><div class="door">%s</div></div></section>' % (
            cls, d['id'], a, b, d['kicker'], d['title'], ('<p class="intro">%s</p>' % ' '.join(d['intro'])) if d['intro'] else '', inner, ('<p class="note2">%s</p>' % d['note']) if d['note'] else '', door)
    def items(d, numbered=False):
        return '<div class="items">' + ''.join('<div class="item">%s<h3>%s</h3>%s</div>' % ('<span class="no">%s</span>' % c['num'] if numbered and c['num'] else '', c['h3'], plist(c['paras'])) for c in d['cards']) + '</div>'
    h = C['hero']
    parts = [shop(C['modernize'], items(C['modernize'])), shop(C['events'], items(C['events'])), shop(C['problems'], items(C['problems'])), shop(C['services'], items(C['services'])),
             shop(C['how'], items(C['how'], True)), shop(C['free'], items(C['free'])), shop(C['start'], items(C['start']))]
    o = C['own']
    own = {'id': 'own', 'kicker': 'Yours to keep', 'title': o['h2'], 'intro': [o['lead']], 'links': [], 'note': None}
    parts.append(shop(own, '<div class="items">' + ''.join('<div class="item">%s</div>' % ('<p>%s</p>' % p) for p in o['items']) + '</div>'))
    w = C['work']
    parts.append(shop({'id': 'work', 'kicker': w['kicker'], 'title': w['title'], 'intro': [], 'links': [], 'note': None}, work_block(), cls='workshop'))
    parts.append(shop(C['learn'], items(C['learn'])))
    b = C['book']
    parts.append('<section class="shop book" id="book" style="--a:#C8452D;--b:#F7EFE0"><div class="awning"></div><div class="front" style="grid-template-columns:1fr"><div class="window">%s</div></div></section>' % book_block())
    body = fill('''<header class="signs"><a class="brand" href="#top">[[brand]]</a><nav aria-label="Main">[[nav]]</nav></header>
<main id="top"><section class="shop hero" style="--a:#C8452D;--b:#F7EFE0"><div class="awning"></div><div class="front"><div class="sign"><p class="kick">[[kicker]]</p><h1>[[h1]]</h1><p class="lead">[[lead]]</p><div>[[links]]</div></div><div class="door"><a href="#book">Come in: book a free chat</a></div><div class="window" style="grid-column:1"><div class="note">[[card]]</div></div></div></section>
<div class="sale"><span>[[sale]]</span><a href="[[salehref]]">[[salelink]]</a></div>
[[parts]]<div class="walk"></div></main>
<div class="foot"><span>[[f0]]</span><span>[[f1]]</span></div>''', brand=C['brand'], nav=navlinks(), kicker=h['kicker'], h1=h['h1'], lead=h['lead'],
        links=''.join('<a class="btn%s" href="%s">%s</a>' % (' alt' if i else '', h_, t) for i, (h_, t) in enumerate(h['links'])), card=plist(h['card']),
        sale=C['band']['text'], salehref=C['band']['href'], salelink=C['band']['link'], parts='\n'.join(parts), f0=C['footer'][0], f1=C['footer'][1])
    return page(2, ['Bowlby+One', 'Nunito:wght@400;700;800;900'], css, body)

# =====================================================================
# 3 LEDGER
# =====================================================================
def ledger():
    css = '''
:root{--ink:#202124;--paper:#fff;--line:#d3d7dc;--muted:#4a5056;--link:#0B57D0;--f-display:'Inter',Arial,sans-serif;--f-body:'Inter',Arial,sans-serif;--r-pill:4px;--r-s:4px;--r-m:6px;--chip-line:#9aa0a6;--chip-bg:#fff;--chip-on-bg:#188038;--chip-on-fg:#fff;--wcard-line:#d3d7dc;--focus:#0B57D0}
*{box-sizing:border-box}html,body{margin:0}body{background:#fff;color:var(--ink);font:15.5px/1.5 var(--f-body)}
.app{position:sticky;top:0;z-index:30;background:#fff}
.title{display:flex;align-items:center;gap:.75rem;padding:.5rem .75rem;border-bottom:1px solid var(--line)}
.title .ico{width:26px;height:34px;background:#188038;border-radius:3px;position:relative;flex:0 0 auto}.title .ico::after{content:"";position:absolute;inset:8px 5px;background:repeating-linear-gradient(#fff 0 2px,transparent 2px 6px);opacity:.9}
.title h1{margin:0;font:600 1.125rem var(--f-display)}
.title .menus{display:flex;gap:1rem;color:#444;font-size:.875rem;margin-left:.5rem}
.title .share{margin-left:auto;display:inline-flex;align-items:center;min-height:44px;padding:0 1.25rem;border-radius:999px;background:#188038;color:#fff;font-weight:700;text-decoration:none}
.fbar{display:flex;align-items:center;border-bottom:1px solid var(--line);font-size:.875rem}
.fbar .name{width:5rem;padding:.4rem .75rem;border-right:1px solid var(--line);font-weight:600;text-align:center}
.fbar .fx{padding:.4rem .75rem;color:#188038;font-style:italic;font-weight:700}
.fbar .val{flex:1;padding:.4rem .5rem;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;color:#202124}
.cols{display:grid;grid-template-columns:3rem repeat(12,1fr);background:#f1f3f4;border-bottom:1px solid #c0c4c9;font-size:.75rem;color:#555;font-weight:600}
.cols span{padding:.15rem 0;text-align:center;border-right:1px solid #dadce0}
.sheet{counter-reset:r;padding-bottom:7rem}
.row{display:grid;grid-template-columns:3rem repeat(12,1fr);border-bottom:1px solid var(--line);min-height:2rem}
.row::before{counter-increment:r;content:counter(r);background:#f1f3f4;border-right:1px solid #c0c4c9;color:#555;font-size:.75rem;font-weight:600;display:flex;align-items:flex-start;justify-content:center;padding-top:.45rem}
.cell{padding:.45rem .7rem;border-right:1px solid var(--line);min-width:0;cursor:cell}
.cell:hover{background:#f4f9ff}
.cell.sel{outline:2px solid #188038;outline-offset:-2px;background:#f2fbf4}
.row.hdr .cell{background:#e6f4ea;font-weight:700;border-bottom:2px solid #188038}
.c-1-12{grid-column:2/14}.c-1-9{grid-column:2/11}.c-1-3{grid-column:2/5}.c-4-9{grid-column:5/11}.c-1-4{grid-column:2/6}.c-5-12{grid-column:6/14}.c-10-12{grid-column:11/14}.c-1-6{grid-column:2/8}.c-7-12{grid-column:8/14}.c-1-2{grid-column:2/4}.c-3-12{grid-column:4/14}
.big{font:800 clamp(2rem,5.4vw,5.5rem)/1 var(--f-display);letter-spacing:-.035em;padding:1.25rem .9rem}
.h2c{font:800 clamp(1.5rem,3vw,2.6rem)/1.1 var(--f-display);letter-spacing:-.02em;padding:.9rem .9rem}
.lead{font-size:1.2rem}
.kickc{font:600 .8125rem 'Roboto Mono',ui-monospace,monospace;color:#188038;letter-spacing:.04em;text-transform:uppercase}
.t{font-weight:700}.fcell{font:500 .8125rem 'Roboto Mono',ui-monospace,monospace;color:#188038}
.cell p{margin:0 0 .5rem}.cell p:last-child{margin:0}
.cmt{background:#FFF8C5;border:1px solid #e3d46b;box-shadow:2px 3px 0 rgba(0,0,0,.12)}
.hl{background:#FFF2A8;font-weight:700}
.btn{display:inline-flex;align-items:center;min-height:46px;padding:0 1.2rem;border-radius:4px;background:#188038;color:#fff;font-weight:700;text-decoration:none;margin:.25rem .6rem .25rem 0}.btn.alt{background:#fff;color:#188038;border:2px solid #188038}
.num{font:800 3.2rem/1 var(--f-display);color:#188038}
.tabs{position:fixed;left:0;right:0;bottom:0;z-index:35;display:flex;overflow-x:auto;background:#f1f3f4;border-top:1px solid #c0c4c9}
.tabs a{white-space:nowrap;min-height:44px;display:inline-flex;align-items:center;padding:0 1.1rem;color:#333;text-decoration:none;font-weight:600;font-size:.875rem;border-right:1px solid #dadce0}
.tabs a.on{background:#fff;color:#188038;box-shadow:inset 0 -3px 0 #188038}
.foot{display:flex;flex-wrap:wrap;gap:.5rem 2rem;justify-content:space-between;padding:1rem .9rem;color:#555;font-size:.875rem}
.wk{padding:1rem .9rem 1.25rem;grid-column:2/14;border-right:1px solid var(--line)}
.wk .lede{max-width:80rem;margin:0 0 .5rem}
#designPick{bottom:58px}
@media (max-width:860px){.cols{display:none}.row,.row.hdr{display:block}.row::before{display:none}.title .menus{display:none}.cell{border-right:0;border-bottom:1px solid var(--line)}.wk{border:0}.fbar .name{width:3.5rem}}
'''
    h = C['hero']
    cnt = [0]
    rows = []
    def row(cells, cls=''):
        rows.append('<div class="row %s">%s</div>' % (cls, ''.join(cells)))
    def cell(span, html, cls=''):
        return '<div class="cell c-%s %s" tabindex="0">%s</div>' % (span, cls, html)
    def section(d, key):
        row([cell('1-12', '<span class="kickc">%s</span><div class="h2c" style="padding:.25rem 0 0">%s</div>' % (d['kicker'], d['title']))], 'hdr')
        if d['intro']: row([cell('1-9', plist(d['intro']))])
    def cardrows(d, fmt='=SERVICE'):
        for k, c in enumerate(d['cards']):
            row([cell('1-3', '<span class="t">%s</span>' % c['h3']), cell('4-9', plist(c['paras'])), cell('10-12', '<span class="fcell" aria-hidden="true">%s(%d)</span>' % (fmt, k + 1))])
    def tail(d):
        if d['links']: row([cell('1-12', links(d['links']))])
        if d['note']: row([cell('1-9', '<em>%s</em>' % d['note'])])
    # hero
    row([cell('1-9', '<div class="big">%s</div>' % h['h1']), cell('10-12', '<div class="cmt" style="padding:.75rem">%s</div>' % plist(h['card']))])
    row([cell('1-9', '<p class="lead">%s</p>' % h['lead'])])
    row([cell('1-12', links(h['links']))])
    row([cell('1-9', '<span class="hl">%s</span> <a href="%s">%s</a>' % (C['band']['text'], C['band']['href'], C['band']['link']))])
    tabs = [('Home', 'top')]
    for key, nm in [('modernize', 'Modernize'), ('events', 'Events'), ('problems', 'Help with'), ('services', 'Services'), ('how', 'How it works'), ('free', 'Free site'), ('start', 'Getting started')]:
        d = C[key]; rows.append('<div id="%s"></div>' % d['id']); tabs.append((nm, d['id'])); section(d, key)
        if key == 'how':
            row([cell('1-3', '<div class="num">%s</div><div class="t">%s</div>%s' % (d['cards'][0]['num'], d['cards'][0]['h3'], plist(d['cards'][0]['paras']))), cell('4-9', '<div class="num">%s</div><div class="t">%s</div>%s' % (d['cards'][1]['num'], d['cards'][1]['h3'], plist(d['cards'][1]['paras']))), cell('10-12', '<div class="num">%s</div><div class="t">%s</div>%s' % (d['cards'][2]['num'], d['cards'][2]['h3'], plist(d['cards'][2]['paras'])))])
        else: cardrows(d, {'modernize': '=EASY', 'events': '=PUBLISH', 'problems': '=HELP', 'services': '=SERVICE', 'free': '=INCLUDED', 'start': '=STEP'}[key])
        tail(d)
    o = C['own']
    row([cell('1-12', '<span class="kickc">Yours to keep</span><div class="h2c" style="padding:.25rem 0 0">%s</div>' % o['h2'])], 'hdr')
    row([cell('1-9', '<p>%s</p>' % o['lead'])])
    row([cell('1-4', '<p>%s</p>' % o['items'][0]), cell('5-12', '<p>%s</p>' % o['items'][1])] if False else [cell('1-3', '<p>%s</p>' % o['items'][0]), cell('4-9', '<p>%s</p>' % o['items'][1]), cell('10-12', '<p>%s</p>' % o['items'][2])])
    w = C['work']; rows.append('<div id="work"></div>'); tabs.append(('Our work', 'work'))
    row([cell('1-12', '<span class="kickc">%s</span><div class="h2c" style="padding:.25rem 0 0">%s</div>' % (w['kicker'], w['title']))], 'hdr')
    rows.append('<div class="row"><div class="wk">%s</div></div>' % work_block())
    d = C['learn']; rows.append('<div id="learn"></div>'); tabs.append(('Learn', 'learn')); section(d, 'learn'); cardrows(d, '=TIP')
    rows.append('<div id="book"></div>'); tabs.append(('Book a chat', 'book'))
    rows.append('<div class="row"><div class="wk">%s</div></div>' % book_block())
    body = fill('''<div class="app"><div class="title"><span class="ico" aria-hidden="true"></span><h1>[[brand]]</h1><span class="menus" aria-hidden="true"><span>File</span><span>Edit</span><span>View</span><span>Insert</span><span>Help</span></span><a class="share" href="#book">Book a free chat</a></div>
<div class="fbar" aria-hidden="true"><span class="name" id="nm">A1</span><span class="fx">fx</span><span class="val" id="fv"></span></div>
<div class="cols" aria-hidden="true"><span></span><span>A</span><span>B</span><span>C</span><span>D</span><span>E</span><span>F</span><span>G</span><span>H</span><span>I</span><span>J</span><span>K</span><span>L</span></div></div>
<main class="sheet" id="top">[[rows]]<div class="foot"><span>[[f0]]</span><span>[[f1]]</span></div></main>
<nav class="tabs" aria-label="Main" id="tabs">[[tabs]]<a href="calendar/">Events calendar</a></nav>''', brand=C['brand'] + '.xlsx', rows='\n'.join(rows), tabs=''.join('<a href="#%s">%s</a>' % (i, n) for n, i in tabs), f0=C['footer'][0], f1=C['footer'][1])
    js = '''<script>
(function(){var cells=[].slice.call(document.querySelectorAll('.cell')),nm=document.getElementById('nm'),fv=document.getElementById('fv'),sel=null;
var rowsAll=[].slice.call(document.querySelectorAll('.row'));
var L='ABCDEFGHIJKL';
function pick(c){if(sel)sel.classList.remove('sel');sel=c;c.classList.add('sel');var r=rowsAll.indexOf(c.parentNode)+1,m=/c-(\\d+)-/.exec(c.className);var col=L[(m?+m[1]:1)-1]||'A';nm.textContent=col+r;fv.textContent=c.innerText.replace(/\\s+/g,' ').trim()}
document.addEventListener('click',function(e){var c=e.target.closest('.cell');if(c&&!e.target.closest('a,button,select'))pick(c)});
document.addEventListener('focusin',function(e){var c=e.target.closest&&e.target.closest('.cell');if(c)pick(c)});
if(cells[0])pick(cells[0]);
var tabs=[].slice.call(document.querySelectorAll('#tabs a[href^="#"]')),map={};tabs.forEach(function(a){var t=document.querySelector(a.getAttribute('href'));if(t)map[a.getAttribute('href')]=t});
if('IntersectionObserver' in window){var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting)tabs.forEach(function(a){a.classList.toggle('on',map[a.getAttribute('href')]===e.target)})})},{rootMargin:'-20% 0px -70% 0px'});Object.keys(map).forEach(function(k){io.observe(map[k])})}
})();
</script>'''
    return page(3, ['Inter:wght@400;500;600;700;800', 'Roboto+Mono:wght@500'], css, body, js)

# =====================================================================
# 4 PINBOARD
# =====================================================================
def pinboard():
    css = '''
:root{--ink:#2a2118;--paper:#B88A5C;--line:#8a6238;--muted:#fff8ea;--link:#8A2A0B;--wlink:#8A2A0B;--f-display:'Caveat','Kalam','Comic Sans MS',cursive;--f-body:'Nunito',system-ui,sans-serif;--r-pill:999px;--r-s:8px;--r-m:4px;--chip-line:#6b4a2a;--chip-bg:#fffdf6;--chip-fg:#2a2118;--chip-on-bg:#2a2118;--chip-on-fg:#fff;--wcard-bg:#fffdf6;--wcard-line:#d8c7a4;--focus:#fff}
*{box-sizing:border-box}body{margin:0;color:#2a2118;font:1.125rem/1.5 var(--f-body);background:radial-gradient(rgba(0,0,0,.14) 1px,transparent 1.6px) 0 0/13px 13px,radial-gradient(rgba(255,255,255,.12) 1px,transparent 1.6px) 6px 6px/13px 13px,#B88A5C;min-height:100vh}
.frame{margin:10px;border:14px solid #6b4423;border-radius:6px;box-shadow:inset 0 0 30px rgba(0,0,0,.35),0 0 0 3px #4d2f15;padding:1.5rem 2vw 4rem;min-height:calc(100vh - 20px)}
.tags{display:flex;flex-wrap:wrap;gap:.9rem 1.1rem;align-items:flex-start;padding:0 0 .5rem}
.tags a.brand{flex:1 1 100%;font:700 1.9rem var(--f-display);color:#fff8ea;text-decoration:none;text-shadow:0 2px 0 rgba(0,0,0,.35)}
.tag{position:relative;display:inline-flex;align-items:center;min-height:44px;padding:.35rem 1rem .35rem 1.9rem;background:#F4E3B9;color:#2a2118;font-weight:800;text-decoration:none;border-radius:6px 22px 22px 6px;box-shadow:0 4px 8px rgba(0,0,0,.3);transform:rotate(var(--r,0deg));transform-origin:20px 0}
.tag::before{content:"";position:absolute;left:.65rem;top:50%;width:11px;height:11px;margin-top:-5px;border-radius:50%;background:#B88A5C;box-shadow:inset 0 1px 2px rgba(0,0,0,.5)}
.tag::after{content:"";position:absolute;left:11px;top:-22px;width:2px;height:22px;background:#f5f0e0}
.tag:hover{transform:rotate(0)}
.board{display:grid;grid-template-columns:repeat(12,1fr);gap:1.5rem;margin-top:2.2rem;align-items:start}
.note{position:relative;background:var(--bg,#FFF1A8);padding:1.4rem 1.25rem 1.25rem;box-shadow:0 10px 16px -6px rgba(0,0,0,.45),0 1px 0 rgba(255,255,255,.4) inset;transform:rotate(var(--rot,0deg));transition:transform .15s,box-shadow .15s;touch-action:pan-y}
.note::before{content:"";position:absolute;top:-10px;left:50%;width:15px;height:15px;margin-left:-8px;border-radius:50%;background:radial-gradient(circle at 35% 30%,#ff9a8a,#c62828 60%,#7f1010);box-shadow:0 4px 5px rgba(0,0,0,.4)}
.note.drag{cursor:grabbing;box-shadow:0 20px 28px -8px rgba(0,0,0,.55);transition:none;z-index:50}
.note h3{margin:0 0 .35rem;font:700 1.75rem/1.05 var(--f-display)}.note p{margin:0 0 .55rem}.note p:last-child{margin:0}
.y{--bg:#FFF1A8}.p{--bg:#FFC9DA}.b{--bg:#BFE3FF}.g{--bg:#C9F0C0}.o{--bg:#FFD9A8}.w{--bg:#FFFDF6}.v{--bg:#E3D2FF}
.s3{grid-column:span 3}.s4{grid-column:span 4}.s5{grid-column:span 5}.s6{grid-column:span 6}.s8{grid-column:span 8}.s12{grid-column:span 12}
.poster{grid-column:span 8;padding:2rem 2rem 1.75rem;--bg:#FFFDF6}
.poster .kick{font:700 1.5rem var(--f-display);color:#8A2A0B}
.poster h1{margin:0 0 1rem;font:700 clamp(2.8rem,6.4vw,6.8rem)/.95 var(--f-display);color:#2a2118}
.poster .lead{font-size:1.3rem;max-width:60rem}
.strip{grid-column:1/-1;position:relative;justify-self:start;margin:1.2rem 0 -.3rem;padding:.5rem 1.6rem;background:#F3E6C0;box-shadow:0 4px 8px rgba(0,0,0,.3);transform:rotate(-1deg);clip-path:polygon(0 8%,2% 0,98% 6%,100% 0,100% 94%,98% 100%,2% 94%,0 100%)}
.strip .kick{display:block;font-weight:900;letter-spacing:.1em;text-transform:uppercase;font-size:.8rem;color:#8A2A0B}
.strip h2{margin:0;font:700 clamp(2rem,4.4vw,4rem)/1 var(--f-display);color:#2a2118}
.intro{grid-column:span 8;color:#fff8ea;font-weight:700;text-shadow:0 1px 2px rgba(0,0,0,.45);margin:0}
.btn{display:inline-flex;align-items:center;min-height:50px;padding:0 1.3rem;border-radius:999px;background:#2a2118;color:#fff;font-weight:800;text-decoration:none;margin:.3rem .6rem .3rem 0;border:3px solid #2a2118}.btn.alt{background:transparent;color:#2a2118}
.ctas{grid-column:1/-1}.ctas .btn{background:#fffdf6;color:#2a2118;border-color:#2a2118}
.sticker{display:inline-block;transform:rotate(-3deg);background:#fff;border:3px dashed #C8452D;padding:.4rem .9rem;font-weight:900;color:#8A2A0B}
.num{font:700 4.5rem/.8 var(--f-display);color:#8A2A0B}
.workpaper{grid-column:1/-1;background:#fffdf6;padding:1.5rem;box-shadow:0 10px 16px -6px rgba(0,0,0,.45)}
.workpaper .lede{max-width:80rem;margin:0 0 .5rem}
.noteline{grid-column:span 8;color:#fff8ea;font-weight:700;margin:0;text-shadow:0 1px 2px rgba(0,0,0,.45)}
.hint{position:fixed;left:14px;bottom:14px;z-index:55;display:flex;gap:.5rem;align-items:center;background:#2a2118;color:#fff8ea;padding:6px 8px 6px 14px;border-radius:999px;font-weight:700;font-size:.875rem}
.hint button{min-height:40px;padding:0 14px;border:0;border-radius:999px;background:#FFF1A8;color:#2a2118;font-weight:800;cursor:pointer}
.foot{margin-top:2.5rem;color:#fff8ea;display:flex;flex-wrap:wrap;justify-content:space-between;gap:.5rem 2rem;font-size:.9375rem;text-shadow:0 1px 2px rgba(0,0,0,.5)}
@media (max-width:1000px){.poster,.s8,.intro,.noteline{grid-column:span 12}.s3,.s4,.s5,.s6{grid-column:span 6}}
@media (max-width:640px){.s3,.s4,.s5,.s6{grid-column:span 12}.frame{border-width:8px;padding-left:3vw;padding-right:3vw}.hint{display:none}}
@media (prefers-reduced-motion:reduce){.note,.tag{transition:none}}
'''
    h = C['hero']
    colors = ['y', 'p', 'b', 'g', 'o', 'v', 'w']
    cnt = [0]
    def rot():
        cnt[0] += 1; return '%.1fdeg' % ([-1.6, 1.2, -.7, 1.7, -1.1, .6, 1.4][cnt[0] % 7])
    def note(inner, span='s4', col=None, extra=''):
        c = col or colors[cnt[0] % len(colors)]
        return '<div class="note %s %s %s" style="--rot:%s">%s</div>' % (span, c, extra, rot(), inner)
    def strip(d, kicker=None, title=None):
        return '<div class="strip" id="%s"><span class="kick">%s</span><h2>%s</h2></div>' % (d['id'], kicker or d['kicker'], title or d['title'])
    def notes(d, spans):
        return ''.join(note('<h3>%s</h3>%s' % (c['h3'], plist(c['paras'])), spans[k % len(spans)]) for k, c in enumerate(d['cards']))
    def extras(d):
        s = ''
        if d['intro']: s += '<p class="intro">%s</p>' % ' '.join(d['intro'])
        return s
    def tail(d):
        s = ''
        if d['links']: s += '<div class="ctas">%s</div>' % links(d['links'])
        if d['note']: s += '<p class="noteline">%s</p>' % d['note']
        return s
    parts = []
    for key, spans in [('modernize', ['s6', 's6', 's6', 's6']), ('events', ['s4']), ('problems', ['s4']), ('services', ['s4', 's4', 's4', 's6', 's6', 's4', 's8'][:7])]:
        d = C[key]; parts.append(strip(d) + extras(d) + notes(d, spans) + tail(d))
    d = C['how']
    parts.append(strip(d) + ''.join(note('<div class="num">%s</div><h3>%s</h3>%s' % (c['num'], c['h3'], plist(c['paras'])), 's4') for c in d['cards']))
    d = C['free']; parts.append(strip(d) + notes(d, ['s4']) + tail(d))
    d = C['start']; parts.append(strip(d) + notes(d, ['s4']) + tail(d))
    o = C['own']
    parts.append(strip({'id': 'own'}, 'Yours to keep', o['h2']) + '<p class="intro">%s</p>' % o['lead'] + ''.join(note('<p>%s</p>' % p, 's4') for p in o['items']))
    w = C['work']
    parts.append(strip({'id': 'work'}, w['kicker'], w['title']) + '<div class="workpaper note" style="--rot:0deg">%s</div>' % work_block())
    d = C['learn']; parts.append(strip(d) + notes(d, ['s4']))
    parts.append('<div class="strip" id="book"><span class="kick">Come say hi</span><h2>Book a free first conversation.</h2></div><div class="workpaper note" style="--rot:0deg">%s</div>' % book_block().replace('<h2>%s</h2>' % C['book']['h2'], ''))
    tags = ''.join('<a class="tag" style="--r:%.1fdeg" href="%s">%s</a>' % ([-3, 2, -1.5, 3, -2.5, 1.5, -2, 2.5][i % 8], x[0], x[1]) for i, x in enumerate(C['nav']))
    body = fill('''<div class="frame"><header class="tags"><a class="brand" href="#top">[[brand]]</a>[[tags]]</header>
<main class="board" id="top">
<div class="note poster" style="--rot:-.8deg"><div class="kick">[[kicker]]</div><h1>[[h1]]</h1><p class="lead">[[lead]]</p><div>[[links]]</div></div>
<div class="note s4 y" style="--rot:1.6deg">[[card]]</div>
<div class="note s4 p" style="--rot:-1.4deg"><span class="sticker">[[sale]]</span><p style="margin-top:.75rem"><a href="[[salehref]]" style="color:#8A2A0B;font-weight:800">[[salelink]]</a></p></div>
[[parts]]
</main><div class="foot"><span>[[f0]]</span><span>[[f1]]</span></div></div>
<div class="hint"><span>Drag the notes around</span><button type="button" id="tidy">Tidy up</button></div>''', brand=C['brand'], tags=tags, kicker=h['kicker'], h1=h['h1'], lead=h['lead'], links=links(h['links']),
        card=plist(h['card']).replace('<p>', '<h3>', 1).replace('</p>', '</h3>', 1), sale=C['band']['text'], salehref=C['band']['href'], salelink=C['band']['link'], parts='\n'.join(parts), f0=C['footer'][0], f1=C['footer'][1])
    js = '''<script>
(function(){var z=10,notes=[].slice.call(document.querySelectorAll('.note:not(.workpaper)'));
notes.forEach(function(n){var sx,sy,ox=0,oy=0,on=false;n.style.cursor='grab';
n.addEventListener('pointerdown',function(e){if(e.button||e.target.closest('a,button,input,select,textarea,summary'))return;on=true;sx=e.clientX;sy=e.clientY;n.setPointerCapture(e.pointerId);n.classList.add('drag');n.style.zIndex=++z;e.preventDefault()});
n.addEventListener('pointermove',function(e){if(!on)return;n.style.translate=(ox+e.clientX-sx)+'px '+(oy+e.clientY-sy)+'px'});
function end(e){if(!on)return;on=false;n.classList.remove('drag');ox+=e.clientX-sx;oy+=e.clientY-sy;n._o=[ox,oy]}
n.addEventListener('pointerup',end);n.addEventListener('pointercancel',end);
n._reset=function(){ox=oy=0;n.style.translate='';n.style.zIndex=''}});
document.getElementById('tidy').addEventListener('click',function(){notes.forEach(function(n){n._reset()})});
})();
</script>'''
    return page(4, ['Caveat:wght@600;700', 'Nunito:wght@400;700;800;900'], css, body, js)

# =====================================================================
# 5 TERMINAL
# =====================================================================
def terminal():
    css = '''
:root{--ink:#D6DEEB;--paper:#0A0E14;--line:#2b3a4a;--muted:#A7B3C4;--link:#82AAFF;--wlink:#0B4FC0;--f-display:'JetBrains Mono','IBM Plex Mono',ui-monospace,Menlo,monospace;--f-body:'IBM Plex Sans',system-ui,sans-serif;--r-pill:4px;--r-s:4px;--r-m:6px;--chip-line:#4a5c70;--chip-bg:#101722;--chip-fg:#D6DEEB;--chip-on-bg:#7EE787;--chip-on-fg:#04110a;--wcard-bg:#F4F7FB;--wcard-line:#2b3a4a;--focus:#FFCB6B}
*{box-sizing:border-box}html{background:#0A0E14}body{margin:0;background:#0A0E14;color:var(--ink);font:1.0625rem/1.6 var(--f-body)}
a{color:var(--link)}
.bar{position:sticky;top:0;z-index:40;display:flex;align-items:center;gap:.75rem;padding:.4rem 1.2vw;background:#0f1622;border-bottom:1px solid var(--line);font:500 .875rem var(--f-display)}
.dots{display:flex;gap:6px}.dots i{width:12px;height:12px;border-radius:50%;background:#ff5f56}.dots i:nth-child(2){background:#ffbd2e}.dots i:nth-child(3){background:#27c93f}
.bar .ttl{color:#A7B3C4;flex:1;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.bar button,.bar a.go{min-height:40px;padding:0 .9rem;border-radius:6px;border:1px solid #4a5c70;background:#101722;color:#D6DEEB;font:600 .8125rem var(--f-display);cursor:pointer;text-decoration:none;display:inline-flex;align-items:center}
.bar a.go{background:#7EE787;border-color:#7EE787;color:#04110a}
.screen{padding:0 1.2vw 6rem}
.blk{padding:2.5rem 0 1.5rem;border-bottom:1px dashed #263446;display:grid;grid-template-columns:3.5rem 1fr;gap:0 1rem}
.gut{font:500 .8125rem/1.6 var(--f-display);color:#4f6279;text-align:right;user-select:none;padding-top:.15rem}
.gut span{display:block}
.pr{margin:0 0 .75rem;font:500 .9375rem var(--f-display);color:#7EE787}.pr b{color:#FFCB6B;font-weight:500}
.blk h2{margin:0 0 .75rem;font:800 clamp(1.7rem,3.4vw,3rem)/1.08 var(--f-display);letter-spacing:-.02em;color:#fff}
.blk h2::before{content:"# ";color:#FFCB6B}
.out{color:#C3CEDC;max-width:90rem}
.out>p{margin:0 0 .8rem;max-width:80rem}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(min(100%,19rem),1fr));gap:1rem;margin-top:1.25rem}
.file{border:1px solid #2b3a4a;border-radius:8px;background:#0F1620;padding:1rem 1.1rem;transition:border-color .15s}
.file:hover{border-color:#7EE787}
.file h3{margin:0 0 .5rem;font:700 1.05rem/1.25 var(--f-display);color:#82AAFF}.file h3::before{content:"## ";color:#4f6279}
.file p{margin:0 0 .55rem;color:#C9D3E0}.file p:last-child{margin:0}
.file .no{display:block;font:800 3rem/1 var(--f-display);color:#FFCB6B;margin-bottom:.25rem}
.hero{padding:3rem 0 2rem}
.hero h1{margin:0 0 1rem;font:800 clamp(2.3rem,6.4vw,6.4rem)/1.02 var(--f-display);letter-spacing:-.035em;color:#fff}
.hero h1::after{content:"";display:inline-block;width:.5em;height:.95em;margin-left:.15em;background:#7EE787;vertical-align:-.1em}
@media (prefers-reduced-motion:no-preference){.hero h1::after{animation:blink 1.1s steps(1) infinite}@keyframes blink{50%{opacity:0}}}
.hero .lead{font-size:1.3rem;max-width:70rem;color:#E6EDF7;margin:0 0 1.25rem}
.btn{display:inline-flex;align-items:center;min-height:50px;padding:0 1.3rem;border-radius:6px;background:#7EE787;color:#04110a;font:700 .9375rem var(--f-display);text-decoration:none;margin:0 .7rem .7rem 0;border:2px solid #7EE787}.btn.alt{background:transparent;color:#7EE787}
.ask{margin:1.5rem 0 0;padding:1.25rem;border:1px solid #2b3a4a;border-radius:8px;background:#0F1620}
.ask p{margin:0 0 .75rem;font:600 1rem var(--f-display);color:#FFCB6B}
.ask .opts{display:flex;flex-wrap:wrap;gap:.6rem}
.ask button{min-height:46px;padding:0 1rem;border-radius:6px;border:1px solid #4a5c70;background:#101722;color:#D6DEEB;font:600 .9375rem var(--f-body);cursor:pointer}
.ask button:hover{border-color:#7EE787;color:#7EE787}
.card2{margin-top:1.5rem;border-left:4px solid #FFCB6B;padding:.25rem 0 .25rem 1.25rem;max-width:62rem}.card2 p{margin:0 0 .6rem}.card2 p:first-child{font:700 1.3rem/1.25 var(--f-display);color:#FFCB6B}
.flash{animation:fl 1.6s}@keyframes fl{0%,60%{box-shadow:inset 0 0 0 3px #7EE787}100%{box-shadow:inset 0 0 0 3px transparent}}
.cta{margin-top:1.25rem}.note{margin-top:1rem;color:#A7B3C4;font-style:italic;max-width:70rem}
.workwrap .lede{margin:0 0 .6rem;color:#C3CEDC}
.workwrap a{color:#82AAFF}
.blk.light .out{max-width:none}
.palette{position:fixed;inset:0;z-index:80;background:rgba(3,6,10,.72);display:none;align-items:flex-start;justify-content:flex-start;padding:10vh 1.2vw 0}
.palette.open{display:flex}
.pal{width:min(46rem,100%);background:#0F1620;border:1px solid #4a5c70;border-radius:10px;box-shadow:0 20px 50px rgba(0,0,0,.6);overflow:hidden}
.pal input{width:100%;min-height:54px;padding:0 1rem;background:#0A0E14;border:0;border-bottom:1px solid #2b3a4a;color:#fff;font:500 1.0625rem var(--f-display)}
.pal ul{list-style:none;margin:0;padding:.4rem;max-height:50vh;overflow:auto}
.pal li a{display:flex;align-items:center;min-height:44px;padding:0 .8rem;border-radius:6px;color:#D6DEEB;text-decoration:none;gap:.6rem}
.pal li a.on,.pal li a:hover{background:#17314a;color:#fff}.pal li a::before{content:"cd";font:600 .8125rem var(--f-display);color:#7EE787}
.foot{padding:1.5rem 0 3rem;color:#8d9bb0;display:flex;flex-wrap:wrap;justify-content:space-between;gap:.5rem 2rem;font:500 .875rem var(--f-display)}
@media (max-width:760px){.blk{grid-template-columns:1fr}.gut{display:none}.bar .ttl{display:none}}
'''
    h = C['hero']
    def gut(n=30): return '<div class="gut" aria-hidden="true">' + ''.join('<span>%d</span>' % i for i in range(1, n + 1)) + '</div>'
    def blk(d, cmd, inner, cls=''):
        return '<section class="blk %s" id="%s">%s<div><p class="pr">$ <b>%s</b></p><h2>%s</h2><div class="out">%s%s%s%s</div></div></section>' % (cls, d['id'], gut(), cmd, d['title'], ''.join('<p>%s</p>' % p for p in d.get('intro', [])), inner,
            ('<div class="cta">%s</div>' % links(d['links'])) if d.get('links') else '', ('<p class="note">%s</p>' % d['note']) if d.get('note') else '')
    def files(d, numbered=False):
        return '<div class="grid">' + ''.join('<div class="file">%s<h3>%s</h3>%s</div>' % ('<span class="no">%s</span>' % c['num'] if numbered and c['num'] else '', c['h3'], plist(c['paras'])) for c in d['cards']) + '</div>'
    parts = [blk(C['modernize'], 'cat modernize/README.md', files(C['modernize'])), blk(C['events'], 'cat events/README.md', files(C['events'])),
             blk(C['problems'], 'ls help/', files(C['problems'])), blk(C['services'], 'ls services/', files(C['services'])),
             blk(C['how'], 'syd --how-it-works', files(C['how'], True)), blk(C['free'], 'cat free-starter-website.md', files(C['free'])),
             blk(C['start'], 'man start-a-business', files(C['start']))]
    o = C['own']
    parts.append(blk({'id': 'own', 'title': o['h2'], 'intro': [o['lead']]}, 'cat OWNERSHIP.txt', '<div class="grid">' + ''.join('<div class="file"><p>%s</p></div>' % p for p in o['items']) + '</div>'))
    w = C['work']
    parts.append(blk({'id': 'work', 'title': w['title']}, 'ls -l work/', work_block()))
    parts.append(blk(C['learn'], 'tldr email', files(C['learn'])))
    parts.append('<section class="blk" id="book">%s<div><p class="pr">$ <b>syd book --free</b></p><div class="out">%s</div></div></section>' % (gut(), book_block().replace('<h2>', '<h2 style="margin:0 0 .75rem;font:800 clamp(1.7rem,3.4vw,3rem)/1.08 var(--f-display);color:#fff">')))
    chips = [('I need a website', '#modernize'), ('I want an events calendar', '#events'), ("I'm starting a business", '#start'), ('New computer or Wi-Fi', '#services'), ('I just have a question', '#book')]
    body = fill('''<div class="bar"><span class="dots" aria-hidden="true"><i></i><i></i><i></i></span><span class="ttl">syd@willow-creek: ~ &mdash; [[brand]]</span><button type="button" id="palBtn" aria-haspopup="dialog">Jump to&hellip; (press /)</button><a class="go" href="#book">Book a chat</a></div>
<div class="screen"><main id="top"><section class="blk hero">[[gut]]<div><p class="pr">$ <b>whoami</b></p><p class="pr" style="color:#A7B3C4">[[kicker]]</p><h1>[[h1]]</h1><p class="pr">$ <b>cat welcome.txt</b></p><p class="lead">[[lead]]</p><div>[[links]]</div>
<div class="ask" role="group" aria-label="What do you need?"><p>? What are you trying to do</p><div class="opts">[[chips]]</div></div>
<div class="card2">[[card]]</div><p class="note">[[sale]] <a href="[[salehref]]">[[salelink]]</a></p></div></section>
[[parts]]</main><div class="foot"><span>[[f0]]</span><span>[[f1]]</span></div></div>
<div class="palette" id="pal" role="dialog" aria-modal="true" aria-label="Jump to a section"><div class="pal"><input id="palIn" type="text" placeholder="Jump to… (type a section, Enter to go, Esc to close)" aria-label="Jump to"><ul id="palList"></ul></div></div>''',
        brand=C['brand'], gut=gut(22), kicker=h['kicker'], h1=h['h1'], lead=h['lead'], links=links(h['links']), chips=''.join('<button type="button" data-go="%s">%s</button>' % (u, t) for t, u in chips),
        card=plist(h['card']), sale=C['band']['text'], salehref=C['band']['href'], salelink=C['band']['link'], parts='\n'.join(parts), f0=C['footer'][0], f1=C['footer'][1])
    secs = [(n, u) for u, n in C['nav'] if u.startswith('#')] + [('Free starter website', '#free'), ('What I can do', '#services'), ('Events calendars (publish yours)', '#events'), ('Along the 299 events calendar (opens the calendar)', 'calendar/')]
    import json
    js = '''<script>
(function(){var S=%s,pal=document.getElementById('pal'),inp=document.getElementById('palIn'),list=document.getElementById('palList'),btn=document.getElementById('palBtn'),idx=0,cur=[];
function go(h){pal.classList.remove('open');if(h.charAt(0)==='#'){var t=document.querySelector(h);if(t){t.scrollIntoView({behavior:matchMedia('(prefers-reduced-motion:reduce)').matches?'auto':'smooth',block:'start'});t.classList.remove('flash');void t.offsetWidth;t.classList.add('flash');history.replaceState(null,'',h)}}else location.href=h}
function draw(){var q=inp.value.toLowerCase();cur=S.filter(function(s){return s[0].toLowerCase().indexOf(q)>-1});idx=0;list.innerHTML=cur.map(function(s,i){return '<li><a href="'+s[1]+'" data-i="'+i+'"'+(i===0?' class="on"':'')+'>'+s[0]+'</a></li>'}).join('')}
function open(){pal.classList.add('open');inp.value='';draw();inp.focus()}
function mark(){[].forEach.call(list.querySelectorAll('a'),function(a,i){a.classList.toggle('on',i===idx)})}
btn.addEventListener('click',open);inp.addEventListener('input',draw);
list.addEventListener('click',function(e){var a=e.target.closest('a');if(a){e.preventDefault();go(a.getAttribute('href'))}});
pal.addEventListener('click',function(e){if(e.target===pal)pal.classList.remove('open')});
document.addEventListener('keydown',function(e){
 if(pal.classList.contains('open')){if(e.key==='Escape'){pal.classList.remove('open');btn.focus()}else if(e.key==='ArrowDown'){idx=Math.min(idx+1,cur.length-1);mark();e.preventDefault()}else if(e.key==='ArrowUp'){idx=Math.max(idx-1,0);mark();e.preventDefault()}else if(e.key==='Enter'&&cur[idx]){go(cur[idx][1]);e.preventDefault()}return}
 if((e.key==='/'&&!/input|textarea|select/i.test(document.activeElement.tagName))||((e.ctrlKey||e.metaKey)&&e.key.toLowerCase()==='k')){e.preventDefault();open()}});
[].forEach.call(document.querySelectorAll('[data-go]'),function(b){b.addEventListener('click',function(){go(b.getAttribute('data-go'))})});
})();
</script>''' % json.dumps(secs)
    return page(5, ['JetBrains+Mono:wght@500;700;800', 'IBM+Plex+Sans:wght@400;500;600;700'], css, body, js)
