def selection_sort(arr):
    """
    Implement the selection sort algorithm.
    Takes a list of items and sorts them in place from smallest to largest.

    Args:
        arr: List of items to be sorted in place

    Returns:
        The sorted list (same reference, modified in place)
    """
    n = len(arr)
    for i in range(n):
        # Find the minimum element in remaining unsorted array
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # Swap the found minimum element with the first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


if __name__ == '__main__':
    # Test cases
    test_arrays = [
        [3, 6, 8, 10, 1, 2, 1],
        [],
        [5],
        [1, 2, 3, 4, 5],
        [5, 4, 3, 2, 1],
        [2, 2, 2, 2],
        [1, 3, 2, 4, 6, 5],
        [33, 1, 89, 2, 67, 245],
        [5, 16, 99, 12, 567, 23, 15, 72, 3]
    ]

    print("Testing Selection Sort Algorithm:")
    print("=" * 40)

    for i, arr in enumerate(test_arrays, 1):
        original = arr[:]
        selection_sort(arr)
        print(f"Test {i}: {original} -> {arr}")
