import scrapy


class AirpollutionSpider(scrapy.Spider):
    name = 'airpollution'
    allowed_domains = ['www.accuweather.com']
    start_urls = ['https://www.accuweather.com/en/gb/kings-heath/b14-7/air-quality-index/321753']

    def parse(self, response):
        # 1. Get pollution index number
        pollution_index = response.css('div.aq-number ::text').get().strip()
        # 2. Get classifcation e.g. fair, good
        pollution_string = response.css('p.category-text ::text').get()
        # 3. Get description of quality
        pollution_descrip = response.css('p.statement ::text').get().strip()


        yield {
            "Pollution index": pollution_index,
            "Classification": pollution_string,
            "Description": pollution_descrip
        }