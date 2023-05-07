from graph import *

tick = 0

def DFSVisit(G: Graph, u: Vertex) -> None:
    G.tick += 1
    u.d = G.tick
    u.color = Color.GRAY
    for v in G.Adj(u):
        if v.WasVisited():
            v.p = u
            DFSVisit(G, v)
    u.color = Color.BLACK
    G.tick += 1
    u.f = G.tick

def DFS(matrix: AdjMatrix) -> Graph:
    G = Graph(adjMatrix=matrix)
    for v in G.V.values():
        v.color = Color.WHITE
        v.p = None
    G.tick = 0
    for u in G.V.values():
        if u.WasVisited():
            DFSVisit(G, u)

    return G