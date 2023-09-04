import requests
import ddddocr
username = '20***11' # 学号
password = "ql***" # 密码

session = requests.Session()

headers = {
    'Host': 'yuyue.lib.qlu.edu.cn',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/117.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Accept-Encoding': 'gzip, deflate',
    'Connection': 'close',
    'Referer': 'http://yuyue.lib.qlu.edu.cn/home/web/seat/area/1',
    'Upgrade-Insecure-Requests': '1'
}

# 在会话中设置请求头
session.headers.update(headers)

# 初始化 DdddOcr
ocr = ddddocr.DdddOcr()

# 替换为验证码的 HTTP 链接
captcha_url = 'http://yuyue.lib.qlu.edu.cn/api.php/check'

# 下载验证码图像
response = session.get(captcha_url)
img_bytes = response.content

# 使用 DdddOcr 识别验证码
res = ocr.classification(img_bytes)

# 打印识别结果
print('识别出的验证码为：' + res)
data = {
    'username': username,
    'password': password,
    'verify': res
}
res = session.post("http://yuyue.lib.qlu.edu.cn/api.php/login",data=data)
print(res.text)