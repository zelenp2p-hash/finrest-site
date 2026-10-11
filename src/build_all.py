import subprocess,os
subprocess.run(['python3','-I','site/build3.py','https://t.me/finrest_sup'],check=True)
from playwright.sync_api import sync_playwright
p='site/finrest-keisy.html'
with sync_playwright() as pw:
    b=pw.chromium.launch(); pg=b.new_page(viewport={'width':390,'height':844})
    errs=[]; pg.on('pageerror',lambda e: errs.append(str(e)))
    pg.goto('file://'+os.path.abspath(p)); pg.wait_for_timeout(1000)
    charts=pg.evaluate("Object.fromEntries([...document.querySelectorAll('.fig div[id]')].map(d=>[d.id,d.innerHTML]))")
    print('sw',pg.evaluate("document.documentElement.scrollWidth"),errs)
    pg.locator('#tarify').screenshot(path='site/tar.png'); pg.locator('div.top').screenshot(path='site/nav.png')
    b.close()
s=open(p).read()
for k,v in charts.items(): s=s.replace(f'<div id="{k}"></div>',f'<div id="{k}">{v}</div>',1)
open(p,'w').write(s)
open('out/finrest-keisy.html','w').write('<!doctype html>\n<html lang="ru"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'+s.replace('</style>','</style></head><body>',1)+'\n</body></html>')
print(len(charts))
