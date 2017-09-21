# -*- coding: utf-8 -*-
import scrapy


class DoubantopSpider(scrapy.Spider):
    name = 'doubantop'
    allowed_domains = ['movie.douban.com/top250']
    start_urls = ['https://movie.douban.com/top250/']

    def parse(self, response):
        pass
