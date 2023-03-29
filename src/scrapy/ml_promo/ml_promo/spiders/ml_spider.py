from pathlib import Path

import scrapy

# https://stackoverflow.com/questions/39202058/how-to-solve-403-error-in-scrapy
HEADERS = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:48.0) Gecko/20100101 Firefox/48.0'}

class PromosSpider(scrapy.Spider):
    name = "promos"

    def start_requests(self):
        urls = [
            'https://www.mercadolivre.com.br/ofertas?page=1'
        ]

        for url in urls:
            yield scrapy.Request(url=url, headers=HEADERS, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-1]
        self.log(f'Connected to {page}')

        for promo_item in response.css("li.promotion-item"):
            yield {
                'title': promo_item.css("p.promotion-item__title::text").get()
            }


        next_page = response.css("li.andes-pagination__button--next a::attr(href)").get()

        if next_page is not None:
            yield scrapy.Request(next_page, headers=HEADERS, callback=self.parse)