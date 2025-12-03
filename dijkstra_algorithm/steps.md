Steps to Implement Dijkstra's Shortest Path Algorithm

Step 1: Define the infinity constant
- Set INF = float('inf') to represent infinite distance

Step 2: Create the adjacency matrix
- Define adj_matrix as a 2D list representing the graph weights

Step 3: Define the main function
- Create shortest_path function with parameters: matrix, start_node, target_node=None

Step 4: Get the number of nodes
- Set n = len(matrix)

Step 5: Initialize distances list (initially single element)
- Set distances = [INF]

Step 6: Expand distances list to n elements
- Set distances = [INF] * n

Step 7: Set distance to start node
- Set distances[start_node] = 0

Step 8: Initialize paths list
- Set paths = [[node_no] for node_no in range(n)]

Step 9: Initialize visited list
- Set visited = [False] * n

Step 10: Start main algorithm loop
- For _ in range(n): set min_distance = INF, current = -1

Step 11: Find unvisited node with smallest distance
- For node_no in range(n): pass (placeholder for finding minimum)

Step 12: Check if node is valid candidate
- If not visited[node_no] and distances[node_no] < min_distance: pass

Step 13: Update minimum tracking variables
- Set min_distance = distances[node_no], current = node_no

Step 14: Break if no valid node found
- If current == -1: break

Step 15: Mark current node as visited
- Set visited[current] = True

Step 16: Iterate through all nodes for neighbors
- For node_no in range(n): set distance = matrix[current][node_no]

Step 17: Check if valid neighbor
- If distance != INF and not visited[node_no]: set new_distance = distances[current] + distance

Step 18: Update distance if shorter path found
- If new_distance < distances[node_no]: set distances[node_no] = new_distance

Step 19: Update path if shorter path found
- Set paths[node_no] = paths[current] + [node_no]

Step 20: Determine target nodes to display
- Set targets = [target_node] if target_node is not None else range(n)

Step 21: Loop through target nodes
- For node_no in targets: pass

Step 22: Skip invalid targets
- If node_no == start_node or distances[node_no] == INF: continue

Step 23: Convert path to string representation
- Set string_path = (str(n) for n in paths[node_no])

Step 24: Join path strings
- Set path = ' -> '.join(string_path)

Step 25: Print results
- Print formatted distance and path

Step 26: Return results
- Return distances, paths

Step 27: Demonstrate the function
- Call shortest_path(adj_matrix, 0, 5)
