import time
import urllib

import requests
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5
import base64
username = "202****" # 教务系统账号
password = "*****" # 教务系统密码 明文

session = requests.Session()
session.get("http://jw.qlu.edu.cn/jwglxt/xtgl/login_slogin.html")
session.get("http://jw.qlu.edu.cn/jwglxt/xtgl/login_slogin.html")
getPublicKey = session.get("http://jw.qlu.edu.cn/jwglxt/xtgl/login_getPublicKey.html")
getPublicKey_json = getPublicKey.json()

# 模数和指数的Base64编码值
modulus_b64 = str(getPublicKey_json["modulus"]).replace("/","\/")

exponent_b64 = getPublicKey_json["exponent"]

# 使用Base64解码模数和指数
modulus_bytes = base64.b64decode(modulus_b64)
exponent_bytes = base64.b64decode(exponent_b64)

# 创建RSA公钥对象
rsa_key = RSA.construct((int.from_bytes(modulus_bytes, byteorder='big'), int.from_bytes(exponent_bytes, byteorder='big')))

# 使用RSA公钥加密数据

cipher = PKCS1_v1_5.new(rsa_key)
ciphertext = cipher.encrypt(password.encode())

# 将加密后的数据进行Base64编码
encrypted_password_b64 = base64.b64encode(ciphertext).decode()

data = {
    'csrftoken': '',
    'yhm': username,
    'mm': encrypted_password_b64,
    'mm':encrypted_password_b64
}
get = session.post("http://jw.qlu.edu.cn/jwglxt/xtgl/login_slogin.html",data=data)
# 此时已经成功登录 接下来测试
res = session.get("http://jw.qlu.edu.cn/jwglxt/xsxxxggl/xsgrxxwh_cxXsgrxx.html?gnmkdm=N100801&layout=default")
print(res.text)