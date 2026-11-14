"""One shared top bar so every page links to every other page.

bar(prefix, current): prefix is the path back to the site root ('' , '../').
inject(path, prefix, current): put the bar right after <body>, replacing an older copy.
Run `python3 tools/sitebar.py` to refresh the two hand-edited pages (calendar, event desk).
"""
import os, re

CSS = ('.sitebar{background:#151A3C;color:#fff;font:600 15px/1.2 system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;'
       'display:flex;flex-wrap:wrap;align-items:center;gap:2px 6px;padding:2px 10px;position:relative;z-index:50}'
       '.sitebar b{margin-right:auto;padding:10px 6px;font-weight:800}'
       '.sitebar a{color:#fff;text-decoration:none;padding:0 12px;min-height:44px;display:inline-flex;align-items:center;border-radius:8px}'
       '.sitebar a:hover,.sitebar a:focus-visible{background:rgba(255,255,255,.16);outline:2px solid #FFC93C;outline-offset:-2px}'
       '.sitebar a[aria-current]{color:#FFC93C;text-decoration:underline;text-underline-offset:5px}')

PAGES = [('', 'Small Business Studio', 'studio'), ('calendar/', 'Events calendar', 'calendar'), ('event-desk/', 'Event Desk', 'desk')]


def bar(prefix='', current=''):
    links = ''.join('<a href="%s%s"%s>%s</a>' % (prefix, href, ' aria-current="page"' if key == current else '', label)
                    for href, label, key in PAGES)
    return '<!--sitebar--><style>%s</style><nav class="sitebar" aria-label="All pages"><b>Willow Creek</b>%s</nav><!--/sitebar-->' % (CSS, links)


def inject_html(html, prefix, current):
    html = re.sub(r'<!--sitebar-->.*?<!--/sitebar-->', '', html, flags=re.S)
    return re.sub(r'(<body[^>]*>)', lambda m: m.group(1) + '\n' + bar(prefix, current), html, count=1)


def inject(path, prefix, current):
    with open(path, encoding='utf-8') as f:
        html = f.read()
    new = inject_html(html, prefix, current)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(new)


if __name__ == '__main__':
    root = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
    inject(os.path.join(root, 'calendar', 'index.html'), '../', 'calendar')
    inject(os.path.join(root, 'event-desk', 'index.html'), '../', 'desk')
