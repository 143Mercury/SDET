import scrapy


class ErrorSpider(scrapy.Spider):
    name = "error_spider"
    start_urls = ["https://www.votpusk.ru/"]

    def parse(self, response):
        if response.status == 404:
            self.logger.error("404 Error found at %s", response.url)
        for link in response.css("a::attr(href)").getall():
            yield response.follow(link, self.parse)

