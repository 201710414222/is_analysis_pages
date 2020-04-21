# -*- coding: utf-8 -*-
import scrapy


class DripcarSpider(scrapy.Spider):
    name = 'dripcar'
    allowed_domains = ['www.dripcar.com']
    start_urls = ['http://www.dripcar.com/']

    def parse(self, response):
        div_list = response.xpath('//div[starts-with(@class, "models")]')
        # print(type(div_list))
        # 遍历列表，获取列表内容
        item_list = []
        for div in div_list:
            try:
                image_url = div.xpath('./div[@class="list_car"]/dl/dt/a/img/@src').extract()
                image_url = '\n'.join(image_url)
                information= div.xpath('./div[@class="list_car"]/dl/dd/p[@class="corolla nowrap"]/a/text()').extract()
                information = '\n'.join(information)

                price = div.xpath('./div[@class="list_car"]/dl/dd/p[@class="corolla_1"]/text()').extract()
                price = '\n'.join(price)

                item = dict(
                    image_url=image_url,
                    information=information,
                    price=price,
                )
                yield item
            except:
                print("爬取失败！")
                continue
