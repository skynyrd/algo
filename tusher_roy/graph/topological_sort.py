# Explanation: https://youtu.be/ddTC4Zovtbc?list=PLrmLmBdmIlpu2f2g8ltqaaCZiq6GJvl1j
# Time and space complexity: O(n)
from common.graph.Graph import Graph
from common.graph.Vertex import Vertex


def make_it_visited(vertex: Vertex, stack, visited):
    visited.add(vertex.id)

    for adj_vertex in vertex.adjacent_vertices:
        if adj_vertex.id in visited:
            continue

        make_it_visited(adj_vertex, stack, visited)

    stack.append(vertex.id)


def top_sort(graph: Graph):
    stack = []
    visited = set()

    for vertex in graph.all_vertices:
        if vertex in visited:
            continue

        make_it_visited(graph.all_vertices[vertex], stack, visited)

    return stack


if __name__ == "__main__":
    graph = Graph(is_directed=True)
    graph.add_edge(1, 3)
    graph.add_edge(1, 2)
    graph.add_edge(3, 4)
    graph.add_edge(5, 6)
    graph.add_edge(6, 3)
    graph.add_edge(3, 8)
    graph.add_edge(8, 11)

    result_stack = top_sort(graph)

    for _ in range(0, len(result_stack)):
        print(result_stack.pop())
