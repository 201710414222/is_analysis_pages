# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CarItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #保存图片url
    image_url=scrapy.Field()
    #保存商品信息
    information=scrapy.Field()
    #保存商品价格
    price=scrapy.Field()
    pass
