# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AutovitscrapingItem(scrapy.Item):
    # define the fields for your item here like:
    seller = scrapy.Field()
    make = scrapy.Field()
    model = scrapy.Field()
    version = scrapy.Field()
    year = scrapy.Field()
    km = scrapy.Field()
    engine_size = scrapy.Field()
    fuel = scrapy.Field()
    power = scrapy.Field()
    transmission = scrapy.Field()
    drive = scrapy.Field()
    euro = scrapy.Field()
    body_style = scrapy.Field()
    country = scrapy.Field()
    no_accident = scrapy.Field()
    service_history = scrapy.Field()
    registered = scrapy.Field()
    condition = scrapy.Field()
    location = scrapy.Field()
    price = scrapy.Field()
    links = scrapy.Field()
    pass

class AutovitLinks(scrapy.Item):
    offers = scrapy.Field()
    links = scrapy.Field()
