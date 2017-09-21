# -*- coding: utf-8 -*-
import scrapy


class DoubantopSpider(scrapy.Spider):
    name = 'doubantop'
    allowed_domains = ['movie.douban.com/top250']
    # start_urls = ['https://movie.douban.com/top250/']
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
    }
    def start_requests(self):
        url = 'https://movie.douban.com/top250'
        yield Request(url, headers=self.headers)

    def parse(self, response):
        pass
