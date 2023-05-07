from typing import Iterable, Tuple
from enum import Enum
from sys import maxsize

class Index(int):
    pass

class Weight(int):
    pass

class AdjMatrix(list[list[Weight]]):
    pass

class Color(Enum):
    WHITE = 0
    BLACK = 1
    GRAY = 2

class Vertex:
    index: int
    d: int # distance
    f: int
    p: int
    color: Color
    def __init__(self, index: int) -> None:
        self.index = index
        self.color = Color.WHITE
    def __hash__(self) -> int:
        return self.index
    def __lt__(self, other):
        return self.d < other.d
    
    def WasVisited(self) -> bool:
        return self.color != Color.WHITE

class Edge:
    vertices: Tuple[Vertex, Vertex]
    w: Weight
    def __hash__(self) -> int:
        return self.vertices[0].index + self.vertices[1].index * 100000
    def __init__(self, ui: Vertex, vi: Vertex) -> None:
        if ui.index > vi.index:
            self.index = (vi, ui)
        elif vi.index > ui.index:
            self.index = (ui, vi)
        else:
            raise Exception
    
    def GetIndex(u: Vertex, v: Vertex) -> int:
        e = Edge(ui=u, vi=v)
        return hash(e)

class Graph:
    tick: int
    V: dict[int, Vertex]
    edges: dict[int, Edge]
    adjMatrix: AdjMatrix
    adj: dict[Index, list[Index]]

    def __init__(self, adjMatrix: AdjMatrix) -> None:
        self.tick = 0
        self.V = dict()
        self.adj = dict()
        self.edges = dict()
        self.adjMatrix = adjMatrix
        for i, line in enumerate(adjMatrix):
            # creating new vertex
            v = Vertex(i)
            self.V[i] = v
            adjacents = []
            self.adj[i] = adjacents
            for j,_ in enumerate(line):
                weight = adjMatrix[i][j]
                if weight != 0:
                    adjacents.append(j)

    # returns the vertices that are adjacent 
    def Adj(self, i: Vertex) -> Iterable[Vertex]:
        for j in self.adj[i.index]:
            yield self.V[j]

    def Weight(self, u: Vertex, v: Vertex) -> Weight:
        return self.adjMatrix[u.index][v.index]

    def InitializeSingleSource(self, s: Vertex):
        for v in self.V.values():
            v.color = Color.WHITE
            v.d = maxsize
            v.p = None
        s.d = 0
        s.p = None
    
    def CanRelax(self, u: Vertex, v: Vertex) -> bool:
        newDistance = u.d + self.Weight(u, v)
        return v.d > newDistance

    def Relax(self, u: Vertex, v: Vertex) -> bool:
        newDistance = u.d + self.Weight(u, v)
        if self.CanRelax(u, v):
            v.d = newDistance
            v.p = u
            return True
        return False
