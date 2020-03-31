# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class EConItem(scrapy.Item):
    # define the fields for your item here like:
    store_name = scrapy.Field()     # 商家名
    store_url = scrapy.Field()      # store_url
    mode_manage = scrapy.Field()    # 主营
    phone_list = scrapy.Field()     # 手机号
    qq_list = scrapy.Field()        # QQ号
    wangwang = scrapy.Field()       # 旺旺
    address = scrapy.Field()        # 地址
    wechat = scrapy.Field()         # 微信
    main_puduct = scrapy.Field()
    puduct_detail = scrapy.Field()
    sell_counts = scrapy.Field()    # 商品总数
    latest_time = scrapy.Field()    # 最新上新时间
    date = scrapy.Field()           # 采集日期
