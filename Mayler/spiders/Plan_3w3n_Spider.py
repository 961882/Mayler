from scrapy.spider import BaseSpider

class Plan_3w3n_Spider(BaseSpider)
    name = "3w3n" #
    allowed_domains = ["3w3n.com"]
    start_urls = [
        "http://www.3w3n.com/showPriceDefaultList?r=DBF0650FC49BB3EDEA5996A5188167AC"
    ]
    #http://www.3w3n.com/showPriceDefaultList?r=DBF0650FC49BB3EDEA5996A5188167AC