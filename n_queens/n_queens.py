def dfs_n_queens(n):
    """
    Solves the N-Queens problem using depth-first search with backtracking.

    Args:
        n (int): The size of the chessboard (n x n)

    Returns:
        list: A list of solutions, where each solution is a list of column indices
              for queen placement in each row (0-based indexing)
    """
    if n < 1:
        return []

    def is_safe(board, row, col):
        """Check if it's safe to place a queen at board[row][col]"""
        # Check column
        for i in range(row):
            if board[i] == col:
                return False

        # Check upper-left diagonal
        for i, j in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
            if board[i] == j:
                return False

        # Check upper-right diagonal
        for i, j in zip(range(row-1, -1, -1), range(col+1, n)):
            if board[i] == j:
                return False

        return True

    def dfs(row, board, result):
        """DFS backtracking function"""
        if row == n:
            # Found a valid solution
            result.append(board[:])
            return

        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col
                dfs(row + 1, board, result)
                # Backtrack is automatic since we modify board in place

    result = []
    board = [-1] * n  # -1 indicates no queen placed yet
    dfs(0, board, result)
    return result


# Example usage
if __name__ == "__main__":
    print("N=1:", dfs_n_queens(1))
    print("N=4:", dfs_n_queens(4))
    print("N=0:", dfs_n_queens(0))
