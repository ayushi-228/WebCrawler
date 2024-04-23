# Web Crawler

## Description
This Python project is a web crawler built using Scrapy that crawls Wikipedia pages related to Apple Inc. The crawler starts from the Wikipedia page for Apple Inc. and recursively follows links to other Wikipedia pages to gather information. The crawled data includes the title of each page and the text content of paragraphs within each page.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/ayushi-228/WebCrawler.git
   ```

3. Navigate to the project directory:
    ```bash
    cd wikipedia_crawler
    ```

4. (Optional) Create and activate a virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

5. Install Scrapy:
    ```bash
    pip install scrapy
    ```

## Usage
To run the web crawler, execute the following command:
```bash
scrapy crawl apple_inc -o output.json
```

## Spider
```bash
The `AppleSpider` class in this project is a Scrapy Spider specifically designed to crawl Wikipedia pages related to Apple Inc. It starts from the Wikipedia page for Apple Inc. (`https://en.wikipedia.org/wiki/Apple_Inc.`) and recursively follows links to other Wikipedia pages to gather information.

The Spider class has the following attributes and methods:

- `name`: The name of the Spider, which is `"apple_inc"`.
- `allowed_domains`: The list of allowed domains for the Spider to crawl, which includes `"en.wikipedia.org"`.
- `custom_settings`: A dictionary containing custom settings for the Spider, such as the maximum depth to crawl (`DEPTH_LIMIT`) and the maximum number of pages to crawl (`MAX_PAGES`).
- `__init__()`: The constructor method initializes the Spider object and sets the initial page count.
- `start_requests()`: A method that generates the initial requests to start crawling from the specified start URLs.
- `parse()`: The main parsing method that extracts data from each crawled page and yields the extracted data as Scrapy Items. It also follows links to other Wikipedia pages for further crawling.

The Spider class is responsible for crawling Wikipedia pages, extracting relevant information such as page titles and paragraph text, and following links to continue crawling recursively.
For more details on how the Spider works, refer to the code in `apple_spider.py`.
```
## Indexer
