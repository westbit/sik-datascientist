from abc import ABC, abstractmethod

from features.web_scraping_service.domain.entities.website import Website


class WebScrapingRepository(ABC):
    @abstractmethod
    def scrape_website(self, url: str) -> Website:
        pass
