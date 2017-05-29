import scrapy

class FarmSpider(scrapy.spiders.Spider):
    name = "farm"  # 爬虫的名字，执行时使用
    allowed_domains = ["3w3n.com"]  # 允许爬取的域名，非此域名的网页不会爬取
    start_urls = [
        "http://www.3w3n.com"  # 起始url，此例只爬着一个页面
    ]

    def parse(self, response):  # 真正的爬虫方法
        html = response.body  # response是获取到的来自网站的返回
        # 以下四行将html存入文件
        filename = "index.html"
        file = open(filename, "w")
        file.write(html)
        file.close()