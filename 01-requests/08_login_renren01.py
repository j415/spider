import requests

session = requests.session()

post_url = "http://www.renren.com/PLogin.do"
post_data = {"email": "mr_mao_hacker@163.com", "password": "alarmchime"}
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"}

# 使用session发送post请求，cookie保存在其中
session.post(post_url, data=post_data, headers=headers)

# 再使用session进行请求登陆之后才能访问的地址
post_url2 = "http://www.renren.com/327550029/profile"
r = session.get(post_url2, headers=headers)

# 保存页面
with open("files/renren.html", 'w', encoding='utf-8') as f:
    f.write(r.content.decode())
