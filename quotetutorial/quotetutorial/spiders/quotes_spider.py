import scrapy
from ..items import QuotetutorialItem


class Quotes(scrapy.Spider):
    name = 'quotes'
    page_number = 2
    start_urls = ['http://quotes.toscrape.com/page/1/']

    def parse(self, response):
        all_div_quotes = response.css('div.quote')
        items = QuotetutorialItem()

        for quotes in all_div_quotes:
            title = quotes.css('span.text::text').extract()
            author = quotes.css('.author::text').extract()
            tag = quotes.css('.tag::text').extract()

            items['title'] = title
            items['author'] = author
            items['tag'] = tag

            yield items

        next_page = f'http://quotes.toscrape.com/page/{Quotes.page_number}/'

        if Quotes.page_number < 11:
            Quotes.page_number += 1
            yield response.follow(next_page, callback = self.parse)
