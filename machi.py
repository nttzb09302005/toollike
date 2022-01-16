import os,requests,threading
from time import sleep
from datetime import datetime
time = datetime.now()
def clr():
  if os.name == "nt":
    os.system("cls")
  else:
    os.system("clear")
clr()


print('\033[1;36m= \033[1;37m= '*20)
coki=input(f'\033[1;37m[\033[1;31m+\033[1;37m]\033[1;32m Nhập Cookie Machine-Liker: \033[1;35m')
use='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36 Edg/97.0.1072.55'
link=input(f'\033[1;37m[\033[1;31m+\033[1;37m]\033[1;32m Nhập Link Bài Viết: \033[1;35m')
print('\033[1;36m= \033[1;37m= '*20)
print("\033[1;37m[\033[1;31m1\033[1;37m] \033[1;31m=> \033[1;32mBUFF LIKE")
print("\033[1;37m[\033[1;31m2\033[1;37m] \033[1;31m=> \033[1;32mBUFF LOVE")
print("\033[1;37m[\033[1;31m3\033[1;37m] \033[1;31m=> \033[1;32mBUFF WOW")
print("\033[1;37m[\033[1;31m4\033[1;37m] \033[1;31m=> \033[1;32mBUFF HAHA")
print("\033[1;37m[\033[1;31m7\033[1;37m] \033[1;31m=> \033[1;32mBUFF BUỒN")
print("\033[1;37m[\033[1;31m8\033[1;37m] \033[1;31m=> \033[1;32mBUFF PHẪN NỘ")
print("\033[1;37m[\033[1;31m16\033[1;37m] \033[1;31m=> \033[1;32mBUFF THƯƠNG THƯƠNG")
print('\033[1;36m= \033[1;37m= '*20)
rec = input(f'\033[1;37m[\033[1;31m+\033[1;37m]\033[1;32m Nhập Cảm Xúc: \033[1;35m')
print('\033[1;36m= \033[1;37m= '*20)

headers = {
'Host': 'www.machine-liker.com',
'cache-control': 'max-age=0',
'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
'sec-ch-ua-mobile': '?1',
'save-data': 'on',
'upgrade-insecure-requests': '1',
'user-agent': use,
'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'sec-fetch-site': 'none',
'sec-fetch-mode': 'navigate',
'sec-fetch-user': '?1',
'sec-fetch-dest': 'document',
'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
'cookie': coki
}
get_id=requests.post('https://www.machine-liker.com/api/get-post-info/',headers=headers,data={'url': link}).json()
id=get_id['post']['id']
str=get_id['post']['story']
while (True):
    get_story=requests.get(f'https://www.machine-liker.com/send-reactions/?post_id={id}&story={str}',headers=headers).text
    post_id=get_story.split('<input type="hidden" name="')[1].split('" value="')[0]
    send=get_story.split('<input type="hidden" name="')[1].split('" value="')[1].split('" required')[0]
    buff=requests.post('https://www.machine-liker.com/api/send-reactions/',headers=headers,data={post_id: send,'reactions': rec,'limit': '145'}).json()
    if buff['status'] == "ok":
      sorec = buff['info']['message'].split(" ")[0]
      tong = buff['info']['total_reactions']
      print(f'\033[1;37m<> \033[1;36m{id} \033[1;37m<> \033[1;32mĐã Tăng \033[1;33m{sorec} \033[1;32mReactions \033[1;37m<> \033[1;32mTổng \033[1;33m{tong} \033[1;32mReactions')
      for i in range(605, -1, -1):
        print(
        f'\033[1;31m◈ \033[1;31m[\033[0;36m|\033[1;31m] \033[0;36mVui Lòng Đợi {i} •   ', end='\r')
        sleep(0.25)
        print(
            f'  \033[1;31m[\033[0;36m/\033[1;31m] \033[0;36mVui Lòng Đợi {i} ••    ', end='\r')
        sleep(0.25)
        print(
            f'\033[1;31m◈ \033[1;31m[\033[0;36m-\033[1;31m] \033[0;36mVui Lòng Đợi {i} •••   ', end='\r')
        sleep(0.25)
        print(
            f'  \033[1;31m[\033[0;36m\\\033[1;31m] \033[0;36mVui Lòng Đợi {i} ••••    ', end='\r')
        sleep(0.25)
    else:
        print('\033[1;31m[\033[1;33m'+datetime.now().strftime("%H:%M:%S")+'\033[1;31m] \033[1;31mTăng Reaction Thất Bại! ',end="\r")
        break