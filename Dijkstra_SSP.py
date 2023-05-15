from collections import defaultdict


class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = defaultdict(list)
        self.distance = {}

    def addNode(self, value):
        self.nodes.add(value)

    def addEdge(self, fromNode, toNode, distance):
        self.edges[fromNode].append(toNode)
        self.distance[(fromNode, toNode)] = distance


def dijkstra(graph, initial):
    visited = {initial: 0}
    path = {}
    nodes = set(graph.nodes)
    while nodes:
        min_node = None
        for node in nodes:
            if node in visited:
                if min_node is None:
                    min_node = node
                elif visited[min_node] > visited[node]:
                    min_node = node
        if min_node is None:
            break
        current_weight = visited[min_node]
        for edges in graph.edges[min_node]:
            if edges not in visited or visited[edges] > current_weight + graph.distance[(min_node, edges)]:
                visited[edges] = current_weight + graph.distance[(min_node, edges)]
                path[edges] = min_node
        nodes.remove(min_node)
    return visited, path


customGraph = Graph()
customGraph.addNode("A")
customGraph.addNode("B")
customGraph.addNode("C")
customGraph.addNode("D")
customGraph.addNode("E")
customGraph.addNode("F")
customGraph.addNode("G")
customGraph.addEdge("A", "B", 2)
customGraph.addEdge("A", "C", 5)
customGraph.addEdge("B", "C", 6)
customGraph.addEdge("B", "D", 1)
customGraph.addEdge("B", "E", 3)
customGraph.addEdge("C", "F", 8)
customGraph.addEdge("D", "E", 4)
customGraph.addEdge("E", "G", 9)
customGraph.addEdge("F", "G", 7)

cost, path = dijkstra(customGraph, "A")
print(path)


def path_construction(path):
    for i in path.keys():
        while path[i][-1] != 'A':
            path[i] += '<-' + path[path[i][-1]]


path_construction(path)

print(cost)
print(path)
