import graph

def BellmanFord(matrix: graph.AdjMatrix, si: graph.Index) -> graph.Graph:
    G = graph.Graph(adjMatrix=matrix)
    s = G.V[si]
    G.InitializeSingleSource(s=s)
    # for e in G.edges.values():
        
