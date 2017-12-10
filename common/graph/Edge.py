from common.graph.Vertex import Vertex


class Edge(object):
    def __init__(self, vertex1: Vertex, vertex2: Vertex, is_directed, weight):
        self.weight = weight
        self.is_directed = is_directed
        self.vertex2 = vertex2
        self.vertex1 = vertex1

    def __eq__(self, other):
        return self.vertex1.id == other.vertex1.id and self.vertex2.id == other.vertex2.id

    def __hash__(self):
        return hash(self.vertex1) + hash(self.vertex2)

    def __str__(self):
        return f"Edge {str(self.vertex1)} {str(self.vertex2)} Weight: {str(self.weight)}"

    def __repr__(self):
        return self.__str__()
