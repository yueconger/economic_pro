# -*- coding: utf-8 -*-
import scrapy
import re
from e_con.items import EConItem


class Bao66Spider(scrapy.Spider):
    name = 'bao66'
    allowed_domains = ['bao66.cn']
    start_urls = ['http://www.bao66.cn/']

    def start_requests(self):
        letter_list = [chr(i) for i in range(65, 91)]  # 所有大写字母
        letter_list.append("9")
        for letter in letter_list:
            url_original = "http://www.bao66.cn/supplier/0,0,{0},1,1,all.html".format(letter)
            yield scrapy.Request(
                url=url_original,
                callback=self.parse
            )

    def parse(self, response):
        if response.status != 200:
            print("状态码不正常")
        else:
            page_urlList = []
            try:
                pageList = response.xpath('//ul[@class="pageList"]/li')
            except Exception as e:
                print("本页没有其他内容", e)
            else:
                for page in pageList:
                    next_page = page.xpath('./a/@href').extract_first()
                    url = response.urljoin(next_page)  # 构建next_page链接
                    page_urlList.append(url)

                """具体信息部分"""
                li_list = response.xpath('//ul[@class="seller_list"]/li')
                for li in li_list:
                    item = EConItem()
                    detail = li.xpath('./div[@class="col-md-7 col-xs-7 list_con"]')
                    item['store_name'] = detail.xpath('./div[@class="name"]/a/text()').extract_first()  # 店铺名称
                    item['store_url'] = detail.xpath('./div[@class="name"]/a/@href').extract_first()  # 店铺url

                    mode_manage = detail.xpath('./div[@class="url"][2]/text()').extract_first()  # 经营模式
                    item['mode_manage'] = mode_manage.split("经营模式：")[1] if "经营模式：" in mode_manage else ""

                    phone_str = detail.xpath('./div[@class="text"][1]/span/text()').extract_first()  # 联系电话
                    phone_list = phone_str.split("电话：")[1] if "电话：" in phone_str else ""
                    item['phone_list'] = phone_list.split()  # list类型

                    qq = detail.xpath('./div[@class="text"][1]/span[2]/img/@data-supplier-qq').extract_first()  # qq号
                    qq_list = re.sub("、|,|/", " ", qq)
                    item['qq_list'] = qq_list.split()  # list类型

                    wangwang = detail.xpath(
                        './div[@class="text"][1]/span[3]/img/@data-supplier-wangwang').extract_first()  # 旺旺号 没有则为空
                    # wangwang = wangwang if wangwang != "" else "无"
                    item['wangwang'] = wangwang

                    address = detail.xpath('./div[@class="text"][2]/text()').extract_first()
                    item['address'] = address.split("拿货地址：")[1].strip()

                    yield scrapy.Request(
                        url=item['store_url'] + "/all,1,1",
                        meta={'item': item},
                        callback=self.detail_parse
                    )

                for page_url in page_urlList:
                    yield scrapy.Request(
                        url=page_url,
                        callback=self.parse

                    )

    def detail_parse(self, response):
        print(response.url)
        item = response.meta['item']
        categorys = response.xpath('//ul[@class="screen_menu"]/li[not(@id="categorys")]')
        sell_type = []
        sell_counts = 0
        for cate in categorys:
            cate_dict = {}
            cate_dict['产品类型'] = cate.xpath('./a/text()').extract_first()
            nums = cate.xpath('./a/span/text()').extract_first()
            cate_dict['产品数量'] = int(nums) if nums != '' else 0
            sell_counts += cate_dict['产品数量']
            sell_type.append(cate_dict)
        cates = []
        for i in sell_type:
            cates.append(i['产品类型'])
        item['main_puduct'] = '/'.join(cates)

        item['puduct_detail'] = {'所有商品': sell_counts, }
        print('###########', item)
