from pathlib import Path
import scrapy

class AppleSpider(scrapy.Spider):
    name = "apple_inc"
    allowed_domains = ["en.wikipedia.org"]
    custom_settings = {
        'DEPTH_LIMIT': 10,
        'MAX_PAGES': 300
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.page_count = 0

    def start_requests(self):
        start_urls = ["https://en.wikipedia.org/wiki/Apple_Inc."]
        for url in start_urls:
            yield scrapy.Request(url=url, callback=self.parse) 

    def parse(self, response):
        if self.page_count >= self.custom_settings.get('MAX_PAGES'):
            self.logger.info(f"Reached maximum pages limit ({self.custom_settings.get('MAX_PAGES')}). Stopping crawl.")
            return
        page = response.url.split("/")[-1]
        filename = f"D:/IRProject/course_project/crawler/webpages/{page}.html"
        file_path = Path(filename)
        file_path.write_bytes(response.body)

        self.page_count += 1

        yield {
            "title": response.css("span.mw-page-title-main::text").get(),
            "paragraphs": "".join(response.css("div.mw-content-ltr p::text").getall()),
        }
        for link in response.css("div.mw-content-ltr p a::attr(href)").extract()[:5]:
            if link.startswith("/wiki/") and ':' not in link:
                next_page = response.urljoin(link)
                yield scrapy.Request(next_page, callback=self.parse)  
