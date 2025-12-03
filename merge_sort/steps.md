# Merge Sort Implementation Steps

## Step 1: Function Declaration
Created the `merge_sort` function with `array` as a parameter. This function implements the merge sort algorithm recursively.

```python
def merge_sort(array):
```

## Step 10: Array Splitting Logic
Implemented the core splitting logic where the array is divided into two halves using integer division for the middle point.

```python
middle_point = len(array) // 2
left_part = array[:middle_point]
right_part = array[middle_point:]
```

## Step 25: Final Output Display
Added the final output display showing both the unsorted and sorted arrays, completing the merge sort implementation.

```python
if __name__ == '__main__':
    numbers = [4, 10, 6, 14, 2, 1, 8, 5]
    print('Unsorted array: ')
    print(numbers)
    merge_sort(numbers)
    print('Sorted array: ')
    print(numbers)
```

The complete merge sort algorithm successfully sorts arrays using a divide-and-conquer approach with O(n log n) time complexity.
