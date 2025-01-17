import scrapy

class MercadolivreSpider(scrapy.Spider):
    name = "mercadolivre"
    allowed_domains = ["mercadolivre.com.br"]
    start_urls = ["https://lista.mercadolivre.com.br/tenis-corrida-masculino"]
  
    def parse(self, response):
        products = response.css('div.poly-card__content')
        for product in products:
            prices = product.css('span.andes-money-amount__fraction::text').getall()
            cents = product.css('span.andes-money-amount__cents::text').getall()
            yield {
                'brand': product.css('span.poly-component__brand::text').get(),
                'name': product.css('h2.poly-component__title-wrapper a::text').get(),
                'old_price_reais': prices[0] if len(prices) > 0 else None,
                'old_price_centavos': cents[0] if len(cents) > 0 else None,
                'new_price_reais': prices[1] if len(prices) > 1 else None,
                'new_price_centavos': cents[1] if len(cents) > 1 else None,
                'review_amount': product.css('span.poly-reviews__rating::text').get(),
                'review_rating_number': product.css('span.poly-reviews__total::text').get()
            }
