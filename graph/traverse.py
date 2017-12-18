from queue import Queue

from graph.GraphBase import GraphBase


def breadth_first(graph: GraphBase, start=0):
    queue = Queue()
    queue.put(start)

    visited = [0 for i in range(graph.num_vertices)]

    while not queue.empty():
        vertex = queue.get()

        if visited[vertex] == 1:
            continue

        print(f"Visit: {vertex}")
        visited[vertex] = 1

        for v in graph.get_adjacent_vertices(vertex):
            if visited[v] != 1:
                queue.put(v)


def depth_first(graph, visited, current=0):
    if visited[current] == 1:
        return

    visited[current] = 1

    print(f"Visit: {current}")

    for vertex in graph.get_adjacent_vertices(current):
        depth_first(graph, visited, vertex)
