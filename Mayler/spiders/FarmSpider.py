# -*- coding: UTF-8 -*-

from scrapy.spider import Spider
from scrapy.selector import Selector
from scrapy.http.request import Request

#from Mayler.settings import *


class FarmSpider(Spider):
    name = "farmer"  # 爬虫的名字，执行时使用
    allowed_domains = ["3w3n.com"]  # 允许爬取的域名，非此域名的网页不会爬取
    start_urls = [
        #"http://www.3w3n.com"  # 起始url，此例只爬着一个页面
        "http://www.3w3n.com/showPriceDefaultList?r=DFE42636EA5AD2D1ABE98981EA676073"
    ]

    def start_requests(self):
        for url in self.start_urls:
            yield Request(url, cookies={'3w3n.com':'UM_distinctid=15c47d376a71f9-077f536ba6a1e6-1d3b6853-fa000-15c47d376a8211; JSESSIONID=9374C4505D8147E1DEC780B0EA421BA0; CNZZDATA3767539=cnzz_eid%3D1420715067-1495849037-%26ntime%3D1496062026'})

    def parse(self, response):  # 真正的爬虫方法
        print '页面开始------------------------'
        html = response.body  # response是获取到的来自网站的返回
        print html
        print '页面结束------------------------'

        print 'header开始------------------------'