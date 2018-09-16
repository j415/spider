import requests
import time

proxies = {"http": "http://120.79.99.27:80"}

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"}

url = "http://www.baidu.com"
start_time = time.time()
r = requests.get(url, proxies=proxies, headers=headers)
end_time = time.time()
print(r.status_code)
print(end_time - start_time)
