import injector

from features.network_analysis_service.domain.entities.network_cluster import (
    NetworkCluster,
)
from features.network_analysis_service.domain.repositories.network_analysis_repository import (
    NetworkAnalysisRepository,
)


class AnalyzeNetwork:
    @injector.inject
    def __init__(self, repository: NetworkAnalysisRepository) -> None:
        self.repository = repository

    def execute(self) -> NetworkCluster:
        self.website_network = self.repository.load_network()
        return self.repository.analyze_network(self.website_network)
