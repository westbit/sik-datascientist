import injector

from features.web_scraping_service.data.datasources.web_scraping_datasource import (
    WebScrapingDatasource,
)
from features.web_scraping_service.data.models.website_model import WebsiteModel
from features.web_scraping_service.domain.entities.website import Website
from features.web_scraping_service.domain.repositories.web_scraping_repository import (
    WebScrapingRepository,
)


class WebScrapingRepositoryImpl(WebScrapingRepository):
    @injector.inject
    def __init__(self, data_source: WebScrapingDatasource):
        self.data_source = data_source

    def scrape_website(self, url: str) -> Website:
        try:
            result = self.data_source.scrape_website(url)
            return WebsiteModel.to_entity(result)
        except Exception as e:
            raise e
