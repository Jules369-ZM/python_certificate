# Depth-First Search Algorithm Implementation

This module implements the Depth-First Search (DFS) algorithm for graph traversal using an adjacency matrix representation.

## Function Description

`dfs(adjacency_matrix, start_node)` performs a depth-first search starting from the given node and returns all reachable nodes.

- **Input:**
  - `adjacency_matrix`: A 2D list where `matrix[i][j] == 1` indicates an edge between nodes i and j
  - `start_node`: Integer representing the starting node (0 to n-1)

- **Output:** List of all nodes reachable from the start_node in DFS order

## Algorithm Overview

DFS explores as far as possible along each branch before backtracking. It uses a stack (LIFO) data structure to keep track of nodes to visit:

1. Start with the given node on the stack
2. While stack is not empty:
   - Pop the top node from stack
   - If not visited, mark as visited and add to result
   - Push all unvisited neighbors onto the stack

## Example Usage

```python
matrix = [
    [0, 1, 0, 1, 0],  # Node 0 connected to 1, 3
    [1, 0, 1, 0, 1],  # Node 1 connected to 0, 2, 4
    [0, 1, 0, 0, 0],  # Node 2 connected to 1
    [1, 0, 0, 0, 1],  # Node 3 connected to 0, 4
    [0, 1, 0, 1, 0]   # Node 4 connected to 1, 3
]

print(dfs(matrix, 0))  # Output: [0, 3, 4, 1, 2]
print(dfs(matrix, 2))  # Output: [2, 1, 4, 3, 0]
```

## Time Complexity

- **O(V + E)** where V is the number of vertices and E is the number of edges

## Running the Code

```bash
cd dfs
python3 dfs.py
