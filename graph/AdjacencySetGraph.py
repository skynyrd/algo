# Adjacency Linked List Flaws
# Order matters: same graph can have multiple representations, cannot compare exactly.
# Deletion of a node is inefficient
# Each node maintains a linked list of its adjacent nodes
# ............
# Adjacency sets are more afficient, each node maintains a set of its adjacent nodes
from graph.GraphBase import GraphBase


class AdjacencySetGraphNode:
    def __init__(self, vertex_id):
        self.vertex_id = vertex_id
        self.adjacency_set = set()

    def add_edge(self, v):
        if self.vertex_id == v:
            raise ValueError(f"The vertex {v} cannot be adjacent to itself")

        self.adjacency_set.add(v)

    def get_adjacent_vertices(self):
        return sorted(self.adjacency_set)


class AdjacencySetGraph(GraphBase):
    def __init__(self, num_vertices, directed):
        super(AdjacencySetGraph, self).__init__(num_vertices, directed)

        self.vertex_list = []
        for i in range(num_vertices):
            self.vertex_list.append(AdjacencySetGraphNode(i))

    def get_edge_weight(self, v1, v2):
        return 1

    def display(self):
        for i in range(self.num_vertices):
            for v in self.get_adjacent_vertices(i):
                print(f"{i} --> {v}")

    def get_adjacent_vertices(self, v):
        if v < 0 or v >= self.num_vertices:
            raise ValueError(f"Cannot access vertex {v}")

        return self.vertex_list[v].get_adjacent_vertices()

    def add_edge(self, v1, v2, weight=1):
        if v1 >= self.num_vertices or v2 >= self.num_vertices or v1 < 0 or v2 < 0:
            raise ValueError(f"Vertices {v1} and {v2} are out of the bunds")

        if weight != 1:
            raise ValueError("An adjacency set cannot represent edge weights > 1")

        self.vertex_list[v1].add_edge(v2)

        if not self.directed:
            self.vertex_list[v2].add_edge(v1)

    def get_indegree(self, v):
        if v < 0 or v >= self.num_vertices:
            raise ValueError(f"Cannot access vertex {v}")

        indegree = 0
        for i in range(self.num_vertices):
            if v in self.get_adjacent_vertices(i):
                indegree += 1

        return indegree
