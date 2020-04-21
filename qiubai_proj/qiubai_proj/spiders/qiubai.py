import scrapy


class QiubaiSpider(scrapy.Spider):
    name = 'qiubai'
    allowed_domains = ['www.qiushibaike.com']
    start_urls = ['http://www.qiushibaike.com/']

    def parse(self, response):
        li_list = response.xpath('//li[starts-with(@id, "qiushi_tag_")]')
        #print(type(div_list))
        # 遍历列表，获取列表内容
        item_list = []
        for div in li_list:
            '''
            先通过xpath获取内容，返回的是一个列表
            然后通过extract()转换成unicode字符串，再获取第0个, 也就是指定的内容
            将解析到的内容保存到字典中
            '''
            try:
                image_url = div.xpath('./div[@class="recmd-right"]/div[@class="recmd-detail clearfix"]/a[@class="recmd-user"]/img/@src').extract()
                name = div.xpath('./div[@class="recmd-right"]/div[@class="recmd-detail clearfix"]/a[@class="recmd-user"]/span[@class=recmd-name]/text').extract()
                #age = div.xpath('./div[@class="author clearfix"]/div/text()').extract_first()
                content = div.xpath('./div[@class="recmd-right"]/a[@class="recmd-content"]/text()').extract()
                content = ' '.join(content)
                haha_count = div.xpath(
                    './div[@class="recmd-right"]/div[@class="recmd-detail clearfix"]/div[@class="recmd-num"]/span/text()').extract_first()
                item = dict(
                    image_url=image_url,
                    name=name,
                    content=content,
                    haha_count=haha_count
                )
                yield item
            except:
                continue