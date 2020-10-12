import re, sys, os
from time import sleep, ctime
import urllib

baca=''

if os.name in ['nt', 'win32']:
        os.system('cls')
else:
        os.system('clear')
print '''

  _____                       ______          _             
 |  __ \                     |  ____|        | |            
 | |__) | __ _____  ___   _  | |__ _   _  ___| | _____ _ __ 
 |  ___/ '__/ _ \ \/ / | | | |  __| | | |/ __| |/ / _ \ '__|
 | |   | | | (_) >  <| |_| | | |  | |_| | (__|   <  __/ |   
 |_|   |_|  \___/_/\_\\__, | |_|   \__,_|\___|_|\_\___|_|   
                       __/ |                                
                      |___/   By : \__FAHD__/                            
                                        

    '''
print 'Note: Most of the Proxies are being updated everyday. If none of them worked, come back and try again later.'
print '------------------------------------------------'

print '[1] Fresh Proxies'
print '[2] New Proxies'
print '[3] Random Proxies'
print '[4] Old Proxies'+'\n------------------'
pilihan = raw_input('[+] Enter your choice : ')

print '[+] Connecting...'
try:
    if pilihan=='1':
        url=urllib.urlopen('http://nntime.com/proxy-list-01.htm').read()
    elif pilihan == '2':
        url=urllib.urlopen('http://nntime.com/proxy-list-02.htm').read()
    elif pilihan=='3':
        url=urllib.urlopen('http://nntime.com/proxy-list-03.htm').read()
    elif pilihan=='4':
        url=urllib.urlopen('http://nntime.com/proxy-list-04.htm').read()
except:
    print '[*] Can not establish SSL connection!'
    sys.exit('[*] Please Check your internet and try again!')

for isi in url:
        baca+=isi    
print '[+] Connected Successfully!'
sleep(2)
print '[+] Please wait...'

print '------------------------------------------------'
print 'IPAddress\t\t\t Updated\t\t'
print '------------------------------------------------'

cari_IP = re.findall(r'td>\d+\.\d+\.\d+\.\d+<',baca)
ip=[]
for i in cari_IP:
    ip.append(i[3:-1])
cari_port = re.findall(r'value="\d*.\d*\.\d*\.\d*" onclick',baca)
port=[]
pan=[]
j=0
cari_pan = re.findall(r'":".*\)',baca)
for i in cari_pan:
    pan.append(i[3:-1])
    
for i in cari_port:
    batas = -9 - len(pan[j])/2
    port.append(i[batas:-9])
    j+=1

cari_tipe=re.findall(r'<td>\w+\W\w+</td>|<td>\w+\s</td>',baca)
tipe=[]
n=0
for i in cari_tipe:
    if i[4:-5]=='transparent proxy':
        i='transparent '
        tipe.append(i)
    else:
        tipe.append(i[4:-5])
    
cari_update = re.findall(r'GMT">.*</dfn>',baca)
update=[]
for i in cari_update:
    update.append(i[5:-6])

cari_org = re.findall(r'organization">.*</td>',baca)
org=[]
for i in cari_org:
    org.append(i[14:-5])

try:
    for rr in range(0,(len(ip)-1)):
        print ip[rr]+':'+ port[rr] + '\t\t|' + update[rr]
        sleep(2)
except KeyboardInterrupt:
    print '\n[+] User Aborted'
    sleep(1)
    sys.exit(1)

print '------------------------------------------------'
print 'Done'
print '------------------------------------------------'
