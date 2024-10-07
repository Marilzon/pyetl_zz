from typing import Dict
from requests import get, exceptions


class HttpCrawler:
    def __init__(self, url: str) -> None:
        self.__url = url

    def crawl_from_html(self) -> Dict[int, str]:
        try:
            response = get(self.__url)

            return {
                "status_code": response.status_code,
                "html": response.text,
            }

        except exceptions.RequestException as e:
            print(f"Error during request: {e}")
            return None
