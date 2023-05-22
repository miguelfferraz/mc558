# -*- coding: utf-8 -*-


class Graph:
    """
    Class representing a graph.

    Attributes:
        n (int): The number of vertices in the graph.
        edges (list): List of edges in the graph.
        parent (list): The parent array used in the disjoint-set data structure.
        rank (list): The rank array used in the disjoint-set data structure.
    """

    def __init__(self, n: int):
        """
        Initialize a graph with the given number of vertices.

        Args:
            n (int): The number of vertices in the graph.
        """
        self.n = n

        self.edges = []

        self.parent = list(range(n))
        self.rank = [0] * n

    def add_edge(self, u: int, v: int, cost: int):
        """
        Add an edge to the graph.

        Args:
            u (int): The first vertex of the edge.
            v (int): The second vertex of the edge.
            cost (int): The cost or weight of the edge.
        """
        self.edges.append((u, v, cost))

    def make_set(self, vertex: int):
        """
        Initialize a disjoint-set for the given vertex.

        Args:
            vertex (int): The vertex to create a disjoint-set for.
        """
        self.parent[vertex] = vertex
        self.rank[vertex] = 0

    def find(self, vertex: int) -> int:
        """
        Find the representative (root) of the disjoint-set that the given vertex belongs to.

        Args:
            vertex (int): The vertex to find the representative for.

        Returns:
            int: The representative (root) of the disjoint-set.
        """
        if self.parent[vertex] != vertex:
            self.parent[vertex] = self.find(self.parent[vertex])
        return self.parent[vertex]

    def union(self, u: int, v: int):
        """
        Merge two disjoint-sets by rank.

        Args:
            u (int): The first vertex.
            v (int): The second vertex.
        """
        root_u = self.find(u)
        root_v = self.find(v)

        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1

    def kruskal(self, k: int) -> int:
        """
        Find the minimum cost of connecting the graph with a given number of clusters.

        Args:
            k (int): The number of clusters desired.

        Returns:
            int: The minimum cost of connecting the graph with the given number of clusters.
        """
        total_cost = 0
        num_clusters = self.n

        for vertex in range(self.n):
            self.make_set(vertex)

        self.edges.sort(key=lambda e: e[2])

        for u, v, cost in self.edges:
            if num_clusters == k:
                break

            if self.find(u) != self.find(v):
                self.union(u, v)
                total_cost += cost
                num_clusters -= 1

        return total_cost


def read_edges(graph: Graph, m: int):
    """
    Read edges from input and add them to the graph.

    Args:
        graph (Graph): The Graph object to add the edges to.
        num_edges (int): The number of edges to read.
    """
    for _ in range(m):
        a, b, cost = map(int, input().split())
        graph.add_edge(a, b, cost)


def main():
    """
    Entry point of the program.

    Reads input from the user, constructs a graph, and finds the
    minimum cost of creating k clusters using Kruskal's algorithm.
    Prints the minimum cost.
    """
    n, m, k = map(int, input().split())

    graph = Graph(n)
    read_edges(graph, m)
    print(graph.kruskal(k))


if __name__ == "__main__":
    main()
