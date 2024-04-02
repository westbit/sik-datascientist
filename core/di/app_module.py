import injector
from injector import Binder

from features.network_analysis_service.data.datasources.network_analysis_datasource import (
    NetworkAnalysisDatasource,
)
from features.network_analysis_service.data.repositories.network_analysis_repository_impl import (
    NetworkAnalysisRepositoryImpl,
)
from features.network_analysis_service.domain.repositories.network_analysis_repository import (
    NetworkAnalysisRepository,
)
from features.network_analysis_service.domain.usecases.analyze_network import (
    AnalyzeNetwork,
)
from features.network_analysis_service.domain.usecases.identify_cluster import (
    IdentifyCluster,
)
from features.web_scraping_service.data.datasources.web_scraping_datasource import (
    WebScrapingDatasource,
)
from features.web_scraping_service.data.repositories.web_scraping_repository_impl import (
    WebScrapingRepositoryImpl,
)
from features.web_scraping_service.domain.repositories.web_scraping_repository import (
    WebScrapingRepository,
)
from features.web_scraping_service.domain.services.queue_handler import QueueHandler
from features.web_scraping_service.domain.usecases.scrape_website import ScrapeWebsite


class AppModule(injector.Module):
    def configure(self, binder: Binder):
        # Webscraping feature
        binder.bind(
            WebScrapingDatasource, to=WebScrapingDatasource, scope=injector.singleton
        )
        binder.bind(
            WebScrapingRepository,  # type: ignore
            to=WebScrapingRepositoryImpl,
            scope=injector.singleton,
        )
        binder.bind(QueueHandler, to=QueueHandler, scope=injector.singleton)
        binder.bind(ScrapeWebsite, to=ScrapeWebsite, scope=injector.singleton)

        # Network analysis feature
        binder.bind(
            NetworkAnalysisDatasource,
            to=NetworkAnalysisDatasource,
            scope=injector.singleton,
        )
        binder.bind(
            NetworkAnalysisRepository,  # type: ignore
            to=NetworkAnalysisRepositoryImpl,
            scope=injector.singleton,
        )
        binder.bind(AnalyzeNetwork, to=AnalyzeNetwork, scope=injector.singleton)
        binder.bind(IdentifyCluster, to=IdentifyCluster, scope=injector.singleton)
