import scrapy


class AirpollutionSpider(scrapy.Spider):
    name = 'airpollution'
    allowed_domains = ['www.accuweather.com']
    start_urls = ['https://www.accuweather.com/en/gb/kings-heath/b14-7/air-quality-index/321753']

    def parse(self, response):


        # Get days of week from today to three days into the future
        # days = response.css('p.day-of-week ::text').getall()
        # Remove duplicate 'today' item from list
        # days.remove(days[0])
        # Loop through remaining days
        #days = response.css('div.air-quality-daily-list').getall()
        # days = response.css('div.air-quality-content ::text').getall()

        for day in response.css('div.air-quality-daily-list'):
            # 1. Get pollution index number
            pollution_index = day.css('div.aq-number ::text').get().strip()
            # 2. Get classifcation e.g. fair, good
            pollution_string = day.css('p.category-text ::text').get()
            # 3. Get description of quality
            pollution_descrip = day.css('p.statement ::text').get().strip()
            # 4. Get date 
            date = day.css('p.date ::text').get().strip()


            yield {
                "Date": date,
                "Pollution index": pollution_index,
                "Classification": pollution_string,
                "Description": pollution_descrip
            }