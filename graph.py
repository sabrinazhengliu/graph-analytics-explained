import networkx as nx
import itertools
import random


class MyGraph:

    def __init__(self, list_nodes=[], list_edges=[]) -> None:
        self.graph = nx.Graph()
        self.graph.add_nodes_from(list_nodes)
        self.graph.add_edges_from(list_edges)
        self.n_nodes = len(list_nodes)
        self.n_edges = len(list_edges)
        pass

    def __repr__(self) -> str:
        info = f"Graph ({self.n_nodes} nodes and {self.n_edges} edges)"
        return info


class RandomGraph(MyGraph):

    def __init__(self) -> None:
        super().__init__()
        list_nodes = self.generate_random_nodes()
        list_edges = self.generate_random_edges(list_nodes)
        self.graph.add_nodes_from(list_nodes)
        self.graph.add_edges_from(list_edges)
        self.n_nodes = len(list_nodes)
        self.n_edges = len(list_edges)
        pass

    @staticmethod
    def generate_random_nodes() -> list:
        n_nodes = random.randint(10, 100)
        list_nodes = list(range(n_nodes))
        return list_nodes

    @staticmethod
    def generate_random_edges(list_nodes) -> list:
        n_nodes = len(list_nodes)
        n_edges = random.randint(0, int(n_nodes * (n_nodes - 1) / 2))
        list_pairs = list(itertools.combinations(list_nodes, r=2))
        rand_index = random.sample(range(len(list_pairs)), n_edges)
        list_edges = [
            pair for pair in list_pairs
            if list_pairs.index(pair) in rand_index
        ]
        return list_edges


class CustomizedGrpah(MyGraph):
    def __init__(self) -> None:
        pass


def generate_graph(graph_type: str, n: int, r: float):

    if graph_type == 'Predefined Graph':
        G = nx.binomial_tree(8)
        pos = nx.spring_layout(G, seed=10)
        for i, _ in enumerate(G.nodes):
            G.nodes[i]['pos'] = pos[i]

    if graph_type == 'Random Graph':
        n = random.randint(1, 100)   # return int between 1 and 100
        p = random.random()          # return float between 0 and 1
        G = nx.gnp_random_graph(n, p)
        pos = nx.spring_layout(G)
        for i, _ in enumerate(G.nodes):
            G.nodes[i]['pos'] = pos[i]

    if graph_type == 'Customized Graph':
        G = nx.random_geometric_graph(n, r)

    return G


if __name__ == '__main__':

    g = MyGraph()

    n_nodes = 10
    n_edges = n_nodes - 1
    list_nodes = list(range(n_nodes))
    list_pairs = list(itertools.combinations(list_nodes, r=2))
    rand_index = random.sample(range(len(list_pairs)), n_edges)
    list_edges = [p for p in list_pairs if list_pairs.index(p) in rand_index]

    print(list_edges)
    g = MyGraph(list_nodes, list_edges)
    print(g)
