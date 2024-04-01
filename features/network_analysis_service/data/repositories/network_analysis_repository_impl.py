import injector

from features.network_analysis_service.data.datasources.network_analysis_datasource import (
    NetworkAnalysisDatasource,
)
from features.network_analysis_service.domain.entities.network_cluster import (
    NetworkCluster,
)
from features.network_analysis_service.domain.repositories.network_analysis_repository import (
    NetworkAnalysisRepository,
)
from features.web_scraping_service.domain.entities.website_network import WebsiteNetwork


class NetworkAnalysisRepositoryImpl(NetworkAnalysisRepository):
    @injector.inject
    def __init__(self, datasources: NetworkAnalysisDatasource) -> None:
        self.datasource = datasources

    def load_network(self) -> WebsiteNetwork:
        return self.datasource.load_network()

    def analyze_network(self, website_network: WebsiteNetwork) -> NetworkCluster:
        return self.datasource.analyze_network(website_network)
