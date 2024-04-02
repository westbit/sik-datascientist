import requests
from bs4 import BeautifulSoup
from requests.adapters import HTTPAdapter
from requests.exceptions import RequestException
from urllib3 import Retry

from features.web_scraping_service.data.models.website_model import WebsiteModel


class WebScrapingDatasource:
    def __init__(self):
        retries = Retry(
            total=3, backoff_factor=1, status_forcelist=[429, 500, 502, 503, 504]
        )
        self.session = requests.Session()
        self.session.mount("http://", HTTPAdapter(max_retries=retries))
        self.session.mount("https://", HTTPAdapter(max_retries=retries))

    def scrape_website(self, url: str) -> WebsiteModel:
        try:
            response = self.session.get(url, timeout=5)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, "html.parser")

            links = []
            for link in soup.find_all("a", href=True):
                href = link["href"]
                if href.startswith("http"):
                    links.append(href)
                elif href.startswith("/"):
                    full_url = requests.compat.urljoin(url, href)
                    links.append(full_url)

            return WebsiteModel(url, links)
        except RequestException:
            # Returner en tom WebsiteModel for at fortsætte processen
            return WebsiteModel(url, [])
        except Exception as e:
            raise Exception(f"Generel fejl: {e}")
