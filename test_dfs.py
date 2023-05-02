from dfs import DFS

matrix = [
[0, 1, 0, 1, 1],
[1, 0, 1, 0, 1],
[0, 1, 0, 0, 1],
[1, 0, 0, 0, 1],
[1, 1, 1, 1, 0]
]

G = DFS(matrix=matrix)
print(G)