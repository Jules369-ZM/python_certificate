# Binary Search Algorithm Workshop

This folder contains a step-by-step implementation of a binary search algorithm that tracks the search path.

## Steps Overview

**Step 1:** Create a `binary_search` function with `search_list` and `value` parameters, containing `pass` initially.

**Step 2:** Initialize `path_to_target` as an empty list to track the search path.

**Step 3:** Initialize `low = 0` and `high = len(search_list) - 1` for search boundaries.

**Step 4:** Create a while loop that continues while `low <= high`.

**Step 5:** Calculate `mid = (low + high) // 2` for the middle index.

**Step 6:** Get `value_at_middle = search_list[mid]`.

**Step 7:** Append `value_at_middle` to `path_to_target` to track the path.

**Step 8:** Check if `value == value_at_middle`, return `path_to_target` and success message with index.

**Step 9:** Add `break` after the if statement for initial testing (later removed).

**Step 10:** Add test calls: `binary_search([1, 2, 3, 4, 5], 3)` and `binary_search([1, 2, 3, 4, 5, 9], 4)`.

**Step 11:** Add `elif value > value_at_middle:` with `pass` placeholder.

**Step 12:** Replace `pass` in elif with `low = mid + 1` to search right half.

**Step 13:** Replace `pass` in else with `high = mid - 1` to search left half.

**Step 14:** Add test call for not found: `binary_search([1, 3, 5, 9, 14, 22], 10)`.

**Step 15:** Update return for not found to include message: `([], "Value not found")`.

**Step 16:** Update found return to include index: `(path_to_target, f"Value found at index {mid}")`.

## Algorithm Explanation

The binary search algorithm efficiently finds a target value in a sorted list by repeatedly dividing the search space in half. This implementation tracks the path taken during the search and returns both the path and a status message with the index when found.

## Usage

```python
result = binary_search([1, 2, 3, 4, 5], 3)
# Returns: ([3], 'Value found at index 2')

result = binary_search([1, 3, 5, 9, 14, 22], 10)
# Returns: ([], 'Value not found')
```

## Time Complexity

- **Best Case:** O(1) - when the target is at the middle
- **Worst Case:** O(log n) - when the target is at the ends or not present
- **Average Case:** O(log n)

The algorithm requires the input list to be sorted.
