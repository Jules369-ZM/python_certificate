# Selection Sort Algorithm Implementation

This directory contains an implementation of the Selection Sort algorithm in Python.

## Overview

Selection sort is a simple comparison-based sorting algorithm. It works by repeatedly finding the smallest element from the unsorted portion of the list and swapping it with the first unsorted element. This process continues until the entire list is sorted.

## Algorithm Steps

1. **Start with the first element**: Consider the first element as the minimum
2. **Find the minimum**: Scan the remaining unsorted portion to find the actual minimum element
3. **Swap**: Swap the found minimum element with the first unsorted element
4. **Repeat**: Move to the next position and repeat steps 1-3 until the list is sorted

## Implementation Details

- **Function**: `selection_sort(arr)` - takes a list and sorts it in place, returning the sorted list
- **Time Complexity**: O(n²) in all cases (best, average, and worst)
- **Space Complexity**: O(1) - sorts in place with constant extra space
- **Stability**: Not stable (relative order of equal elements may change)

## Usage

```python
from selection_sort import selection_sort

arr = [33, 1, 89, 2, 67, 245]
sorted_arr = selection_sort(arr)
print(sorted_arr)  # [1, 2, 33, 67, 89, 245]
```

## Test Cases

The implementation includes comprehensive test cases covering:
- Mixed unsorted arrays
- Empty arrays
- Single element arrays
- Already sorted arrays
- Reverse sorted arrays
- Arrays with duplicate elements

Run tests with:
```bash
python3 selection_sort.py
