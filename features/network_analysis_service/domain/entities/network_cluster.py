class NetworkCluster:
    def __init__(self):
        self.clusters = []
        self.edges = []  # Tilføj en liste til at gemme kanter

    def add_cluster(self, cluster):
        self.clusters.append(cluster)

    def add_edge(self, edge):
        self.edges.append(edge)
