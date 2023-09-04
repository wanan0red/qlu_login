import re

import requests
from Crypto.Cipher import DES
import base64
username = "20****001" # sso 平台 学号
password = "*****" # sso 平台密码 明文
def des_encrypt(t, e):
    n = base64.b64decode(t)
    cipher = DES.new(n, DES.MODE_ECB)
    e = _pad(e.encode(), 8)
    encrypted = cipher.encrypt(e)
    return base64.b64encode(encrypted).decode()
def _pad(s, block_size):
    padding = block_size - (len(s) % block_size)
    return s + bytes([padding] * padding)
session = requests.Session()
resp = session.get("https://sso.qlu.edu.cn/login")
croypto_pattern = r'<p id="login-croypto">(.+?)<\/p>'
croypto = re.search(croypto_pattern, resp.text).group(1)
encrypted_password = des_encrypt(croypto, password)
execution_pattern = r'<p id="login-page-flowkey">([^<]+)</p>'
execution = re.search(execution_pattern, resp.text).group(1)


data = {
    'username': username,
    'type': 'UsernamePassword',
    '_eventId': 'submit',
    'geolocation': '',
    'execution': execution,
    'captcha_code': '',
    'croypto': croypto,
    'password': encrypted_password
}


res = session.post("https://sso.qlu.edu.cn/login",data=data)
# 此时已经成功登录 接下来访问教务系统进行测试
res1 = session.get("https://jw.qlu.edu.cn/sso/ddlogin")
print(session.get("https://jw.qlu.edu.cn/jwglxt/xsxxxggl/xsgrxxwh_cxXsgrxx.html?gnmkdm=N100801&layout=default").text)

