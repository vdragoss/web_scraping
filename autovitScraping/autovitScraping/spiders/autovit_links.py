import scrapy
from ..items import AutovitLinks


class autovit_links(scrapy.Spider):
    name = 'autovit_links'
    page_number = 2
    start_urls = ['https://www.autovit.ro/autoturisme/?search%5Bfilter_float_price%3Afrom%5D=1&search%5Border%5D=created_at%3Adesc&search%5Bcountry%5D=&page=1']

    def parse(self, response):
        items = AutovitLinks()
        f = open("links.txt", "a")
        offers = response.css('div article')
        for offer in offers:
            link = offer.attrib['data-href']
            f.write(link + '\n')
        items['offers'] = offers

        yield items

        next_page = f'https://www.autovit.ro/autoturisme/?search%5Bfilter_float_price%3Afrom%5D=1&search%5Border%5D=created_at%3Adesc&search%5Bcountry%5D=&page={autovit_links.page_number}'

        if autovit_links.page_number < 5:
            autovit_links.page_number += 1
            yield response.follow(next_page, callback = self.parse)
