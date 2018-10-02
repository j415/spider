# author: aspiring
# author: aspiring
import requests
from lxml import etree
import json
import threading
from queue import Queue

class QiubaiSpider:
    def __init__(self):
        self.url_temp = "https://www.qiushibaike.com/8hr/page/{}/"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"}
        self.url_queue = Queue()
        self.html_queue = Queue()
        self.content_queue = Queue()

    def get_url_list(self):
        # return [self.url_temp.format(i) for i in range(1,14)]
        for i in range(1,14):
            self.url_queue.put(self.url_temp.format(i))

    def parse_url(self):
        while True:
            url = self.url_queue.get()
            print(url)
            response = requests.get(url,headers=self.headers)
            # return response.content.decode()
            self.html_queue.put(response.content.decode())
            self.url_queue.task_done()

    def get_content_list(self): # 提取数据
        while True:
            html_str = self.html_queue.get()
            html = etree.HTML(html_str)
            div_list = html.xpath("//div[@id='content-left']/div") # 分组
            content_list = []
            for div in div_list:
                item = {}
                item["content"] = div.xpath(".//div[@class='content']/span/text()")
                item["content"] = [i.replace("\n","") for i in item["content"]]
                item["author_gender"] = div.xpath(".//div[contains(@class,'articleGender')]/@class")
                item["author_gender"] = item["author_gender"][0].split(" ")[-1].replace("Icon", "") if len(item["author_gender"])>0 else None
                item["author_age"] = div.xpath(".//div[contains(@class,'articleGender')]/text()")
                item["author_age"] = item["author_age"][0] if len(item["author_age"]) >0 else None
                item["content_img"] = div.xpath(".//div[@class='thumb']/a/img/@src")
                item["content_img"] = "https:"+item["content_img"][0] if len(item["content_img"]) >0 else None
                item["author_img"] = div.xpath(".//div[@class='author clearfix']//img/@src")
                item["author_img"] = "https:"+item["author_img"][0] if len(item["author_img"])>0 else None
                item["stats_vote"] = div.xpath(".//span[@class='stats-vote']/i/text()")
                item["stats_vote"] = item["stats_vote"][0] if len(item["stats_vote"])>0 else None
                content_list.append(item)
            # return content_list
            self.content_queue.put(content_list)
            self.html_queue.task_done()

    def save_content_list(self): # 保存
        while True:
            content_list = self.content_queue.get()
            with open("files/qiubai_queue.txt", "a", encoding="utf-8") as f:
                for content in content_list:
                    f.write(json.dumps(content, ensure_ascii=False, indent=2))
                    f.write("\n")
            print("保存成功")
            self.content_queue.task_done()



    def run(self): # 实现主要逻辑
        thread_list = []
        #1.url_list
        t_url = threading.Thread(target=self.get_url_list)
        thread_list.append(t_url)
        #2.遍历，发送请求，获取响应
        for i in range(20):
            t_parse = threading.Thread(target=self.parse_url)
            thread_list.append(t_parse)
        #3.提取数据
        for i in range(2):
            t_html = threading.Thread(target=self.get_content_list)
            thread_list.append(t_html)
        #4.保存
        t_save = threading.Thread(target=self.save_content_list)
        thread_list.append(t_save)

        for t in thread_list:
            t.setDaemon(True) # 把子线程设置为守护线程，该线程不重要 主线程结束，子线程结束
            t.start()

        for q in [self.url_queue,self.html_queue,self.content_queue]:
            q.join() # 让主线程等待阻塞，等待对列的任务完成之后再完成

        print("主线程结束")

if __name__ == '__main__':
    qiubai_spider = QiubaiSpider()
    qiubai_spider.run()