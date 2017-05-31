# -*- coding: UTF-8 -*-

import scrapy
from scrapy.spider import Spider


class FarmSpider(Spider):
    name = "farmer2"  # 爬虫的名字，执行时使用
    allowed_domains = ["3w3n.com"]  # 允许爬取的域名，非此域名的网页不会爬取
    # start_urls = [
    #     #"http://www.3w3n.com"  # 起始url，此例只爬着一个页面
    #     "http://www.3w3n.com/showPriceDefaultList",
    # ]

    # headers = {'Host':"www.3w3n.com",
    #             'User-Agent':"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:51.0) Gecko/20100101 Firefox/51.0",
    #             'Accept':"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    #             'Cookie':"JSESSIONID=8781A8427903E4D06B80D7D7865A4160",
    #             'Accept-Language':"en-US,en;q=0.5",
    #             'Accept-Encoding':"gzip, deflate",
    #             'Connection':"keep-alive",
    #             'Upgrade-Insecure-Requests':"1"}

    def start_requests(self):
        return [scrapy.FormRequest("http://www.3w3n.com/showPriceDefaultList",
                                formdata={'r': "58ED63716FED6A913B9D247C00CBD0E6"},
                                cookies={'JSESSIONID': "314F0ED803005889DC23D80A22A20FD8"},
                                )]

    def parse(self, response):  # 真正的爬虫方法

        print '页面开始------------------------'
        #item = response.meta['item']
        html = response.body # response是获取到的来自网站的返回
        print html
        print response.headers
        print '页面结束------------------------'