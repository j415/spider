import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36"}
#
# p = {'wd': 'python'}
#
# # url = "https://www.baidu.com/s?"
# url = "https://www.baidu.com/s"
#
# r = requests.get(url, headers=headers, params=p)
#
# print(r.status_code)
# print(r.request.url)

url = "https://www.baidu.com/s?wd={}".format("python")
# url = 'https://www.baidu.com/s?wd={"python"}'    # 也行
r = requests.get(url, headers=headers)
print(r.status_code)
print(r.request.url)
