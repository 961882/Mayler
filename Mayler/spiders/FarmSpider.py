# -*- coding: UTF-8 -*-

import scrapy
from Mayler.settings import *


class FarmSpider(scrapy.spiders.Spider):
    name = "farmer"  # 爬虫的名字，执行时使用
    allowed_domains = ["3w3n.com"]  # 允许爬取的域名，非此域名的网页不会爬取
    start_urls = [
        #"http://www.3w3n.com"  # 起始url，此例只爬着一个页面
        "http://www.3w3n.com/showPriceDefaultList?r=DBF0650FC49BB3EDEA5996A5188167AC"
    ]

    def parse(self, response):  # 真正的爬虫方法
        print '页面开始------------------------'
        html = response.body  # response是获取到的来自网站的返回
        print html
        print '页面结束------------------------'

        print 'header开始------------------------'