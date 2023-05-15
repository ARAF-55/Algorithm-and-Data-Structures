class DisjointSet:
    def __init__(self, vertices):
        self.vertices = vertices
        self.parent = {}
        for vertex in self.vertices:
            self.parent[vertex] = vertex
        self.rank = dict.fromkeys(vertices, 0)

    def find(self, item):
        if self.parent[item] == item:
            return item
        else:
            return self.find(self.parent[item])

    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)
        if self.rank[x_root] > self.rank[y_root]:
            self.parent[y_root] = x_root
            if x_root == x:
                self.rank[x_root] += 1
        elif self.rank[y_root] > self.rank[x_root]:
            self.parent[x_root] = y_root
            if y_root == y:
                self.rank[y_root] += 1
        else:
            self.parent[y_root] = x_root
            self.rank[x_root] += 1

# vertices = ["A", "B", "C", "D", "E"]

# ds = DisjointSet(vertices)
# ds.union("A", "B")
# print(ds.find("D"))
