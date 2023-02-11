import scrapy


class AirpollutionSpider(scrapy.Spider):
    name = 'airpollution'
    allowed_domains = ['www.accuweather.com']
    start_urls = ['https://www.accuweather.com/en/gb/kings-heath/b14-7/air-quality-index/321753']

    def parse(self, response):
        # Get days of week from today to three days into the future
        days = response.css('p.day-of-week ::text').getall()
        # Remove duplicate 'today' item from list
        days.remove(days[0])
        # Loop through remaining days
        rows = response.css('div.air-quality-daily-list')
        # 1. Get pollution index number
        pollution_index = rows.css('div.aq-number ::text').getall()
        # 2. Get classifcation e.g. fair, good
        pollution_string = rows.css('p.category-text ::text').getall()
        # 3. Get description of quality
        pollution_descrip = rows.css('p.statement ::text').getall()
        # 4. Get date 
        dates = rows.css('p.date ::text').getall()
        
        i=0
        for day in days: 
            yield {
                "Date": dates[i],
                "Day": day.strip(),
                "Pollution index": pollution_index[i].strip(),
                "Classification": pollution_string[i].strip(),
                "Description": pollution_descrip[i].strip()
            }
            i+=1