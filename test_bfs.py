from graph import Graph
from bfs import BFS

matrix = [
[0, 1, 0, 1, 1],
[1, 0, 1, 0, 1],
[0, 1, 0, 0, 1],
[1, 0, 0, 0, 1],
[1, 1, 1, 1, 0]
]

G = BFS(matrix=matrix, si=3)
print(G)