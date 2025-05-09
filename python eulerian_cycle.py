from collections import defaultdict

def eulerian_cycle(graph):
    def find_cycle(node):
        cycle = []
        while graph[node]:
            neighbor = graph[node].pop()
            find_cycle(neighbor)
        cycle.append(node)
        eulerian_cycle.append(node)

    eulerian_cycle = []
    for node in graph:
        find_cycle(node)

    
    eulerian_cycle.reverse()
    return eulerian_cycle

# Sample Input
input_data = [
    "0: 3",
    "1: 0",
    "2: 1 6",
    "3: 2",
    "4: 2",
    "5: 4",
    "6: 5 8",
    "7: 9",
    "8: 7",
    "9: 6"
]


graph = defaultdict(list)
for line in input_data:
    node, neighbors = line.split(":")
    node = int(node)
    neighbors = list(map(int, neighbors.split()))
    graph[node] = neighbors

# Find the Eulerian cycle
eulerian_cycle_result = eulerian_cycle(graph)

# Convert the result to a space-separated string
eulerian_cycle_str = " ".join(map(str, eulerian_cycle_result))
print(eulerian_cycle_str)
