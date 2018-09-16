import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"}

data = {
    "from": "zh",
    "to": "en",
    "query": "人生苦短，我用python",
    "simple_means_flag": "3",
    "sign": "289133.35420",
    "token": "feecd7a4dafa9616cb274c0bd2b36bd8"

}
post_url = "http://fanyi.baidu.com/v2transapi"

r = requests.post(post_url,data=data,headers=headers)
print(r.content.decode())