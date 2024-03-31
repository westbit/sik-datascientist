from injector import inject

from features.web_scraping_service.domain.entities.website import Website
from features.web_scraping_service.domain.repositories.web_scraping_repository import (
    WebScrapingRepository,
)


class ScrapeWebsite:
    @inject
    def __init__(self, repository: WebScrapingRepository):
        self.repository = repository

    def execute(self, url: str) -> Website:
        return self.repository.scrape_website(url)
