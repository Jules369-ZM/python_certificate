# Quicksort Algorithm Implementation

This directory contains an implementation of the Quicksort algorithm in Python.

## Overview

Quicksort is a divide-and-conquer sorting algorithm that works by selecting a 'pivot' element from the array and partitioning the other elements into two sub-arrays, according to whether they are less than or greater than the pivot. The sub-arrays are then sorted recursively.

## Algorithm Steps

1. **Choose a pivot**: Select an element from the array (this implementation uses the first element)
2. **Partition**: Create three sublists:
   - Elements less than the pivot
   - Elements equal to the pivot
   - Elements greater than the pivot
3. **Recursively sort**: Apply quicksort to the less-than and greater-than sublists
4. **Concatenate**: Combine the sorted sublists in order

## Implementation Details

- **Function**: `quick_sort(arr)` - takes a list of integers and returns a new sorted list
- **Time Complexity**: Average O(n log n), Worst case O(n²)
- **Space Complexity**: O(n) due to creating new lists
- **Stability**: Not stable (relative order of equal elements may change)

## Usage

```python
from quicksort import quick_sort

arr = [3, 6, 8, 10, 1, 2, 1]
sorted_arr = quick_sort(arr)
print(sorted_arr)  # [1, 1, 2, 3, 6, 8, 10]
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
python3 quicksort.py
