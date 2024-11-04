import scrapy

class SofaSpider(scrapy.Spider):
    name = "sofa_spider"
    allowed_domains = ["divan.ru"]
    start_urls = ["https://www.divan.ru/category/divany-i-kresla"]

    def parse(self, response):
        # Парсинг информации о диванах на текущей странице
        for product in response.css('div.lsooF'):
            price = product.css('div.q5Uds span::text').get()

            # Выдача данных
            if price:
                yield {
                    "Price": price,
                }

        # Переход на следующую страницу
        for page_number in range(1, 42):  # Страницы с 2 по 41
            next_page_url = f"https://www.divan.ru/category/divany-i-kresla/page-{page_number}"
            yield scrapy.Request(url=next_page_url, callback=self.parse)
