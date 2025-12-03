def quick_sort(arr):
    """
    Implement the quicksort algorithm.
    Takes a list of integers and returns a new sorted list from least to greatest.

    Args:
        arr: List of integers to be sorted

    Returns:
        A new list containing the same integers in sorted order
    """
    # Base case: arrays with 0 or 1 elements are already sorted
    if len(arr) <= 1:
        return arr[:]

    # Choose pivot (first element)
    pivot = arr[0]

    # Partition the array into three lists
    less_than_pivot = []
    equal_to_pivot = []
    greater_than_pivot = []

    for num in arr:
        if num < pivot:
            less_than_pivot.append(num)
        elif num == pivot:
            equal_to_pivot.append(num)
        else:
            greater_than_pivot.append(num)

    # Recursively sort the sublists and concatenate
    return quick_sort(less_than_pivot) + equal_to_pivot + quick_sort(greater_than_pivot)


if __name__ == '__main__':
    # Test cases
    test_arrays = [
        [3, 6, 8, 10, 1, 2, 1],
        [],
        [5],
        [1, 2, 3, 4, 5],
        [5, 4, 3, 2, 1],
        [2, 2, 2, 2],
        [1, 3, 2, 4, 6, 5]
    ]

    print("Testing Quicksort Algorithm:")
    print("=" * 40)

    for i, arr in enumerate(test_arrays, 1):
        sorted_arr = quick_sort(arr)
        print(f"Test {i}: {arr} -> {sorted_arr}")
