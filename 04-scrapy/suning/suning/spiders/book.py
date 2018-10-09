# -*- coding: utf-8 -*-
import scrapy


class BookSpider(scrapy.Spider):
    name = 'book'
    allowed_domains = ['suning.com']
    start_urls = ['https://book.suning.com/']

    def parse(self, response):
        div_list = response.xpath("//div[@class='menu-list']/div")
        for div in div_list:
            item = {}
            item_href = {}
            item["big_classify"] = div.xpath(".//h3/a/text()").extract_first()
            item["small_classify"] = div.xpath(".//dd/a/text()").extract_first()
            item_href["small_href"] = div.xpath(".//dd/a/@href").extract()
            # print(item)
            for href in item_href["small_href"]:
                yield scrapy.Request(
                    href,
                    callback=self.parse_list,
                    meta={"item": item}
                )

    def parse_list(self, response):
        item = response.meta["item"]
        ul_list = response.xpath("//ul[@class='clearfix']/li")
        for ul in ul_list:
            item["shop"] = ul.xpath(".//p[@class='seller oh no-more ']/a/text()").extract_first()
            item["detail_href"] = ul.xpath(".//p[@class='sell-point']/a/@href").extract_first()
            item["detail_href"] = "https:" + item["detail_href"]
            # item["price"] = ul.xpath(".//p[@class='prive-tag']/em//text()")
            # print(item)
            yield scrapy.Request(
                item["detail_href"],
                callback=self.parse_detail,
                meta={"item1": item}
            )
        # 翻页
        next_url = response.xpath("//a[@id='nextPage']/@href").extract()
        next_url = "https://list.suning.com" + next_url
        next_url = str(next_url)
        if next_url is not None:
            yield scrapy.Request(
                next_url,
                callback=self.parse_list
            )

    def parse_detail(self, response):
        item = response.meta["item1"]
        item["title"] = response.xpath(
            "//div[@class='proinfo-title']/h1[@id='itemDisplayName']/text()").extract_first()
        # item["price"] = response.xpath("//span[@class='mainprice']//text()")
        item["author"] = response.xpath("//li[@class='pb-item'][1]/text()").extract_first()
        item["press"] = response.xpath("//li[@class='pb-item'][2]/text()").extract_first()
        item["publish_date"] = response.xpath("//li[@class='pb-item'][3]/span[2]/text()").extract_first()
        # print(item)
        yield item
