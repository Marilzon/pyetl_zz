from typing import Dict
import requests


class HttpRequest:
    def __init__(self) -> None:
        self.__url = "https://www.databricks.com/br/blog"

    def request_from_page(self) -> Dict[int, str]:
        content = requests.get(self.__url, timeout=10)

        return {
            "status_code": content.status_code,
            "html": content.text
        }
