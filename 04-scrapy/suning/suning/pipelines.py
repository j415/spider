# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import re
import logging

logger = logging.getLogger(__name__)


class SuningPipeline(object):
    def process_item(self, item, spider):
        item["title"] = item["title"].split()
        # item["title"] = self.process_content(item["title"])
        item["author"] = str(item["author"])
        item["author"] = item["author"].split()
        # item["press"] = self.process_content(item["press"])
        item["press"] = str(item["press"])
        item["press"] = item["press"].split()
        # print(type(item["press"]))
        # print(item)
        logger.warning(item)
        # print(item["title"])
        # print(type(item["title"]))
        return item

    def process_content(self, content):
        content = [re.sub(r"[\r]", "", i) for i in content]
        content = [i for i in content if len(i) > 0]  # 去除列表中的空字符串
        return content
