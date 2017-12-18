Use **Adjacency Matrix** if there are not many nodes that connect each other **densely**

* Space required = O(V^2)
* Checking if edge is present = O(1)
* Iterating over edges = O(V)

Use **Adjacency Set** if there are not nodes that connect each other **sparsely**

* Space required = O(E+V)
* Checking if edge is present = O(log(degree V))
* Iterating over edges = O(degree V)


#### Traversing Tree vs Traversing Graph

* One node is designated root - No designated root
* Only one specific path from root to any node - Multiple paths possible between any pair of nodes
* No cycles - Cycles possible
* Any node will be visited exactly once - Nodes could be visited multiple times (could lead to infinite loop)
* No need to track which nodes already visited - Essential to track which nodes already visited
* No unconnected nodes possible - Unconnected nodes possible
* No need to track which nodes already visited - Algorithm can not terminate until all nodes have been visited.

Acyclic (No cycle) directed graph --> Tensorflow, neural networks

Topological sort --> All the nodes are parent or grand parant of upcoming node. "Comes before", all nodes visited

* Algorithm: Add all vertexes to a list, in other array, calculate indegrees. If no indegree, graph is cyclic
and topological sort is not possible. If not print vertex with 0 indegree. Then remove the vertex from the graph, 
and recurse.

* O(V+E) Each edge visited exactly once, each vertex visited exactly once, multiple solutions possible.

