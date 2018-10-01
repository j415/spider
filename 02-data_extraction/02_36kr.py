import re
import json
from parse_url import parse_url

url = "http://36kr.com/"

html_str = parse_url(url)

ret = re.findall("<script>var props=(.*?),locationnal=",html_str)[0]

with open("files/36kr.json","w",encoding="utf-8") as f:
    f.write(ret)


ret = json.loads(ret)
print(ret)