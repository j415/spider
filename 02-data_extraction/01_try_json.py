# 不可行


import json
import requests
from .parse_url import parse_url
# from pprint import pprint

# url = "https://m.douban.com/rexxar/api/v2/subject_collection/movie_showing/items?start=0&count=18&loc_id=108288"
url = "https://m.douban.com/rexxar/api/v2/subject_collection/movie_showing/items?os=ios&for_mobile=1&callback=jsonp2&start=18&count=18&loc_id=108288&_=1538313441397"

html_str = parse_url(url)

# json.loads把json字符串转化为python类型

ret1 = json.loads(html_str)

# pprint(ret1)
# print(type(ret1))


# json.dumps能够把python转化为json格式
with open("files/douban.json","w",encoding="utf-8") as f:
    f.write(json.dumps(ret1,ensure_ascii=False,indent=4))

with open("files/douban.json","r",encoding="utf-8") as f:
    ret2 = f.read()
    ret3 = json.loads(ret2)
    print(ret3)
    print(type(ret3))

# 使用json.loads提取类文件对象中的数据
with open ("files/douban.json","r",encoding="utf-8") as f:
    ret4 = json.load(f)
    print(ret4)
    print(type(ret4))

# json.dump能够把python类型放入类文件对象中
with open("files/douban1.json","w",encoding="utf-8") as f:
    json.dump(ret1,f,ensure_ascii=False,indent=4)
