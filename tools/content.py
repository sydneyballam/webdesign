"""Pulls the page's words out of harbor-source.html so every design shows the same content."""
import re, os
from bs4 import BeautifulSoup
HERE = os.path.dirname(os.path.abspath(__file__))

def inner(t):
    h = ''.join(str(c) for c in t.contents).strip()
    return re.sub(r' style="[^"]*"', '', h)

def load():
    soup = BeautifulSoup(open(os.path.join(HERE, 'harbor-source.html'), encoding='utf-8').read(), 'html.parser')
    c = {}
    nav = soup.find('nav')
    c['nav'] = [(a['href'], a.get_text(strip=True)) for a in nav.find_all('a')]
    c['brand'] = soup.find('header').find('a').get_text(strip=True)
    secs = soup.find_all('section')
    def sec(i): return secs[i]
    # hero
    h = sec(0); ps = h.find_all('p'); h1 = h.find('h1')
    c['hero'] = dict(kicker=inner(ps[0]), h1=inner(h1), lead=inner(ps[1]),
                     links=[(a['href'], inner(a)) for a in h.find_all('a')],
                     card=[inner(p) for p in ps[2:]])
    b = sec(1)
    c['band'] = dict(text=inner(b.find('span')), href=b.find('a')['href'], link=inner(b.find('a')))
    def generic(s):
        box = s.find('div'); d = dict(id=s.get('id'), kicker=None, title=None, intro=[], cards=[], links=[], note=None)
        grid = None
        for ch in box.find_all(recursive=False):
            if ch.name == 'p':
                if d['title'] is None and d['kicker'] is None: d['kicker'] = inner(ch)
                elif grid is None: d['intro'].append(inner(ch))
                else: d['note'] = inner(ch)
            elif ch.name == 'h2': d['title'] = inner(ch)
            elif ch.name == 'div':
                if ch.find('a') and not ch.find('h3') and not ch.find('p'):
                    d['links'] = [(a['href'], inner(a)) for a in ch.find_all('a')]
                else:
                    grid = True
                    for card in ch.find_all(recursive=False):
                        h3 = card.find('h3')
                        num = None
                        nd = card.find('div')
                        if nd and not nd.find(['h3', 'p']): num = nd.get_text(strip=True)
                        d['cards'].append(dict(h3=inner(h3) if h3 else '', paras=[inner(p) for p in card.find_all('p')], num=num))
        return d
    for key, i in [('modernize', 2), ('events', 3), ('problems', 4), ('services', 5), ('how', 6), ('free', 7), ('start', 8), ('learn', 11)]:
        c[key] = generic(sec(i))
    o = sec(9); c['own'] = dict(h2=inner(o.find('h2')), lead=inner(o.find('h2').find_next('p')), items=[inner(p) for p in o.find_all('p')[1:]])
    w = sec(10); wp = w.find_all('p')
    c['work'] = dict(kicker=inner(wp[0]), title=inner(w.find('h2')), intro=inner(wp[1]), also=inner(wp[2]))
    bk = sec(12); bp = bk.find_all('p')
    c['book'] = dict(h2=inner(bk.find('h2')), p1=inner(bp[0]), p2=inner(bp[1]), fallback=bk.find('a', id='cal-fallback')['href'])
    f = soup.find('footer'); sp = f.find_all('span'); c['footer'] = [inner(s) for s in sp]
    scripts = re.findall(r'<script>(.*?)</script>', open(os.path.join(HERE, 'harbor-source.html'), encoding='utf-8').read(), flags=re.S)
    c['cal_js'], c['work_js'] = scripts[0], scripts[1]
    return c

if __name__ == '__main__':
    import json
    c = load()
    for k, v in c.items():
        if k.endswith('_js'): continue
        print(k, json.dumps(v)[:240])
