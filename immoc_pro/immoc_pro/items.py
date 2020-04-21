# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ImmocProItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #保存图片uml
    img_url=scrapy.Field()
    #保存图片信息
    imformation=scrapy.Field()
    #保存图片价格
    price=scrapy.Field()

