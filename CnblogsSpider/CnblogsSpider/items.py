# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CnblogsspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    url=scrapy.Field()
    title=scrapy.Field()
    time=scrapy.Field()
    content=scrapy.Field()
    cimage_urls=scrapy.Field()
    cimages=scrapy.Field()
    #file_urls=scrapy.Field()
    #files=scrapy.Field()
