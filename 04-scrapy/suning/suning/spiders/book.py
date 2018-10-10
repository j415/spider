# -*- coding: utf-8 -*-
import scrapy
import re
from ..items import SuningItem
from copy import deepcopy


class BookSpider(scrapy.Spider):
    name = 'book'
    allowed_domains = ['suning.com']
    start_urls = ['https://book.suning.com/']

    def parse(self, response):
        div_list = response.xpath("//div[@class='menu-list']/div")
        for div in div_list:
            item = SuningItem()
            item_href = {}
            item["big_classify"] = div.xpath(".//h3/a/text()").extract_first()
            item["small_classify"] = div.xpath(".//dd/a/text()").extract_first()
            item_href["small_href"] = div.xpath(".//dd/a/@href").extract()
            # print(item)
            for href in item_href["small_href"]:
                yield scrapy.Request(
                    href,
                    callback=self.parse_list,
                    meta={"item": deepcopy(item)}
                )

    def parse_list(self, response):
        item = deepcopy(response.meta["item"])
        ul_list = response.xpath("//div[@id='filter-results']/ul[@class='clearfix']/li")
        for ul in ul_list:
            item["shop"] = ul.xpath(".//p[@class='seller oh no-more ']/a/text()").extract_first()
            item["detail_href"] = ul.xpath(".//p[@class='sell-point']/a/@href").extract_first()
            item["detail_href"] = "https:" + item["detail_href"]
            # item["price"] = ul.xpath(".//p[@class='prive-tag']/em//text()")
            # print(item)
            yield scrapy.Request(
                item["detail_href"],
                callback=self.parse_detail,
                meta={"item": deepcopy(item)}
            )
        # # 翻页 s = re.findall("\d+",ss)[0]
        #
        # cateid = re.findall(r"'cateid':'(.*?)'", response.body.decode())[0]
        currentPage = int(re.findall(r'param.currentPage = "(.*?)";', response.body.decode())[0])
        pageNumbers = int(re.findall(r'param.pageNumbers = "(.*?)";', response.body.decode())[0])
        if currentPage < pageNumbers:
            next_url = "https://list.suning.com/emall/showProductList.do?ci=\d{2}&pg={}&cp=1&il=0&iy=0&adNumber=0&n=1&ch=4&prune=0&sesab=ACBAAB&id=IDENTIFYING&cc=533".format(currentPage + 1)
            yield scrapy.Request(
                next_url,
                callback=self.parse_list,
                meta={"item": deepcopy(item)}
            )

        #
        # href_num = response.xpath("//span[@class='page-more']/text()").extract()
        # href_num = re.findall("\d+",href_num)[0]
        #
        # next_url = response.xpath("//a[@id='nextPage']/@href").extract()
        # next_url = "https://list.suning.com" + next_url
        # next_url = str(next_url)
        # if next_url is not None:
        #     yield scrapy.Request(
        #         next_url,
        #         callback=self.parse_list
        #    )

    def parse_detail(self, response):
        item = response.meta["item"]
        item["title"] = response.xpath(
            "//div[@class='proinfo-title']/h1[@id='itemDisplayName']/text()").extract_first()
        # item["price"] = response.xpath("//span[@class='mainprice']//text()")
        item["author"] = response.xpath("//li[@class='pb-item'][1]/text()").extract_first()
        item["press"] = response.xpath("//li[@class='pb-item'][2]/text()").extract_first()
        item["publish_date"] = response.xpath("//li[@class='pb-item'][3]/span[2]/text()").extract_first()
        # print(item)
        yield item
