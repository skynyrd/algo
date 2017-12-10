from common.graph.Graph import Graph

g = Graph(is_directed=False)

g.add_edge(1, 2, 10)
g.add_edge(2, 3, 5)
g.add_edge(1, 4, 6)

print(" *** Edges *** ")
for edge in g.all_edges:
    print(edge)


print(" *** Vertices *** ")
for vertex in g.all_vertices:
    print("Vertex: " + str(g.all_vertices[vertex]))

    for edge in g.all_vertices[vertex].edges:
        print("Edge: " + str(edge))
