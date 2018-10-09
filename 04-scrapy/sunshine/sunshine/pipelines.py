# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import re
import logging
from .settings import MONGO_HOST
from pymongo import MongoClient

# logger = logging.getLogger(__name__)


class SunshinePipeline(object):
    def open_spider(self, spider):
        # spider.hello = "world"
        client = MongoClient()
        self.collection = client["text"]["test"]
    def process_item(self, item, spider):
        # spider.setting.get("MONGO_HOST")
        item["content"] = self.process_content(item["content"])
        print(item)
        # logger.warning(item)

        self.collection.insert(dict(item))
        return item

    def process_content(self, content):
        content = [re.sub(r"\xa0|\s", "", i) for i in content]
        content = [i for i in content if len(i) > 0]  # 去除列表中的空字符串
        return content
