from typing import Iterable
from enum import Enum

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
    d: int
    f: int
    p: int
    color: Color
    def __init__(self, index: int) -> None:
        self.index = index
        self.color = Color.WHITE
    def __hash__(self) -> int:
        return self.index

class Graph:
    tick: int
    vertices: dict[int, Vertex]
    adjMatrix: AdjMatrix
    adj: dict[Index, list[Index]]

    def __init__(self, adjMatrix: AdjMatrix) -> None:
        self.tick = 0
        self.vertices = dict()
        self.adj = dict()
        self.adjMatrix = adjMatrix
        for i, line in enumerate(adjMatrix):
            # creating new vertex
            v = Vertex(i)
            self.vertices[i] = v
            adjacents = []
            self.adj[i] = adjacents
            for j,_ in enumerate(line):
                weight = adjMatrix[i][j]
                if weight != 0:
                    adjacents.append(j)
    
    # returns the vertices that are adjacent 
    def Adj(self, i: Vertex) -> Iterable[Vertex]:
        for j in self.adj[i.index]:
            yield self.vertices[j]

    def Weight(self, u: Vertex, v: Vertex) -> Weight:
        return self.adjMatrix[u.index][v.index]
        