# The adjacency matrix of an undirected graph is symmetric
# The adjacency matrix of an directed graph is asymmetric
import numpy as np

from graph.GraphBase import GraphBase


class AdjacencyMatrixGraph(GraphBase):
    def __init__(self, num_vertices, directed=False):
        super(AdjacencyMatrixGraph, self).__init__(num_vertices, directed)
        self.matrix = np.zeros((num_vertices, num_vertices))

    def get_edge_weight(self, v1, v2):
        return self.matrix[v1][v2]

    def display(self):
        for i in range(self.num_vertices):
            for v in self.get_adjacent_vertices(i):
                print(f"{i} --> {v}")

    def get_adjacent_vertices(self, v):
        if v < 0 or v >= self.num_vertices:
            raise ValueError(f"Cannot access vertex {v}")

        adjacent_vertices = []
        for i in range(self.num_vertices):
            if self.matrix[v][i] > 0:
                adjacent_vertices.append(i)

        return adjacent_vertices

    def add_edge(self, v1, v2, weight=1):
        if v1 >= self.num_vertices or v2 >= self.num_vertices or v1 < 0 or v2 < 0:
            raise ValueError(f"Vertices {v1} and {v2} are out of bounds")

        if weight < 1:
            raise ValueError("An edge cannot have weight < 1")

        self.matrix[v1][v2] = weight

        if not self.directed:
            self.matrix[v2][v1] = weight

    def get_indegree(self, v):
        if v < 0 or v >= self.num_vertices:
            raise ValueError(f"Cannot access vertex {v}")

        indegree = 0
        for i in range(self.num_vertices):
            if self.matrix[i][v] > 0:
                indegree += 1

        return indegree

