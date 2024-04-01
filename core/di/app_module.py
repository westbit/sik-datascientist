from logging.handlers import QueueHandler

import injector
from injector import Binder

from features.web_scraping_service.data.datasources.web_scraping_datasource import (
    WebScrapingDatasource,
)
from features.web_scraping_service.data.repositories.web_scraping_repository_impl import (
    WebScrapingRepositoryImpl,
)
from features.web_scraping_service.domain.usecases.scrape_website import ScrapeWebsite


class AppModule(injector.Module):
    def configure(self, binder: Binder):
        binder.bind(
            WebScrapingDatasource, to=WebScrapingDatasource, scope=injector.singleton
        )
        binder.bind(
            WebScrapingRepositoryImpl,
            to=WebScrapingRepositoryImpl,
            scope=injector.singleton,
        )
        binder.bind(ScrapeWebsite, to=ScrapeWebsite, scope=injector.singleton)
        binder.bind(QueueHandler, to=QueueHandler, scope=injector.singleton)
