import requests
import json
import sys

# print(sys.argv)
query_thing = sys.argv[1]

headers = {
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1"}

post_data = {
    "query": query_thing,
    "from": "zh",
    "to": "en"
}

post_url = "https://fanyi.baidu.com/basetrans"

r = requests.post(post_url, data=post_data, headers=headers)

# print(r.content.decode())

dict_ret = json.loads(r.content.decode())

ret = dict_ret['trans'][0]['dst']
print("result is:", ret)
