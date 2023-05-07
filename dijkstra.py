from graph import *
import heapq

def Dijkstra(matrix: AdjMatrix, sindex: int):
    G = Graph(matrix)
    s = G.V[sindex]
    G.InitializeSingleSource(s=s)
    Q = []
    heapq.heapify(Q)
    for v in G.V.values():
        heapq.heappush(Q, (v.d, v))
    while len(Q) != 0:
        _, u = heapq.heappop(Q)
        for v in G.Adj(u):
            old_dist = v.d
            hasRelaxed = G.Relax(u=u, v=v)
            if hasRelaxed:
                Q.remove((old_dist, v))
                heapq.heapify(Q)
                heapq.heappush(Q, (v.d, v))
    return G