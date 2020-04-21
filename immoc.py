# -*- coding: utf-8 -*-
import scrapy


class ImmocSpider(scrapy.Spider):
    name = 'immoc'
    allowed_domains = ['www.imooc.com']
    start_urls = ['http://www.imooc.com/']

    def parse(self, response):
        pass
