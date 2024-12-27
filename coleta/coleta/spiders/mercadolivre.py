import scrapy

class MercadolivreSpider(scrapy.Spider):
    name = "mercadolivre"
    allowed_domains = ["mercadolivre.com.br"]
    start_urls = ["https://lista.mercadolivre.com.br/tenis-corrida-masculino"]

    def start_requests(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0'
        }
        for url in self.start_urls:
            yield scrapy.Request(url, headers=headers)

    def parse(self, response):
        products = response.css('div.poly-card__content')
        for product in products:
            old_price_parts = product.css('s.andes-money-amount--previous span::text').getall()
            old_price = ''.join(old_price_parts).replace('R$', '').strip()

            yield {
                'brand': product.css('span.poly-component__brand::text').get(),
                'name': product.css('h2.poly-box.poly-component__title a::text').get(),
                'old_price': old_price,
                'new_price': ''.join(product.css('span.andes-money-amount--cents-superscript span::text').getall()).replace('R$', '').strip(),
                'review_amount': product.css('span.poly-reviews__rating::text').get(),
                'review_rating_number': product.css('span.poly-reviews__total::text').re_first(r'\d+')
            }

