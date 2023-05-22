# -*- coding: utf-8 -*-


class Graph:
    def __init__(self, n):
        self.n = n

        self.edges = []

        self.parent = list(range(n))
        self.rank = [0] * n

    def add_edge(self, u, v, cost):
        self.edges.append((u, v, cost))

    def make_set(self, vertex):
        self.parent[vertex] = vertex
        self.rank[vertex] = 0

    def find(self, vertex):
        if self.parent[vertex] != vertex:
            self.parent[vertex] = self.find(self.parent[vertex])
        return self.parent[vertex]

    def union(self, u, v):
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

    def kruskal(self, k):
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


def read_edges(graph, m):
    for _ in range(m):
        a, b, cost = map(int, input().split())
        graph.add_edge(a, b, cost)


def main():
    n, m, k = map(int, input().split())

    graph = Graph(n)
    read_edges(graph, m)

    min_cost = graph.kruskal(k)
    print(min_cost)


if __name__ == "__main__":
    main()
