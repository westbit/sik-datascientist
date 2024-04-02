import injector

from features.network_analysis_service.domain.repositories.network_analysis_repository import (
    NetworkAnalysisRepository,
)
from features.network_analysis_service.domain.usecases.analyze_network import (
    AnalyzeNetwork,
)


class IdentifyCluster:
    @injector.inject
    def __init__(
        self, repository: NetworkAnalysisRepository, analyze_network: AnalyzeNetwork
    ) -> None:
        self.repository = repository
        self.analyze_network = analyze_network

    def execute(self):
        network_cluster = self.analyze_network.execute()
        self.repository.identify_cluster(network_cluster)
