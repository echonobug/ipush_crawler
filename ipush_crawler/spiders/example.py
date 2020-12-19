import scrapy


class ExampleSpider(scrapy.Spider):
    name = 'example'
    allowed_domains = ['examle.com']
    start_urls = ['http://examle.com/']

    def parse(self, response):
        pass
