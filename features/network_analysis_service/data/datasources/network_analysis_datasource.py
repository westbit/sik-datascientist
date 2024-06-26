import logging

import matplotlib.pyplot as plt
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
        network_cluster = NetworkCluster()

        for website in website_network.websites:
            G.add_node(website["url"])
            for link in website["links"]:
                G.add_edge(website["url"], link)
                network_cluster.add_edge((website["url"], link))  # Gem kanten

        partitions = community.louvain_communities(G)
        for cluster in partitions:
            network_cluster.add_cluster(list(cluster))

        return network_cluster

    def identify_cluster(self, network_cluster: NetworkCluster):
        G = nx.Graph()
        for edge in network_cluster.edges:
            G.add_edge(*edge)

        pos = nx.spring_layout(
            G, k=0.01
        )  # positions for all nodes, juster 'k' værdien for at sprede noderne mere ud
        partitions = community.louvain_communities(G)
        colors = [f"C{index}" for index in range(len(partitions))]

        for index, partition in enumerate(partitions):
            nx.draw_networkx_nodes(
                G,
                pos,
                nodelist=list(partition),
                node_color=colors[index],
                node_size=700,
            )

        nx.draw_networkx_edges(G, pos, edgelist=G.edges(), edge_color="black")
        plt.axis("off")
        plt.show()
