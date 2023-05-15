import sys


class Graph:
    def __init__(self, vertexNum, edges, nodes):
        self.vertexNum = vertexNum
        self.edges = edges
        self.nodes = nodes
        self.MST = []

    def primsAlgo(self):
        visited = [0] * self.vertexNum
        visited[0] = True
        edgeNum = 0
        while edgeNum < self.vertexNum - 1:
            minimum = sys.maxsize
            for i in range(self.vertexNum):
                if visited[i]:
                    for j in range(self.vertexNum):
                        if not visited[j] and self.edges[i][j]:
                            if minimum > self.edges[i][j]:
                                minimum = self.edges[i][j]
                                s = i
                                d = j
            edgeNum += 1
            self.MST.append([self.nodes[s], self.nodes[d], self.edges[s][d]])
            visited[d] = True


edges = [[0, 10, 20, 0, 0],
         [10, 0, 30, 5, 0],
         [20, 30, 0, 15, 6],
         [0, 5, 15, 0, 8],
         [0, 0, 6, 8, 0]]
nodes = ["A", "B", "C", "D", "E"]
g = Graph(5, edges, nodes)
g.primsAlgo()

print(g.MST)
