class Vertex(object):
    def __init__(self, id):
        self.id = id
        self.edges = []
        self.adjacent_vertices = []

    def add_adjacent_vertex(self, edge, vertex):
        self.edges.append(edge)
        self.adjacent_vertices.append(vertex)

    def get_degree(self):
        return len(self.edges)

    def __eq__(self, other):
        return self.id == other.id

    def __hash__(self):
        return hash(self.id)

    def __str__(self):
        return "Vertex-" + str(self.id)

    def __repr__(self):
        return self.__str__()

    def __lt__(self, other):
        return self.id < other.id

    def __gt__(self, other):
        return self.id > other.id

