# -*- coding: utf-8 -*-
import scrapy
import re


class RenrenSpider(scrapy.Spider):
    name = 'renren'
    allowed_domains = ['renren.com']
    start_urls = ['http://www.renren.com/968307410/profile']

    def start_requests(self):
        cookies = "anonymid=jmwpy2cn4vx90f; _r01_=1; depovince=SD; JSESSIONID=abccnDu08G0UQcMfy_Bzw; ick_login=c8aa0d7a-acef-4860-aff1-8ab03516e979; ick=f6cf0466-e44b-4987-a200-8d6bd2747416; _de=C3F99B2B3FB663153A088E0059DB1D4F6DEBB8C2103DE356; t=1cede67170541d39c22751f7f773e8120; societyguester=1cede67170541d39c22751f7f773e8120; id=968307410; xnsid=a368ecb4; XNESSESSIONID=d66c56a49771; jebecookies=4578b8ac-d333-49ac-b2fb-950533cae17a|||||; ver=7.0; loginfrom=null; wp_fold=0"
        cookies = {i.split("=")[0]: i.split("=")[1] for i in cookies.split(";")}
        yield scrapy.Request(
            self.start_urls[0],
            callback=self.parse,
            cookies=cookies
        )

    def parse(self, response):
        print(re.findall("蒋华超", response.body.decode()))
        yield scrapy.Request(
            "http://www.renren.com/968307410/profile?v=info_timeline",
            callback=self.parse_detail
        )

    def parse_detail(self,response):
        print(re.findall("蒋华超", response.body.decode()))
