# -*- coding: utf-8 -*-
import scrapy
import re


class Github2Spider(scrapy.Spider):
    name = 'github2'
    allowed_domains = ['github.com']
    start_urls = ['https://github.com/login']

    def parse(self, response):
        yield scrapy.FormRequest.from_response(
            response,  # 自动的从response中获取form表单
            # 这个密码也是不能给你们看的
            formdata={"login": "j415", "password": "aaaaaa"},
            callback=self.after_login,
        )

    def after_login(self, response):
        with open("github2.html", "w", encoding='utf-8') as f:
            f.write(response.body.decode())
        name = re.findall("j415", response.body.decode())
        print(name)
