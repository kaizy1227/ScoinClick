import replace
import requests
import time
import random

from bs4 import BeautifulSoup
import os


proxies = {
    'https': 'http://user22084:YzSDQ@sinv6v2.proxyapp.vn:22084' 
# sinv6v2.proxyapp.vn:22084:user22084:YzSDQ



}


head1 = {
    #email: khoi taikhoan01@qa.team P1090849206 gN9k5LbU 280612
    'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'cookie': '__cf_bm=h_Dyveex6Y4GKg99kVrwd2zQ9kNQZ4c9Fe6dgnttpfQ-1676694756-0-Ab0JyMTl40feWmK/hKNxbyYOKOtIc8UW98ZOfci1SDYUVpFiyy14TUhAtwzlZxgquAj4Les72pVRQDtklv32fnL6IbDF2aloYeiKoaCRO6d6b6MLqigE/g4QmYCCfymI1hW6FI8hoNOn3o8vdKgMlfI=;remember_web_59ba36addc2b2f9401580f014c7f58ea4e30989d=eyJpdiI6Iit0czgrbU84ZGNuaG0wZHR5ZURGd1E9PSIsInZhbHVlIjoiQUMvSWlCZWlSSTEyQWh2RHkvTjlDUEtWV3dmZGt6UCtMbWpKZDlYM1dhWEE0TnpGaE9JUG0rd3htK0Q5SjZZWU15OUlCVEQ1anoxUXhyOG9hamZtS0o1ZlNFaGtYUWxicEl4QXY0NlpHVGs5ZGpsYmx6eTFuN3BUM3NvMXhhcVZKVnR1UEdLYlZmbkVCb0FKczQ2TUl1TXg5K1Y3V1VlazhkamFXOWxiZHlYYTZxc25yNkc1STdBZjZHU0RpeDJUbldyUjUzWTFzc1RwYXFlNEJEUlAvTVpZVm9xVjl2a1E5MGxpTXlqNnZSYz0iLCJtYWMiOiJhZmY0Y2YwNDljNmZkN2JkN2ZiZjA1OGM1MWYzMTUwZjE5YmViMTg3YTk1NWNmOTAxOTgzN2VjNjY3OTk2NTA1IiwidGFnIjoiIn0%3D;XSRF-TOKEN=eyJpdiI6IjZ0ejJVa3JkcVdCYXZoVHhhRzc2YVE9PSIsInZhbHVlIjoiMkJ3aEZva1BjSGlqS1VnOXduUHZwMEFHRjExU1pXbGFFQTZjY1V6am9tNWs3SGpaTWZkNXU5RmszUnVaVVUyV2VNL2FtblQ3d2Q3QkkyM0N6WGJoVlNSSlNMYUVrMDZadTdPMk5NUDRIMWMySUlrck83Vi9xY2pwWVJIcmRSM2oiLCJtYWMiOiJhZTUyNTYzYWY3MTNiODI3NzkzNGVlYzdkNmYxOTJhMDhkODM4NTgzYmM4MWQyOTA3MzM0OTk4ZDMzNmIyMjVhIiwidGFnIjoiIn0%3D;scoinclick_session=eyJpdiI6IjFOR2ZvOWFtYnhiNk5qdm13bm9BdlE9PSIsInZhbHVlIjoiSVYxa3lVRlNTamUxVmFGL01XSS9ueGpxVGZjbHBDZnBWM0xYWmE5MDR5d1Zjd3VVdjZhOEQ1QkhXUVVqb2RQTEJOSlNOazVSK1Z4L3R1aXRyOVZPRGJQMWtzbXA2NERzNDBIQlNvd1Y2dWZCdXF6dGJKMnpNSjltWjBYMERzemwiLCJtYWMiOiI2NzFiMzgzMmI5Y2Y2ODFmYmM1MTVkMWM5YWU0NzRlYTgxMjExNWQ5ZGI4YmE5YzEyMTBhZjQ1OTA0MmEwNGM2IiwidGFnIjoiIn0%3D;_ga_DKC8W2J300=GS1.1.1676694849.1.0.1676694849.0.0.0;_ga=GA1.2.90260558.1676694850;_gid=GA1.2.1781786347.1676694850;|Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5345.1 Safari/537.36',
    'referer': 'https://scoin.click/earn-view',
    'sec-ch-ua': '".Not/A)Brand";v="99", "Chromium";v="108", "Google Chrome";v="108"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5345.1 Safari/537.36'
}



def diem():
    url = "https://scoin.click/home"

    response = requests.get(url, headers=head1, proxies=proxies)
    soup = BeautifulSoup(response.content.decode("utf-8"), "html.parser")
    earning = soup.find("div", {"id": "main-wrapper"}
                        ).find_all("div")[27].div.div.h3.string

    return earning


def gettask():
    url = "https://scoin.click/getTask"

    id = requests.get(url, headers=head1, proxies=proxies)
    id = id.json()
    id = id['data']
    id = id['id']

    return id


def stoptask(id):
    url = "https://scoin.click/endTask/"+str(id)+"/1"

    id = requests.get(url, headers=head1, proxies=proxies)

def checkip():
    url = 'https://icanhazip.com/'

    response = requests.post(url, proxies=proxies)
    response = response.text
    response = response.replace('\n', '')
    return response

def ipp():
    url = 'https://icanhazip.com/'

    response = requests.post(url, proxies=proxies)
    response = response.text
    response = response.replace('\n', '')
    return response
    
def lay_token():
    response = requests.get(url, headers=head1, proxies=proxies)
    soup = BeautifulSoup(response.content.decode("utf-8"), "html.parser")
    token = soup.find_all("input", {"name": "_token"})[0].get('value')
    return token
    
def rut_tien():
    
    url = "https://scoin.click/home"

    response = requests.get(url, headers=head1, proxies=proxies)
    soup = BeautifulSoup(response.content.decode("utf-8"), "html.parser")
    token = soup.find_all("input", {"name": "_token"})[0].get('value')
    
    print(token)
    
    files1 = {
    '_token': token,
    'Method': 'payeer',
    'Wallet': 'P1084263762',
    'Sum': str(diem()),
    'type': '1'
    }
    
    urlRutTien = 'https://scoin.click/withdrawal'
    response1 = requests.post(urlRutTien,headers=head1, proxies=proxies, data = files1)
    return response1



print('ip may')
#print(checkip())
absolute_path = os.path.abspath(__file__)
print("Full path: " + absolute_path)


x=0
while True:
 try:
    if str(checkip()).find(":") != 4:
        print("Proxy die")
        break
    else:
        print("Full path: " + absolute_path)
        print(x)
        if x % 10 == 0:
            if(printtitle() == "scoin.click | is the best traffic exchange platform for Website owners and Youtube blogers!"):
                print(diem())
                telegram_bot_sendtext("Tài khoản "+absolute_path+ ' Có số điểm là: '+ diem())
                time.sleep(random.randint(1, 10))
            else:
                break
        x+=1
        print('----------------')
        stt = gettask()
        time.sleep(random.randint(100, 110))
        stoptask(stt)
 except:
    pass
 
 def printtitle():
    url = "https://scoin.click/"
    response = requests.get(url, proxies=proxies)
    soup = BeautifulSoup(response.content.decode("utf-8"), "html.parser")
    title = soup.find('title')
    title = title.get_text()
    return title