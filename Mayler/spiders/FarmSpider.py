# -*- coding: UTF-8 -*-

import scrapy
import requests
from scrapy.spider import Spider
from scrapy.http.request import Request


class FarmSpider(Spider):
    name = "farmer"  # 爬虫的名字，执行时使用
    allowed_domains = ["3w3n.com"]  # 允许爬取的域名，非此域名的网页不会爬取
    # start_urls = [
    #     #"http://www.3w3n.com"  # 起始url，此例只爬着一个页面
    #     "http://www.3w3n.com/showPriceDefaultList",
    # ]

    headers = {'Host': "www.3w3n.com",
               'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
               'Accept': "*/*",
               'Cookie': "UM_distinctid=15c535e1aa7151-057ae2cd5b8aa3-3e6e4647-c0000-15c535e1aa895; CNZZDATA3767539=cnzz_eid%3D878788885-1496043905-http%253A%252F%252Fwww.3w3n.com%252F%26ntime%3D1496209511; JSESSIONID=24791B3A52F61ACE4FD786444D519B6C",
               'Origin': "http://www.3w3n.com",
               'Referer': "http://www.3w3n.com/user/price4Day/goIndex",
               'Accept-Language': "en-US,en;q=0.5",
               'Accept-Encoding': "gzip, deflate",
               'Connection': "keep-alive",
               'Upgrade-Insecure-Requests':"1"}

    def start_requests(self):
        return [scrapy.FormRequest("http://www.3w3n.com/showPriceDefaultList",
                                   formdata={'r': 'AF2156CCC28BAF2FA8F9D62AEAAF0D7C'},
                                   headers=self.headers,
                                   #method='GET'
                                   )]



    def parse(self, response):  # 真正的爬虫方法

        print '页面开始------------------------'
        #item = response.meta['item']
        html = response.body # response是获取到的来自网站的返回
        print html
        print response
        print '页面结束------------------------'