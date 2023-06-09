import graph
import sys
from collections import deque

def BFS(matrix: graph.AdjMatrix, si: graph.Index) -> graph.Graph:
    G = graph.Graph(matrix)
    for i in G.V.keys():
        v = G.V[i]
        v.color = graph.Color.WHITE
        v.d = sys.maxsize
        v.p = None 
    s = G.V[si]
    s.color = graph.Color.GRAY
    s.d = 0
    s.p = None
    Q = deque([s])
    while len(Q) != 0:
        v = Q.pop()
        for u in G.Adj(v):
            if u.WasVisited():
                u.color = graph.Color.GRAY
                u.p = v
                u.d = v.d + G.Weight(u, v)
                Q.append(u)
        v.color = graph.Color.BLACK
    return G


