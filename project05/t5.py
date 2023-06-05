# -*- coding: utf-8 -*-

SUCCESS = "possible"
FAILURE = "impossible"

INITIAL_ENERGY = 100

INF = float("inf")
NEG_INF = float("-inf")


class Graph:
    def __init__(self, n: int, vertices_cost: list):
        """
        Initializes a graph with the given number of vertices and their corresponding cost.

        Args:
            n (int): The number of vertices in the graph.
            vertices_cost (list): The cost associated with each vertex.
        """
        self.n = n
        self.vertices_cost = vertices_cost
        self.edges = []

    def add_edge(self, u: int, v: int):
        """
        Adds a directed edge from vertex u to vertex v in the graph.

        Args:
            u (int): The source vertex of the edge.
            v (int): The destination vertex of the edge.
        """
        self.edges.append((u, v, self.vertices_cost[v]))

    def bellman_ford(self, origin: int, destination: int, limit: float = float("inf")) -> float:
        """
        Finds the shortest path distance from the origin vertex to the
        destination vertex using the Bellman-Ford algorithm.
        The algorithm stops if the path exceeds the given limit.

        Args:
            origin (int): The source vertex.
            destination (int): The destination vertex.
            limit (float): The maximum allowed path distance.

        Returns:
            float: The shortest path distance from the origin to the destination if
                   it is within the limit, positive infinity if it is not possible
                   to reach the destination, or negative infinity if there is a
                   negative cycle.
        """
        dist = [INF] * self.n
        dist[origin] = 0

        for _ in range(self.n - 1):
            for u, v, w in self.edges:
                if dist[u] != INF and dist[u] + w < dist[v] and dist[u] + w < limit:
                    dist[v] = dist[u] + w

        # It is impossible to reach the destination
        if dist[destination] == INF:
            return INF

        # Check for negative cycles
        for u, v, w in self.edges:
            if dist[u] != INF and dist[u] + w < dist[v]:
                return NEG_INF

        return dist[destination] if dist[destination] != INF else INF


def main():
    """
    Reads the input, constructs a graph, and determines if it is possible to reach
    the destination vertex within the energy limit.

    """
    n = int(input())

    # Invert the sign of the energy costs to transform the problem of finding
    # the longest path into a shortest path problem using the Bellman-Ford algorithm
    energy_costs = [-int(x) for x in input().split()]

    graph = Graph(n=n, vertices_cost=energy_costs)

    m = int(input())
    for _ in range(m):
        u, v = map(int, input().split())
        graph.add_edge(u, v)

    result_cost = -graph.bellman_ford(origin=0, destination=graph.n - 1, limit=INITIAL_ENERGY)
    if result_cost + INITIAL_ENERGY <= 0:
        print(FAILURE)
    else:
        print(SUCCESS)


if __name__ == "__main__":
    main()
