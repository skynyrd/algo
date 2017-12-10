from typing import List

from common.graph.Edge import Edge
from common.graph.Vertex import Vertex


class Graph(object):
    def __init__(self, is_directed):
        self.all_edges: List[Edge] = []
        self.all_vertices = {}
        self.is_directed = is_directed

    def add_edge(self, id1, id2, weight=0):
        if id1 in self.all_vertices:
            vertex1 = self.all_vertices[id1]
        else:
            vertex1 = Vertex(id1)
            self.all_vertices[id1] = vertex1

        if id2 in self.all_vertices:
            vertex2 = self.all_vertices[id2]
        else:
            vertex2 = Vertex(id2)
            self.all_vertices[id2] = vertex2

        edge = Edge(vertex1, vertex2, self.is_directed, weight)

        self.all_edges.append(edge)
        vertex1.add_adjacent_vertex(edge, vertex2)

        if self.is_directed is not True:
            vertex2.add_adjacent_vertex(edge, vertex1)
