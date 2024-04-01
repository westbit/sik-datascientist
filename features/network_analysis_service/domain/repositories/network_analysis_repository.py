from abc import ABC, abstractmethod

from features.network_analysis_service.domain.entities.network_cluster import (
    NetworkCluster,
)
from features.web_scraping_service.domain.entities.website_network import WebsiteNetwork


class NetworkAnalysisRepository(ABC):
    @abstractmethod
    def load_network(self) -> WebsiteNetwork:
        pass

    @abstractmethod
    def analyze_network(self, website_network: WebsiteNetwork) -> NetworkCluster:
        pass
