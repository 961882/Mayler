# -*- coding: UTF-8 -*-

import scrapy
from scrapy.spider import Spider
from scrapy.http.request import Request


class FarmSpider(Spider):
    name = "farmer"  # 爬虫的名字，执行时使用
    allowed_domains = ["3w3n.com"]  # 允许爬取的域名，非此域名的网页不会爬取
    start_urls = [
        #"http://www.3w3n.com"  # 起始url，此例只爬着一个页面
        "http://www.3w3n.com/showPriceDefaultList?r=E4370F75B8B401460EC7D9247020EE1E",
    ]

    headers = {
        "Host": "www.3w3n.com",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
        "Accept-Encoding": "gzip, deflate",
        "Connection": "keep-alive",
        "Referer": "http://www.3w3n.com/user/price4Day/goIndex",
        #"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
        "Cookie": "UM_distinctid=15c47d376a71f9-077f536ba6a1e6-1d3b6853-fa000-15c47d376a8211; JSESSIONID=3CEE98C5D777A8DE6058612383FE40DD; CNZZDATA3767539=cnzz_eid%3D1420715067-1495849037-%26ntime%3D1496152332"
    }

    def from_requests(self):
        for url in self.start_urls:
            yield Request(url, headers=self.headers, callback=self.parse,method="POST")

    def parse(self, response):  # 真正的爬虫方法

        print '页面开始------------------------'
        #item = response.meta['item']
        html = response.body # response是获取到的来自网站的返回
        print html
        print '页面结束------------------------'