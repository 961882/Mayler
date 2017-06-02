# -*- coding: UTF-8 -*-

import scrapy
from scrapy.spider import Spider
from scrapy.selector import Selector
from Mayler.items import MaylerItem


class FarmSpider(Spider):
    name = "farmer2"  # 爬虫的名字，执行时使用
    allowed_domains = ["3w3n.com"]  # 允许爬取的域名，非此域名的网页不会爬取
    # start_urls = [
    #     #"http://www.3w3n.com"  # 起始url，此例只爬着一个页面
    #     "http://www.3w3n.com/showPriceDefaultList",
    # ]

    def parse(self, response):  # 真正的爬虫方法
        print '####################开始执行parse方法###################'
        item = MaylerItem()
        selector = Selector(response)
        all_data = selector.xpath('//div[@class="price_list"]')
        for div in all_data:
            farmName = div.xpath('div[@class="name overflow"]/a/text()')[0].extract()
            item['farm_Name'] = farmName

            yield scrapy.FormRequest("http://www.3w3n.com/showPriceDefaultList",
                                     #callback=self.parse_item,
                                     meta={'item': item},
                                     formdata={'r': "C9036FB4B8D862ED4DE7EDD6484739ED"},
                                     cookies={'JSESSIONID': "D4C150887A2B2039D22A97E4F0705A87"},
                                     )

        print response.body

        print '页面结束------------------------'