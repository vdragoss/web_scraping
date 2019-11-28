import scrapy
from ..items import AutovitscrapingItem


class autovit_carinfo(scrapy.Spider):
    name = 'autovit_carinfo'
    with open("links.txt") as f:
         start_urls = [url.strip() for url in f.readlines()]

    def parse(self, response):
        items = AutovitscrapingItem()
        parameters = response.css('div.offer-params ul li.offer-params__item')

        seller=make=model=version=year=km=engine_size=fuel=power=transmission=drive=euro=body_style=country=no_accident=service_history=condition=registered=price=location = 'na'
        for param in parameters:

            header = param.css('span::text').extract()[0]
            if param.css('a::text').extract():
                content = param.css('a::text').extract()
            else:
                content = param.css('div::text').extract()

            if header == "Oferit de":
                seller = content
            elif header == "Marca":
                make = content
            elif header == "Model":
                model = content
            elif header == "Versiune":
                version = content
            elif header == "Anul fabricatiei":
                year = content
            elif header == "Km":
                km = content
            elif header == "Capacitate cilindrica":
                engine_size = content
            elif header == "Combustibil":
                fuel = content
            elif header == "Putere":
                power = content
            elif header == "Cutie de viteze":
                transmission = content
            elif header == "Norma de poluare":
                euro = content
            elif header == "Transmisie":
                drive = content
            elif header == "Caroserie":
                body_style = content
            elif header == "Tara de origine":
                country = content
            elif header == "Fara accident in istoric":
                no_accident = content
            elif header == "Carte de service":
                service_history = content
            elif header == "Stare":
                condition = content
            elif header == "Inmatriculat":
                registered = content

        price = response.css('.offer-price__number::text')[0].extract()
        currency = response.css('.offer-price__currency::text')[0].extract()
        location = response.css(".seller-box__seller-address__label::text")[0].extract()

        items['seller'] = seller
        items['make'] = make
        items['model'] = model
        items['version'] = version
        items['year'] = year
        items['km'] = km
        items['engine_size'] = engine_size
        items['fuel'] = fuel
        items['power'] = power
        items['transmission'] = transmission
        items['drive'] = drive
        items['euro'] = euro
        items['body_style'] = body_style
        items['country'] = country
        items['no_accident'] = no_accident
        items['service_history'] = service_history
        items['registered'] = registered
        items['condition'] = condition
        items['location'] = location
        items['price'] = price
        # items['link'] = autovit_carinfo.start_urls
        items['currency'] = currency

        yield items

        # next_page = 'https://www.autovit.ro/anunt/audi-q5-ID7GzScv.html'
        # for i in range(len(links)):
        #     yield response.follow(links[i], callback = self.parse)
