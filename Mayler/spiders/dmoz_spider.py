# -*- coding: UTF-8 -*-

import scrapy
from scrapy.spider import Spider
from scrapy.http.request import Request


class DmozSpider(scrapy.Spider):
    name = "dmoz"  # 爬虫的名字，执行时使用
    allowed_domains = ["dmoz.org"]  # 允许爬取的域名，非此域名的网页不会爬取
    start_urls = [
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
    ]

    def parse(self, response):  # 真正的爬虫方法

        print '页面开始------------------------'
        #item = response.meta['item']
        html = response.body # response是获取到的来自网站的返回
        print html
        print '页面结束------------------------'