# -*- coding: utf-8 -*-
from scrapy import Request
from scrapy.spiders import Spider
from douban.items import DoubanItem


class DoubantopSpider(Spider):
    name = 'doubantop'
    # allowed_domains = ['movie.douban.com/top250']
    # start_urls = ['https://movie.douban.com/top250/']
    # headers = {
    #     'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
    # }
    def start_requests(self):
        url = 'https://movie.douban.com/top250'
        # yield Request(url, headers=self.headers)
        yield Request(url)

    def parse(self, response):
        # pass
        item = DoubanItem()
        movies = response.xpath('.//ol[@class="grid_view"]/li')
        # print 'title is :' + tt[0]
        for movie in movies:
            item['ranking'] = movie.xpath('.//div[@class="pic"]/em/text()').extract_first()
            item['movie_name'] = movie.xpath('.//div[@class="hd"]/a/span/text()').extract_first()
            item['score'] = movie.xpath('.//div[@class="star"]/span[@class="rating_num"]/text()').extract_first()
            item['score_num'] = movie.xpath('.//div[@class="star"]/span/text()').re(ur'(\d+)人评价')[0]
            yield item
            print item['ranking'],item['movie_name'],item['score'],item['score_num'] 

        next_url = response.xpath('//span[@class="next"]/a/@href').extract()
        if next_url:
            next_url = 'https://movie.douban.com/top250' + next_url[0]
            # yield Request(url=next_url, headers=self.headers)
            yield Request(url=next_url)
