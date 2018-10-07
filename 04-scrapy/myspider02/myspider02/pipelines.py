# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import logging

logger = logging.getLogger(__name__)


class Myspider02Pipeline(object):
    def process_item(self, item, spider):
        if spider.name == "itcast":
            # if item["come_from"] == 'itcast':
            logger.warning("-" * 10)
        return item


class Myspider02Pipeline2(object):
    def process_item(self, item, spider):
        if spider.name == "jd":
            pass
        return item
