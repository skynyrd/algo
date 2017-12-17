from graph.AdjacencyMatrixGraph import AdjacencyMatrixGraph
from graph.AdjacencySetGraph import AdjacencySetGraph

# graph = AdjacencyMatrixGraph(4, directed=False)
# graph = AdjacencyMatrixGraph(4, directed=True)
graph = AdjacencySetGraph(4, directed=False)
# graph = AdjacencySetGraph(4, directed=True)

graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(2, 3)

for i in range(4):
    print(f"Adjacent to {i} {graph.get_adjacent_vertices(i)}")

for i in range(4):
    print(f"Indegree: {i} {graph.get_indegree(i)}")

for i in range(4):
    for j in graph.get_adjacent_vertices(i):
        print(f"Edge weight: {i} {j} weight: {graph.get_edge_weight(i,j)}")


graph.display()
