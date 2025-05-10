# Eulerian Cycle Algorithm

This Python implementation demonstrates the **Eulerian Cycle** algorithm for finding an Eulerian cycle in a directed graph. The algorithm uses Hierholzer's method to find an Eulerian cycle if one exists, where every edge in the graph is visited exactly once.

## Algorithm Overview

An **Eulerian cycle** in a directed graph is a cycle that visits every edge exactly once and returns to the starting node. To find such a cycle, we use Hierholzer's algorithm, which involves:
1. Finding a cycle in the graph by starting from any node.
2. Iteratively finding cycles within the cycle and appending them together to form the Eulerian cycle.

The algorithm works as follows:

1. **Graph Representation**: The graph is represented as an adjacency list where each node points to a list of its neighbors.
2. **Cycle Search**: The algorithm starts from an arbitrary node and explores the graph by following edges until no more edges are available.
3. **Recursive Traversal**: The cycle is built recursively, and any remaining edges are added to the cycle as sub-cycles.

## Python Code

```python
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
```
### Eulerian_cycle
The eulerian_cycle function is the core of the algorithm. It uses a recursive function find_cycle to explore the graph and build the cycle.
The graph is traversed from an arbitrary starting node.
The function explores neighbors, marking each edge as visited by removing it from the adjacency list.
When a cycle is completed, the node is added to the cycle list.

### Helper Functions
find_cycle: A recursive helper function that explores all edges from the current node and builds the cycle.
eulerian_cycle: The main function that initializes the cycle and calls the recursive function for each node in the graph.

### Requirements
Python 3.6 or higher
No external libraries are required.

### Applications
Solving problems related to pathfinding in graphs, such as the Chinese Postman Problem.
Bioinformatics applications involving sequence assembly and reconstruction based on overlapping fragments.

### License
This project is released under the MIT License.
