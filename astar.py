import heapq
class Graph:
    def __init__(self):
        self.adjacency_list = {}
    
    def add_edge(self, node, neighbor, weight):
        if node not in self.adjacency_list:
            self.adjacency_list[node] = []
        self.adjacency_list[node].append((neighbor, weight))
    
    def a_star_search(self, start_node, goal_node, heuristic_func):
        open_list = []
        closed_list = set()
        heapq.heappush(open_list, (0, start_node, []))  # (f(n), node, path)
        
        while open_list:
            f, current_node, path = heapq.heappop(open_list)
            
            if current_node == goal_node:
                return path + [current_node]
            
            if current_node in closed_list:
                continue
            
            closed_list.add(current_node)
            
            for neighbor, weight in self.adjacency_list.get(current_node, []):
                if neighbor not in closed_list:
                    new_path = path + [current_node]
                    g = f - heuristic_func(current_node) + weight  # g(n) = f(n) - h(n) + c(n, neighbor)
                    h = heuristic_func(neighbor)  # h(n)
                    f_new = g + h
                    heapq.heappush(open_list, (f_new, neighbor, new_path))
        
        return None

def heuristic(node):
    # Example heuristic function, assuming goal_node is 'G'
    distances = {'A': 10, 'B': 6, 'C': 5, 'D': 7, 'E': 3, 'F': 1, 'G': 0}
    return distances.get(node, float('inf'))

# Example graph
graph = Graph()
graph.add_edge('A', 'B', 3)
graph.add_edge('A', 'C', 6)
graph.add_edge('B', 'D', 4)
graph.add_edge('B', 'E', 2)
graph.add_edge('C', 'E', 5)
graph.add_edge('D', 'G', 7)
graph.add_edge('E', 'G', 3)
graph.add_edge('F', 'G', 1)

start_node = 'A'
goal_node = 'G'

path = graph.a_star_search(start_node, goal_node, heuristic)
print("Path:", path)
