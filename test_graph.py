from graph import Graph


def test_graph():
    matrix = [
    [0, 1, 0, 3, 4],
    [1, 0, 3, 0, 6],
    [0, 3, 0, 7, 8],
    [3, 0, 7, 0, 1],
    [4, 6, 8, 1, 0]
    ]

    G = Graph(adjMatrix=matrix)
    print(G)

test_graph()