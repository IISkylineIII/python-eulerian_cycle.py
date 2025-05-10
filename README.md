Eulerian Cycle Finder
This repository provides a Python implementation for finding Eulerian cycles in directed graphs using a recursive depth-first search (DFS) approach.

An Eulerian cycle is a path in a graph that visits every edge exactly once and returns to the starting node. For a directed graph to contain an Eulerian cycle, it must satisfy the following conditions:

The graph must be strongly connected.

Each node must have equal in-degree and out-degree.

How It Works
The graph is represented as an adjacency list using defaultdict(list).

The function eulerian_cycle starts from a given node and builds the cycle recursively using a helper function find_cycle.

The cycle is built in reverse and then reversed at the end to produce the correct order.

Input Format
The input is hardcoded in the script as a list of strings. Each string defines a node and its outgoing edges in the format:

"node: neighbor1 neighbor2 ..."
Example:

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
Running the Script
When you run the script, the Eulerian cycle will be printed as a space-separated sequence of node IDs.
python eulerian_cycle.py
Example output:

9 8 7 6 5 4 3 2 1 0 3 2 6 8 7 9 6 5 4 2 1 0

Requirements
Python 3.x

Uses only Python standard libraries (collections)

License
This project is licensed under the MIT License.
