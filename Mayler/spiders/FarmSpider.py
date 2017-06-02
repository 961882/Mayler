# -*- coding: UTF-8 -*-

import scrapy
from scrapy.spider import Spider
from scrapy.selector import Selector
from Mayler.items import MaylerItem


def changeWd(s):  # 把表中的字符串转化到中文显示
    print s
    sum = 0
    for i in s[0]:
        sum += 1
    ss2 = ''
    count = 0
    for i in range(0, sum):
        # 对 /u2014处理
        if (s[0][i] == u'\u2014'):
            continue
        ss2 += s[0][i]
    s = ss2
    print s


class FarmSpider(Spider):
    name = "farmer"  # 爬虫的名字，执行时使用
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
                                formdata={'r': "28319BF49341BAC75C9F0BA49D9DA760"},
                                cookies={'JSESSIONID': "55809BBC0510F118D76048756EE3FC2A"},
                                )]

    def parse(self, response):  # 真正的爬虫方法
        print '页面开始------------------------'

        ###页面数据调试
        print '###页面数据调试开始###'
        sel = Selector(response)
        sites = sel.xpath('//tr')
        items = []
        for site in sites:
            site = unicode(site,"UTF-8")
            item = MaylerItem()
            item['F_Name'] = site.xpath('td/div[@class="name overflow"]/text()').extract()
            item['F_Pirce'] = site.xpath('td/div[@class="price overflow"]/text()').extract()
            item['F_Tradeplace'] = site.xpath('td/div[@class="tradeplace overflow"]/text()').extract()
            item['F_TTime'] = site.xpath('td/div[@class="time overflow"]/text()').extract()
            items.append(item)
        # for i in range(len(items)):
        #     print i,items[i]
        print '###页面数据调试结束###'
        return items
        ###

        ###获取一列数据案例
        # sites = response.xpath('//div[@class="name overflow"]')
        # items = []
        # for site in sites:
        #     item = MaylerItem()
        #     temp = site.xpath('text()').extract()
        #     item['farm_Name'] = temp
        #
        #     changeWd(temp)
        #     items.append(item)
        ###

        ###判断是否可以正确输出调试
        # html = response.body # response是获取到的来自网站的返回
        # print html
        ###

        print '页面结束------------------------'