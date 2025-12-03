# Adjacency List to Matrix Converter

This module contains a function that converts an adjacency list representation of a graph into an adjacency matrix.

## Function Description

`adjacency_list_to_matrix(adjacency_list)` takes a dictionary representing the adjacency list of an unweighted graph and returns the corresponding adjacency matrix as a 2D list.

- **Input:** Dictionary where keys are nodes and values are lists of connected nodes
- **Output:** 2D list (matrix) where matrix[i][j] = 1 if there's an edge from node i to node j, 0 otherwise
- **Side effect:** Prints each row of the matrix

## Example Usage

```python
adj_list = {0: [2], 1: [2, 3], 2: [0, 1, 3], 3: [1, 2]}
matrix = adjacency_list_to_matrix(adj_list)
# Prints:
# [0, 0, 1, 0]
# [0, 0, 1, 1]
# [1, 1, 0, 1]
# [0, 1, 1, 0]
# Returns: [[0, 0, 1, 0], [0, 0, 1, 1], [1, 1, 0, 1], [0, 1, 1, 0]]
```

## Running the Code

```bash
cd adjacency_list_to_matrix
python3 adjacency_list_to_matrix.py
