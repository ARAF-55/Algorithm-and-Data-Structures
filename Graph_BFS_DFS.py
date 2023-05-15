class Graph:
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict

    def addEdge(self, vertex, edge):
        self.gdict[vertex].append(edge)

    def bfs(self, starting_vertex):
        visited = []
        queue = []
        visited.append(starting_vertex)
        queue.append(starting_vertex)
        while queue:
            vertex = queue.pop(0)
            print(vertex)
            for adjacent_vertex in self.gdict[vertex]:
                if adjacent_vertex not in visited:
                    visited.append(adjacent_vertex)
                    queue.append(adjacent_vertex)

    def dfs(self, startingVertex, visited=None):
        if visited is None:
            visited = []
        print(startingVertex)
        visited.append(startingVertex)
        for adjacent_vertex in self.gdict[startingVertex]:
            if adjacent_vertex not in visited:
                self.dfs(adjacent_vertex, visited)
        return visited


customDict = {"a": ["b", "c"],
              "b": ["a", "d", "e"],
              "c": ["a", "e"],
              "d": ["b", "e", "f"],
              "e": ["d", "f", "c"],
              "f": ["d", "e"]
              }

g = Graph(customDict)
g.dfs("a")
print("Now let's test the bfs method")
g.bfs("a")
