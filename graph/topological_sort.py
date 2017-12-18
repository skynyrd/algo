from queue import Queue

from graph.GraphBase import GraphBase


def topological_sort(graph: GraphBase):
    queue = Queue()
    in_degree_map = {}

    for i in range(graph.num_vertices):
        in_degree_map[i] = graph.get_indegree(i)

        if in_degree_map[i] == 0:
            queue.put(i)

    sorted_list = []
    while not queue.empty():
        vertex = queue.get()
        sorted_list.append(vertex)

        for v in graph.get_adjacent_vertices(vertex):
            in_degree_map[v] = in_degree_map[v] - 1

            if in_degree_map[v] == 0:
                queue.put(v)

    if len(sorted_list) != graph.num_vertices:
        raise ValueError("This graph has a cycle!")

    return sorted_list
