from .crawler import HttpCrawler

def test_http_crawler():
    target_url = "https://www.coingecko.com/pt"

    http_crawler = HttpCrawler(target_url)
    crawl_response = http_crawler.crawl_from_html()
    print(crawl_response)
