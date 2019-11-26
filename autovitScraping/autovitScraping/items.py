# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AutovitscrapingItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    city = scrapy.Field()
    county = scrapy.Field()
    year = scrapy.Field()
    km = scrapy.Field()
    engine = scrapy.Field()
    fuel = scrapy.Field()
    price = scrapy.Field()
    pass
