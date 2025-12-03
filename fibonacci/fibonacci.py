def fibonacci(n):
    """
    Computes the n-th Fibonacci number using dynamic programming.

    Args:
        n (int): A positive integer representing the position in the Fibonacci sequence

    Returns:
        int: The n-th Fibonacci number
    """
    sequence = [0, 1]

    # For n = 0 or n = 1, return the value directly
    if n == 0:
        return sequence[0]
    elif n == 1:
        return sequence[1]

    # Build the sequence up to the n-th number
    for i in range(2, n + 1):
        # Each number is the sum of the two preceding numbers
        next_num = sequence[i-1] + sequence[i-2]
        sequence.append(next_num)

    # Return the n-th Fibonacci number (stored at index n)
    return sequence[n]


# Example usage
if __name__ == "__main__":
    print("fibonacci(0):", fibonacci(0))
    print("fibonacci(1):", fibonacci(1))
    print("fibonacci(2):", fibonacci(2))
    print("fibonacci(3):", fibonacci(3))
    print("fibonacci(4):", fibonacci(4))
    print("fibonacci(5):", fibonacci(5))
    print("fibonacci(10):", fibonacci(10))
