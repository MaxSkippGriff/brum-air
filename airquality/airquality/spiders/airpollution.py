import scrapy


class AirpollutionSpider(scrapy.Spider):
    name = 'airpollution'
    allowed_domains = ['www.accuweather.com']
    start_urls = ['https://www.accuweather.com/en/gb/kings-heath/b14-7/weather-forecast/321753']

    def parse(self, response):
        pollution_num = response.css('div.aq-number ::text').get().strip()
        pollution_string = response.css('p.category-text ::text').get()

        yield {
            "Pollution index": pollution_num,
            "Description": pollution_string
        }