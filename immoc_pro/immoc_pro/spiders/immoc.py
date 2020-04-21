# -*- coding: utf-8 -*-
import scrapy


class ImmocSpider(scrapy.Spider):
    name = 'immoc'
    allowed_domains = ['www.imooc.com']
    start_urls = ['http://www.imooc.com/']

    def parse(self, response):
        div_list = response.xpath('//div[starts-with(@class, "clearfix types-content")]')
        # 遍历列表，获取列表内容
        item_list = []
        for div in div_list:
            '''
            先通过xpath获取内容，返回的是一个列表
            然后通过extract()转换成unicode字符串，再获取第0个, 也就是指定的内容
            将解析到的内容保存到字典中
            '''
            try:

             img_url = div.xpath(
                './div[@class="index-card-container course-card-container container"]/a[@class="course-card"]/div[@class="course-card-top hashadow"]/img[@class="course-banner"]/@src').extract()
             img_url = '\n'.join(img_url)
             imformation = div.xpath(
                './div[@class="index-card-container course-card-container container"]/a[@class="course-card"]/div[@class="course-card-content"]/h3[@class="course-card-name"]/text()').extract()

             imformation = '\n'.join(imformation)
             price = div.xpath(
                './div[@class="index-card-container course-card-container container"]/a[@class="course-card"]/div[@class="course-card-content"]/div[@class="clearfix course-card-bottom"]/div[@class="course-card-price sales"]/text()').extract()

             price = '\n'.join(price)
             item = dict(
                img_url=img_url,
                imformation=imformation,
                price=price,

             )
             yield item
            except:
             print("爬取失败！")
            continue
