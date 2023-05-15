import DisjointSet as dst


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []
        self.nodes = []
        self.MST = []

    def addEdge(self, s, d, w):
        self.graph.append([s, d, w])

    def addNode(self, value):
        self.nodes.append(value)

    def kruskalAlgo(self):
        graph = sorted(self.graph, key=lambda item: item[2])
        ds = dst.DisjointSet(self.nodes)
        selected_edge_num = 0
        while selected_edge_num < self.V - 1:
            for s, d, w in graph:
                s_root = ds.find(s)
                d_root = ds.find(d)
                if s_root != d_root:
                    self.MST.append([s, d, w])
                    selected_edge_num += 1
                    ds.union(s_root, d_root)


g = Graph(5)
g.addNode("A")
g.addNode("B")
g.addNode("C")
g.addNode("D")
g.addNode("E")
g.addEdge("A", "B", 5)
g.addEdge("A", "C", 13)
g.addEdge("A", "E", 15)
g.addEdge("B", "A", 5)
g.addEdge("B", "C", 10)
g.addEdge("B", "D", 8)
g.addEdge("C", "A", 13)
g.addEdge("C", "B", 10)
g.addEdge("C", "E", 20)
g.addEdge("C", "D", 6)
g.addEdge("D", "B", 8)
g.addEdge("D", "C", 6)
g.addEdge("E", "A", 15)
g.addEdge("E", "C", 20)

g.kruskalAlgo()

print(g.MST)