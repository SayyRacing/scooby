import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy import signals
import time

class WantedPersonsSpider(scrapy.Spider):
    name = 'wanted_persons'
    start_urls = ['https://poszukiwani.policja.pl/pos/form/5,Poszukiwani.html?page=0']
    page_count = 0

    custom_settings = {
        'FEED_FORMAT': 'csv',
        'FEED_URI': 'wanted_persons.csv',
        'CONCURRENT_REQUESTS': 300,
        'LOG_ENABLED': False,
    }

    def parse(self, response):
        # Sprawdź, czy określony fragment HTML jest pusty
        if not response.css('div.okno ul.flex li'):
            return
        # Znajdź wszystkie osoby poszukiwane na stronie
        for person in response.css('li.threeRows.thumbList'):
            yield {
                'Name': person.css('strong::text').get().strip(),
                'Link': response.urljoin(person.css('a::attr(href)').get())
            }
        # Przejdź do następnej strony, jeśli istnieje
        next_page = response.css('div#meni_strony ul li a:contains("następna")::attr(href)').get()
        if next_page is not None:
            self.page_count += 1
            yield response.follow(next_page, self.parse)

    @classmethod
    def from_crawler(cls, crawler, *args, **kwargs):
        spider = super().from_crawler(crawler, *args, **kwargs)
        crawler.signals.connect(spider.spider_closed, signal=signals.spider_closed)
        return spider

    def spider_closed(self, spider):
        print(f"Number of pages scraped: {self.page_count}")

def scrapy_find_all():
    # Uruchom proces Scrapy
    process = CrawlerProcess()
    start_time = time.time()
    process.crawl(WantedPersonsSpider)
    process.start()
    end_time = time.time()
    elapsed_time = end_time - start_time
    minutes, seconds = divmod(elapsed_time, 60)
    print(f"Process duration: {minutes:.0f} minutes {seconds:.2f} seconds")
