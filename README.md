# Brum-Air

## Scrape air quality data 

This Django-Scrapy app scrapes air quality data for King's Heath, Birmingham, and displays it on 
a single page. Data includes daily and weekly air quality forecasts.

## How it works

There are five main steps:

1. The client sends a request to crawl specified url
2. Django tells Scrapy to crawl this url
3. Django tells the client that crawling has begun
4. Scrapy scrapes url and saves data in a database
5. Django grabs the data from the database and returns it to the client



## Technologies

* Python 3.8
* Scrapy 2.7
* Django 4.1.6

## Instructions

1. Fork or clone project
2. Create virtual environment

    ``` python3 -m venv env ```
3. Activate virtual environment 

    ``` source env/bin/activate ```
4. Dependencies are saved in the Pipfile. To install, run the following command:

    ``` pipenv install ```

## Using scrapy shell

Once you've executed the instructions above, start up the scrapy shell,

``` scrapy shell ```

Then fetch the accweather url with the following:

``` fetch('https://www.accuweather.com/en/gb/birmingham/b5-5/air-quality-index/326966') ```

Now you can create custom css selectors to grab data from the accweather site. For example, if you want 
to get Birmingham's pollution level today, simply type:

``` response.css('div.aq-number ::text').get().strip() ``` 


## Running scraper

To run the scraper, navigate to the directory containing scrapy.cfg and run the following command:

```scrapy crawl airpollution -o <filename>.json```

You can export data to json or csv.

## Integrating with Django

## Technologies

* Python 3.8
* Scrapy 2.7