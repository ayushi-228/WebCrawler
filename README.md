# Wikipedia Crawler

## Description
This Python project is a web crawler built using Scrapy that crawls Wikipedia pages related to Apple Inc. The crawler starts from the Wikipedia page for Apple Inc. and recursively follows links to other Wikipedia pages to gather information. The crawled data includes the title of each page and the text content of paragraphs within each page.

## Installation
1. Clone the repository:

2. Navigate to the project directory:
    ```bash
    cd wikipedia_crawler
    ```

3. (Optional) Create and activate a virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

4. Install Scrapy:
    ```bash
    pip install scrapy
    ```

## Usage
To run the web crawler, execute the following command:
```bash
scrapy crawl apple_inc -o output.json
