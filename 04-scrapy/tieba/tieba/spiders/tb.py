# -*- coding: utf-8 -*-
import scrapy
import urllib


class TbSpider(scrapy.Spider):
    name = 'tb'
    allowed_domains = ['tieba.com']
    start_urls = [
        'http://tieba.baidu.com/mo/q---596A8CA33D57134A7383E14E264D8288:FG=1--1-3-0--2--wapp_1516511596154_469/m?kw=%E6%9D%8E%E6%AF%85']

    def parse(self, response):
        # 根据帖子进行分组
        div_list = response.xpath("//div[contains(@class,'i')]")
        for div in div_list:
            item = {}
            item["href"] = div.xpath("./a/@href").extract_first()
            item["title"] = div.xpath("./a/text()").extract_first()
            if item["href"] is not None:
                item["href"] = urllib.parse.urljoin(response.url, item["href"])
                yield scrapy.Request(
                    item["href"],
                    callback=self.parse_detail,
                    meta={"item": item}
                )

    def parse_detail(self,response):
        item = response.meta("item")



        # 略略略......
