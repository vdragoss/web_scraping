import scrapy
from ..items import AutovitscrapingItem


class autovit(scrapy.Spider):
    name = 'autovit_spider'
    page_number = 2
    start_urls = ['https://www.autovit.ro/autoturisme/second/?search%5Bfilter_float_price%3Afrom%5D=100&search%5Border%5D=created_at%3Adesc&page=1']

    def parse(self, response):
        items = AutovitscrapingItem()
        nr_of_ads = len(response.css('.ds-param:nth-child(1) span').css('::text').extract())

        for ad in range(nr_of_ads):
            title = response.css('.offer-title__link::text')[ad].extract()
            city = response.css('.ds-location-city::text')[ad].extract()
            county = response.css('.ds-location-region::text')[ad].extract()
            year = response.css('.ds-param:nth-child(1) span').css('::text')[ad].extract()
            km = response.css('.ds-param:nth-child(2) span::text')[ad].extract()
            engine = response.css('.ds-param:nth-child(3) span::text')[ad].extract()
            fuel = response.css('.ds-param:nth-child(4) span::text')[ad].extract()
            price = response.css('.ds-price-number span:nth-child(1)::text')[ad].extract()

            items['title'] = title
            items['city'] = city
            items['county'] = county
            items['year'] = year
            items['km'] = km
            items['engine'] = engine
            items['fuel'] = fuel
            items['price'] = price

            yield items

        # next_page = f'http://quotes.toscrape.com/page/{Quotes.page_number}/'
        #
        # if Quotes.page_number < 11:
        #     Quotes.page_number += 1
        #     yield response.follow(next_page, callback = self.parse)
