# -*- coding: utf-8 -*-

n = int(input())
seq = {i + 1: int(x) for i, x in enumerate(input().split())}

ans = {i: [] for i in range(1, n + 1)}

def sort_graph(sequence: map) -> list:
    """
    Sorts a dictionary-like sequence of (node, degree) pairs in descending
    order by degree and returns a list of nodes that have a degree not equal to zero.

    Args:
        sequence (map): A dictionary-like sequence of (node, degree) pairs.

    Returns:
        list: A list of nodes that have a degree not equal to zero, sorted in
              descending order by their degrees.

    Example:
        >>> graph = {"A": 3, "B": 0, "C": 2, "D": 1}
        >>> sort_graph(graph)
        ['A', 'C', 'D']
    """
    sorted_list = sorted(sequence.items(), 
                         key=lambda item: item[1], 
                         reverse=True)
    return [i[0] for i in sorted_list if i[1] != 0]

def build_graph(sequence: map, adjacency_list: map) -> tuple:
    """
    Builds a graph from a dictionary-like sequence of (node, degree) pairs and an
    adjacency list, and returns a tuple containing the updated sequence and the
    adjacency list.

    The function iteratively adds edges between the nodes with the highest degree
    until it cannot add any more edges or there are no nodes left to add edges to.

    Args:
        sequence (map): A dictionary-like sequence of (node, degree) pairs.
        adjacency_list (map): A dictionary-like adjacency list representing the graph.

    Returns:
        tuple: A tuple containing the updated sequence and the updated adjacency
               list.

    Example:
        >>> sequence = {"A": 3, "B": 2, "C": 1, "D": 0}
        >>> adjacency_list = { "A": [], "B": [], "C": [], "D": [] }
        >>> build_graph(sequence, adjacency_list)
        ({'A': 1, 'B': 0, 'C': 0, 'D': 0}, {'A': ['B', 'C'], 'B': ['A'], 'C': ['A'], 'D': []})
    """
    sequence_list = sort_graph(sequence)
    
    if len(sequence_list) <= 1:
        return (sequence, adjacency_list)

    node_a = sequence_list[0]

    for node_b in sequence_list[1:]:
        if sequence[node_a] == 0:
            break

        if sequence[node_b]:
            adjacency_list[node_a].append(node_b)
            sequence[node_a] -= 1

            adjacency_list[node_b].append(node_a)
            sequence[node_b] -= 1

    if sequence[node_a] != 0:
        return (sequence, adjacency_list)

    return build_graph(sequence, adjacency_list)

seq, ans = build_graph(seq, ans)

if not all(x == 0 for x in seq.values()):
    print("Não é sequência gráfica!")
else:
    for v in ans.values():
        print(" ".join(map(str, v)))
