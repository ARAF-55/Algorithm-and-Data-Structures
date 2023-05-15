class Graph:
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict

    def bfs(self, start, end):
        queue = [[start]]
        visited = [start]
        while queue:
            path = queue.pop(0)
            node = path[-1]
            if node == end:
                return path
            for adjacent_vertex in self.gdict.get(node, []):
                if adjacent_vertex not in visited:
                    new_path = path.copy()
                    new_path.append(adjacent_vertex)
                    queue.append(new_path)


customDict = {"a": ["b", "c"],
              "b": ["d", "g"],
              "c": ["d", "e"],
              "d": ["f"],
              "e": ["f"],
              "g": ["f"]
              }

g = Graph(customDict)
print(g.bfs("a", "g"))
