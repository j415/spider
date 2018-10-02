# author: aspiring encoding: utf-8

import requests
import re
import json

class Qiushi:
    def __init__(self):
        self.start_url = "https://www.qiushibaike.com/text/page/{}/"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"}

    def parse_url(self, url):
        print(url)
        response = requests.get(url, headers=self.headers)

        return response.content.decode()

    def get_first_page_content_list(self, html_str):  # 提取第一页的数据
        content_list = re.findall(r"<div class=\"content\">.*?<span>(.*?)</span>", html_str, re.S)
        # content_list = re.findall(r'<div class="content">\n<span>(.*?)</span>',html_str,re.S)
        # print(content_list)
        return content_list

    def save_content_list(self, content_list):
        with open("files/qiushi.txt", "a", encoding="utf-8") as f:
            for content in content_list:
                f.write(json.dumps(content, ensure_ascii=False))
                f.write("\n")
        print("保存成功")

    def run(self):  # 实现主要逻辑
        num = 1
        while num < 11:
            # 1.start_url
            # 2.发送请求，获取响应
            html_str = self.parse_url(self.start_url.format(num))
            # 3.提取数据
            content_list = self.get_first_page_content_list(html_str)
            # 4.保存
            self.save_content_list(content_list)
            num += 1

if __name__ == '__main__':
    qiushi = Qiushi()
    qiushi.run()
