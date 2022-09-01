import requests
import threading
import random
import string
import schedule
import time
import subprocess
lolo = input(f'spam word:')
proxies = { 'http':'socks5://127.0.0.1:9050', 'https':'socks5://127.0.0.1:9050' }
def spam():
    cmd = r'tor.exeへのパス'
    p = subprocess.Popen(cmd, shell=False)
    code1 = ''.join([random.choice(string.ascii_letters + string.digits) for i in range(6)])
    codex = ''.join([random.choice(string.ascii_letters + string.digits) for i in range(8)])
    codex2= ''.join([random.choice(string.ascii_letters + string.digits) for i in range(17)])
    payload = {
        "userName": code1,
        "gameName": codex,
        "country":0,
        "region": 0,
        "text": lolo+codex2,
        "upfile":"(binary)",
        "Sendbtn": "書き込む"
    }
    r=requests.post("http://hacktool3ds.php.xdomain.jp/Codes/index.php",data=payload, proxies=proxies)
    print(r)
    p.kill()

schedule.every().seconds.do(spam)
while True:
    schedule.run_pending()
    time.sleep(1)
