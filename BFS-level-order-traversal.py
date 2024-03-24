from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def bfs(self, start_vertex):
        visited = set()
        queue = []

        queue.append(start_vertex)
        visited.add(start_vertex)

        while queue:
            vertex = queue.pop(0)
            print(vertex, end=" ")

            for neighbour in self.graph[vertex]:
                if neighbour not in visited:
                    queue.append(neighbour)
                    visited.add(neighbour)

# Create a graph
g = Graph()
g.add_edge(1, 2)
g.add_edge(1, 5)
g.add_edge(2, 5)
g.add_edge(2, 3)
g.add_edge(5, 3)
g.add_edge(5, 4)
g.add_edge(3, 4)

print("BFS Traversal (Level Order):")
g.bfs(1)
