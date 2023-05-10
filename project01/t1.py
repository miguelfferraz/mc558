# -*- coding: utf-8 -*-

FAIL_MESSAGE = "Não é sequência gráfica!"


def read_sequence() -> tuple:
    """
    Reads a sequence of integers from input and returns the length of the sequence and a dictionary-like
    sequence of (node, degree) pairs.

    Returns:
        tuple: A tuple containing the length of the sequence and a dictionary-like sequence of (node, degree) pairs.
    """
    n = int(input())
    sequence = {i + 1: int(x) for i, x in enumerate(input().split())}
    return n, sequence


def build_adjacency_list(n: int) -> dict:
    """
    Builds an empty adjacency list with n nodes.

    Args:
        n (int): The number of nodes in the graph.

    Returns:
        dict: A dictionary-like adjacency list with n nodes, where each node has an empty list of neighbors.
    """
    return {i: [] for i in range(1, n + 1)}


def sort_graph(sequence: dict) -> list:
    """
    Sorts a dictionary-like sequence of (node, degree) pairs in descending
    order by degree and returns a list of nodes that have a degree not equal to zero.

    Args:
        sequence (dict): A dictionary-like sequence of (node, degree) pairs.

    Returns:
        list: A list of nodes that have a degree not equal to zero, sorted in
              descending order by their degrees.

    Example:
        >>> graph = {"A": 3, "B": 0, "C": 2, "D": 1}
        >>> sort_graph(graph)
        ['A', 'C', 'D']
    """
    sorted_list = sorted(
        sequence.items(), key=lambda item: item[1], reverse=True
    )
    return [node for node, degree in sorted_list if degree != 0]


def build_graph(sequence: dict, adjacency_list: dict) -> tuple:
    """
    Builds a graph from a dictionary-like sequence of (node, degree) pairs and an
    adjacency list, and returns a tuple containing the updated sequence and the
    adjacency list.

    The function iteratively adds edges between the nodes with the highest degree
    until it cannot add any more edges or there are no nodes left to add edges to.

    Args:
        sequence (dict): A dictionary-like sequence of (node, degree) pairs.
        adjacency_list (dict): A dictionary-like adjacency list representing the graph.

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

    start = sequence_list[0]

    for destination in sequence_list[1:]:
        if sequence[start] == 0:
            break

        if sequence[destination]:
            adjacency_list[start].append(destination)
            sequence[start] -= 1

            adjacency_list[destination].append(start)
            sequence[destination] -= 1

    if sequence[start] != 0:
        return (sequence, adjacency_list)

    return build_graph(sequence, adjacency_list)


def main():
    """
    Reads a sequence of degrees from the user and prints the corresponding
    graph, if it exists.

    The function reads the input sequence using the read_sequence() function,
    builds an empty adjacency list using the build_adjacency_list() function,
    and constructs a graph from the input sequence using the build_graph() function.
    If the resulting sequence of degrees is a valid graph degree sequence, the
    function prints the corresponding graph using the adjacency list. Otherwise,
    it prints a message indicating that the sequence is not a valid graph degree
    sequence.
    """
    n, sequence = read_sequence()
    adjacency_list = build_adjacency_list(n)

    sequence, adjacency_list = build_graph(sequence, adjacency_list)

    if all(degree == 0 for degree in sequence.values()):
        for value in adjacency_list.values():
            print(" ".join(map(str, value)))
    else:
        print(FAIL_MESSAGE)


if __name__ == "__main__":
    main()
