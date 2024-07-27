class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_edge(self, u, v):
        if u not in self.adj_list:
            self.adj_list[u] = []
        if v not in self.adj_list:
            self.adj_list[v] = []

        self.adj_list[u].append(v)
        self.adj_list[v].append(u)

    def get_friends(self, u):
        if u in self.adj_list:
            return self.adj_list[u]
        else:
            return []

    def get_common_friends(self, u, v):
        if u in self.adj_list and v in self.adj_list:
            return list(set(self.adj_list[u]) & set(self.adj_list[v]))
        else:
            return []

    def get_distance(self, u, v):
        if u in self.adj_list and v in self.adj_list:
            visited = set()
            queue = [(u, 0)]  # (node, distance)

            while queue:
                node, distance = queue.pop(0)
                visited.add(node)

                if node == v:
                    return distance

                for neighbor in self.adj_list[node]:
                    if neighbor not in visited:
                        queue.append((neighbor, distance + 1))

        return -1  # If u or v is not in the graph or there is no path between them


# Example usage
g = Graph()
g.add_edge("Alice", "Bob")
g.add_edge("Bob", "Charlie")
g.add_edge("Charlie", "Dave")

print(g.get_friends("Alice"))  # Output: ['Bob']
print(g.get_friends("Bob"))  # Output: ['Alice', 'Charlie']
print(g.get_friends("Charlie"))  # Output: ['Bob', 'Dave']
print(g.get_friends("Dave"))  # Output: ['Charlie']

# Test case 1: Adding edges and getting friends
g = Graph()
g.add_edge("Alice", "Bob")
g.add_edge("Bob", "Charlie")
g.add_edge("Charlie", "Dave")

assert g.get_friends("Alice") == ['Bob']
assert g.get_friends("Bob") == ['Alice', 'Charlie']
assert g.get_friends("Charlie") == ['Bob', 'Dave']
assert g.get_friends("Dave") == ['Charlie']

# Test case 2: Getting common friends
assert g.get_common_friends("Alice", "Bob") == []
assert g.get_common_friends("Bob", "Charlie") == []
assert g.get_common_friends("Charlie", "Dave") == []
assert g.get_common_friends("Alice", "Charlie") == ['Bob']
assert g.get_common_friends("Bob", "Dave") == ['Charlie']

# Test case 3: Getting distance between nodes
assert g.get_distance("Alice", "Bob") == 1
assert g.get_distance("Alice", "Charlie") == 2
assert g.get_distance("Alice", "Dave") == 3
assert g.get_distance("Bob", "Dave") == 2
assert g.get_distance("Charlie", "Dave") == 1
assert g.get_distance("Alice", "Eve") == -1

print("All tests passed!")