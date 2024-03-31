import requests
from bs4 import BeautifulSoup
from requests.exceptions import RequestException

from features.web_scraping_service.data.models.website_model import WebsiteModel


class WebScrapingDatasource:
    def scrape_website(self, url: str) -> WebsiteModel:
        try:
            response = requests.get(url)
            response.raise_for_status()  # Tjekker for HTTP fejl
            soup = BeautifulSoup(response.text, "html.parser")

            links = []
            for link in soup.find_all("a", href=True):
                links.append(link["href"])

            return WebsiteModel(url, links)
        except RequestException as e:
            raise Exception(f"Fejl ved hentning af siden: {e}")
        except Exception as e:
            raise Exception(f"Generel fejl: {e}")
