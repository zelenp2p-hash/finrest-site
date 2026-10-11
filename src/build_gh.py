import base64,os,shutil,re,sys
R='/home/claude/finrest-site'
src=open('out/finrest-keisy.html').read()
os.makedirs(R+'/img',exist_ok=True)
for p in ['logo/emblem.png','logo/full.png','logo/word.png','shots/abdula_2025.png','shots/abdula_2026.png','shots/abdula_kapital.png','shots/privale.png','shots/privale_kapital.png','shots/treddy.png','shots/treddy_kapital.png']:
    b='data:image/png;base64,'+base64.b64encode(open(p,'rb').read()).decode()
    name=p.replace('/','_'); shutil.copy(p,R+'/img/'+name)
    src=src.replace(b,'img/'+name)
assert 'base64' not in src
if '<title>' not in src: src=src.replace('<head>','<head><title>ФинРест: кейсы и тарифы</title>',1)
if 'name="description"' not in src:
    src=src.replace('<meta charset="utf-8">','<meta charset="utf-8"><meta name="description" content="Управленческий учёт и калькуляция ресторанов в iiko. Кейсы клиентов, тарифы, бесплатный разбор."><meta property="og:title" content="ФинРест: каждая цифра вашего ресторана станет понятной"><meta property="og:description" content="Кейсы клиентов, тарифы и бесплатный разбор ваших цифр.">',1)
open(R+'/index.html','w').write(src)
open(R+'/CNAME','w').write('keisy.finrest.ru\n')
open(R+'/.nojekyll','w').write('')
# sources for future edits
os.makedirs(R+'/src',exist_ok=True)
for f in ['site/t4.html','site/build3.py','site/build_all.py','site/build_gh.py']: shutil.copy(f,R+'/src/'+os.path.basename(f))
print(len(src))
