from dijkstra import Dijkstra

matrix = [
[0, 5, 0, 1, 8],
[5, 0, 2, 0, 1],
[0, 2, 0, 0, 1],
[1, 0, 0, 0, 1],
[8, 1, 1, 1, 0]
]

G = Dijkstra(matrix=matrix, sindex = 1)
print(G)