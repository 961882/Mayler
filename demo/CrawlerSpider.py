                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             # -*- coding: utf-8 -*-
#!/usr/bin/env python
# vim: set fileencoding=utf-8
import scrapy
from scrapy.spiders import CrawlSpider, Rule, Spider
from scrapy.linkextractors.sgml import SgmlLinkExtractor
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector
#from scrapy_splash import SplashRequest
from bs4 import BeautifulSoup
from scrapy.http import Request
from crawler.items import CrawlerItem
import requests
#from crawler.middlewares.downloader import CustomDownloader
#from crawler.dbhelp.Mysql_Conn_Help import MySqlHelp


class Crawler(Spider):
    """docstring for TianYanChaSpiders."""
    name = 'falvwenshu'
    allowed_domains = ['www.ajxxgk.jcy.gov.cn']
    #通过start_urls递增
    start_urls = ['http://www.ajxxgk.jcy.gov.cn/html/zjxflws/index.html']
    #for i in range(1129642432,1129642434):
    #    start_urls.append("http://www.tianyancha.com/company/%d"%(i))
    #提取企业名称和企业ID
    base_url = 'http://www.ajxxgk.jcy.gov.cn'
    def parse(self, response): #get_company_base_info
        print '####################开始执行parse方法###################'
        item = CrawlerItem()
        selector = Selector(response)
        all_data = selector.xpath('//div[@class="crow"]')
        for div in all_data:
            fayuan = div.xpath('div[@class="ctitle"]/a/text()')[0].extract()
            qisushu_url = div.xpath('div[@class="ctitle"]/a/@href')[1].extract()
            qisushu_name = div.xpath('div[@class="ctitle"]/a/@title')[1].extract()
            qisushu_down_url = self.base_url+qisushu_url
            qisushu_num = div.xpath('div[@class="ajh"]/a/text()').extract()
            qisushu_date = div.xpath('div[@class="sj"]/span/text()').extract()
            item['fayuan'] = fayuan
            item['qisushu_name'] = qisushu_name
            item['qisushu_num'] = qisushu_num
            item['qisushu_date'] = qisushu_date
            #yield item
            #return item
            #print '详细部分开始',qisushu_down_url
            yield Request(url=qisushu_down_url, callback=self.parse_item, meta={'item':item})
            #print '详细部分结束'
        #nextLink = selector.xpath('//div[@class="pages"]/a/@href').extract()
        #print nextLink
        #if nextLink:
        #    nextLink = nextLink[0]
        #    yield Request(self.base_url + nextLink, callback=self.parse)

    def parse_item(self,response):
        print '开始执行子页面的#####'
        item = response.meta['item']
        print item
        contnents = response.xpath('//div[@class="content"]')
        for contnents_p in contnents.xpath('.//p/text()'):
            contnents_body = contnents_body + contnents_p.extract().strip()
            item['qisushu_body'] = contnents_body
            print contnents_body

        #contnents2 = response.xpath('//div[@class="content"]/p/text()')[7].extract()
        #contnents3 = response.xpath('//div[@class="content"]/p/text()')[8].extract()
        #contnents4 = response.xpath('//div[@class="content"]/p/text()')[9].extract()
        #contnents5 = response.xpath('//div[@class="content"]/p/text()')[9].extract()
        print contnents1
        print '子页面执行完成#######'
