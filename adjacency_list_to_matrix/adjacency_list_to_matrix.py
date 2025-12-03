def adjacency_list_to_matrix(adjacency_list):
    """
    Converts an adjacency list representation of a graph into an adjacency matrix.

    Args:
        adjacency_list (dict): A dictionary where keys are nodes and values are lists of connected nodes.

    Returns:
        list: A 2D list representing the adjacency matrix.
    """
    # Get all unique nodes from keys and values
    nodes = set(adjacency_list.keys())
    for neighbors in adjacency_list.values():
        nodes.update(neighbors)

    # Sort nodes to ensure consistent ordering
    nodes = sorted(list(nodes))

    # Create mapping from node to index
    node_to_index = {node: i for i, node in enumerate(nodes)}

    # Initialize n x n matrix with 0s
    n = len(nodes)
    matrix = [[0] * n for _ in range(n)]

    # Fill the matrix
    for node, neighbors in adjacency_list.items():
        i = node_to_index[node]
        for neighbor in neighbors:
            j = node_to_index[neighbor]
            matrix[i][j] = 1

    # Print each row of the matrix
    for row in matrix:
        print(row)

    return matrix


# Example usage
if __name__ == "__main__":
    # Test with the first example from the task
    print("Test 1:")
    adj_list1 = {0: [1, 2], 1: [2], 2: [0, 3], 3: [2]}
    print("Adjacency List:", adj_list1)
    print("Adjacency Matrix:")
    matrix1 = adjacency_list_to_matrix(adj_list1)
    print("Returned Matrix:", matrix1)
    print()

    # Test with the second example from the task
    print("Test 2:")
    adj_list2 = {0: [2], 1: [2, 3], 2: [0, 1, 3], 3: [1, 2]}
    print("Adjacency List:", adj_list2)
    print("Adjacency Matrix:")
    matrix2 = adjacency_list_to_matrix(adj_list2)
    print("Returned Matrix:", matrix2)
