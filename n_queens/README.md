# N-Queens Problem Solver

This module implements a solution to the N-Queens problem using depth-first search with backtracking.

## Problem Description

The N-Queens problem requires placing N queens on an N×N chessboard such that no two queens threaten each other. This means no two queens can share the same row, column, or diagonal.

## Function Description

`dfs_n_queens(n)` solves the N-Queens problem for a given board size n.

- **Input:** `n` (int) - The size of the chessboard
- **Output:** List of solutions, where each solution is a list of column indices for queen placement in each row

## Algorithm Overview

The solution uses DFS with backtracking:

1. Try to place a queen in each row, starting from row 0
2. For each row, try all possible columns
3. Check if the placement is safe (no conflicts with existing queens)
4. If safe, recursively try to place queens in subsequent rows
5. If a complete solution is found, add it to results
6. Backtrack by trying the next column in the current row

## Example Usage

```python
# 4x4 board - returns 2 solutions
solutions = dfs_n_queens(4)
# Output: [[1, 3, 0, 2], [2, 0, 3, 1]]

# 1x1 board - returns 1 solution
solutions = dfs_n_queens(1)
# Output: [[0]]

# Invalid input
solutions = dfs_n_queens(0)
# Output: []
```

## Visual Representation

For the solution `[1, 3, 0, 2]` on a 4x4 board:

```
. Q . .
. . . Q
Q . . .
. . Q .
```

## Time Complexity

- **Worst case:** O(N!) due to exploring all possible queen placements
- **Average case:** Much better with pruning of invalid paths

## Running the Code

```bash
cd n_queens
python3 n_queens.py
