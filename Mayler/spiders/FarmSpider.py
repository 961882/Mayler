# -*- coding: UTF-8 -*-

import scrapy
from scrapy.spider import Spider
from scrapy.http.request import Request
from scrapy.http.response import Response


class FarmSpider(Spider):
    name = "farmer"  # 爬虫的名字，执行时使用
    allowed_domains = ["3w3n.com"]  # 允许爬取的域名，非此域名的网页不会爬取
    start_urls = [
        #"http://www.3w3n.com"  # 起始url，此例只爬着一个页面
        "http://www.3w3n.com/user/price4Day/showPriceListPage?pageNo=1&typeId=2&province=%E5%AE%89%E5%BE%BD%E7%9C%81&date=2017-05-28&r=DFE42636EA5AD2D1ABE98981EA676073",
    ]

    headers = {
        "Host": "3w3n.com",
        "Accept": "*/*",
        "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
        "Accept-Encoding": "gzip, deflate",
        "Cookie": "UM_distinctid=15c47d376a71f9-077f536ba6a1e6-1d3b6853-fa000-15c47d376a8211; JSESSIONID=9374C4505D8147E1DEC780B0EA421BA0; CNZZDATA3767539=cnzz_eid%3D1420715067-1495849037-%26ntime%3D1496062026",
    }

#    def start_requests(self):
#        for url in self.start_urls:
#            yield Request(url, self.headers)

    def parse(self, response):  # 真正的爬虫方法
        print '页面开始------------------------'
        html = response.body  # response是获取到的来自网站的返回
        print html
        print '页面结束------------------------'