import logging

import networkx as nx
from networkx.algorithms import community

from features.network_analysis_service.domain.entities.network_cluster import (
    NetworkCluster,
)
from features.web_scraping_service.domain.entities.website_network import WebsiteNetwork


class NetworkAnalysisDatasource:
    def __init__(self) -> None:
        self.website_network = WebsiteNetwork()

    def load_network(self) -> WebsiteNetwork:
        try:
            self.website_network.load()
        except FileNotFoundError:
            logging.error("Website network JSON file not found.")
        return self.website_network

    def analyze_network(self, website_network: WebsiteNetwork) -> NetworkCluster:
        G = nx.Graph()

        for website in website_network.websites:
            G.add_node(website["url"])
            for link in website["links"]:
                G.add_edge(website["url"], link)

        partitions = community.louvain_communities(G)

        network_cluster = NetworkCluster()

        for cluster in partitions:
            network_cluster.add_cluster(list(cluster))

        return network_cluster
