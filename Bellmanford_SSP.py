class Graph:
    def __init__(self, num_vertices):
        self.V = num_vertices
        self.nodes = []
        self.graph = []

    def addNode(self, value):
        self.nodes.append(value)

    def add_edge(self, s, d, w):
        self.graph.append([s, d, w])

    def bellmanFord(self, initial):
        dist = {i: float("Inf") for i in self.nodes}
        dist[initial] = 0
        path = {}
        for _ in range(self.V - 1):
            for s, d, w in self.graph:
                if dist[s] != float("Inf") and dist[s] + w < dist[d]:
                    dist[d] = dist[s] + w
                    path[d] = s

        for s, d, w in self.graph:
            if dist[s] != float("Inf") and dist[s] + w < dist[d]:
                print("The graph contains negative cycle")
                return
        return dist, path


g = Graph(5)
g.addNode("A")
g.addNode("B")
g.addNode("C")
g.addNode("D")
g.addNode("E")
g.add_edge("A", "C", 6)
g.add_edge("A", "D", 6)
g.add_edge("B", "A", 3)
g.add_edge("C", "D", 1)
g.add_edge("D", "C", 2)
g.add_edge("D", "B", 1)
g.add_edge("E", "B", 4)
g.add_edge("E", "D", 2)
cost, paths = g.bellmanFord("E")


def path_construction(path):
    for i in path.keys():
        while path[i][-1] != 'E':
            path[i] += '<-' + path[path[i][-1]]


path_construction(paths)

print(cost)
print(paths)
