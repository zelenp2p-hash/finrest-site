import re,base64,sys
TG=sys.argv[1] if len(sys.argv)>1 else '#zapis'; MAX=sys.argv[2] if len(sys.argv)>2 else '#zapis'
s=open('site/t4.html').read()
s=s.replace('{{TG}}',TG).replace('{{MAX}}',MAX)
def img(m):
    return 'data:image/png;base64,'+base64.b64encode(open(m.group(1),'rb').read()).decode()
s=re.sub(r'\{\{IMG:([^}]+)\}\}',img,s)
open('site/finrest-keisy.html','w').write(s); print(len(s))
