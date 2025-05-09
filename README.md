# Eulerian Cycle Finder

This repository provides a Python implementation for finding an **Eulerian cycle** in a directed graph using a recursive depth-first search approach.

An **Eulerian cycle** is a path in a graph that visits every edge exactly once and returns to the starting node. This implementation assumes that the input graph meets the necessary conditions for an Eulerian cycle (i.e., each node has equal in-degree and out-degree, and the graph is strongly connected).

## Algorithm

- The graph is represented as an adjacency list (dictionary of lists).
- A recursive helper function `find_cycle` is used to explore paths and construct the cycle.
- The cycle is built in reverse order and then reversed to produce the correct sequence.

##  Input Format

The input is hardcoded in the script as a list of strings. Each string represents a node and its outgoing edges in the format:

