# Binary Search Algorithm Workshop - Steps 1-16
def binary_search(search_list, value):
    # Step 2: Initialize path_to_target to track the search path
    path_to_target = []
    # Step 3: Initialize low and high boundaries
    low = 0
    high = len(search_list) - 1
    # Step 4: While loop for the search process
    while low <= high:
        # Step 5: Calculate the middle index
        mid = (low + high) // 2
        # Step 6: Get the value at the middle index
        value_at_middle = search_list[mid]
        # Step 7: Append value_at_middle to path_to_target
        path_to_target.append(value_at_middle)
        # Step 8: Check if value is found
        if value == value_at_middle:
            # Step 16: Return path and message with index
            return path_to_target, f"Value found at index {mid}"
        # Step 11: Elif for value > value_at_middle
        elif value > value_at_middle:
            # Step 12: Update low for right half search
            low = mid + 1
        # Step 13: Else for value < value_at_middle, update high for left half search
        else:
            high = mid - 1
    # Step 15: Return empty list and message when not found
    return [], "Value not found"

print(binary_search([1, 2, 3, 4, 5], 3))
print(binary_search([1, 2, 3, 4, 5, 9], 4))
print(binary_search([1, 3, 5, 9, 14, 22], 10))
