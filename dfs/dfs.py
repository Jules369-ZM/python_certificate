def dfs(adjacency_matrix, start_node):
    """
    Performs depth-first search on a graph represented as an adjacency matrix.

    Args:
        adjacency_matrix (list): A 2D list representing the adjacency matrix
        start_node (int): The starting node for DFS (0 to n-1)

    Returns:
        list: A list of all nodes reachable from the start_node
    """
    if not adjacency_matrix or start_node < 0 or start_node >= len(adjacency_matrix):
        return []

    n = len(adjacency_matrix)
    visited = [False] * n
    stack = [start_node]
    result = []

    while stack:
        node = stack.pop()
        if not visited[node]:
            visited[node] = True
            result.append(node)

            # Add neighbors to stack in order to match expected DFS traversal
            for neighbor in range(n):
                if adjacency_matrix[node][neighbor] == 1 and not visited[neighbor]:
                    stack.append(neighbor)

    return result


# Example usage
if __name__ == "__main__":
    # Example adjacency matrix for a graph with 5 nodes
    # 0 -- 1 -- 2
    # |    |
    # 3 -- 4
    matrix = [
        [0, 1, 0, 1, 0],  # 0 connected to 1, 3
        [1, 0, 1, 0, 1],  # 1 connected to 0, 2, 4
        [0, 1, 0, 0, 0],  # 2 connected to 1
        [1, 0, 0, 0, 1],  # 3 connected to 0, 4
        [0, 1, 0, 1, 0]   # 4 connected to 1, 3
    ]

    print("DFS from node 0:", dfs(matrix, 0))
    print("DFS from node 2:", dfs(matrix, 2))
