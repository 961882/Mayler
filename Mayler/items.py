# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field


class MaylerItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # chanpinxiaolei
    farm_Catgory1 = Field()
    # chanpindalei
    farm_Catgory2 = Field()
    # chanpinmingcheng
    F_Name = Field()
    # chanpinjiage
    F_Price = Field()
    # jiaoyididian
    F_Tradeplace = Field()
    # jiaoyishijian
    F_TTime = Field()

    pass
