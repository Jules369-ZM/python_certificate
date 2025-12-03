# Nth Fibonacci Number Calculator

This module implements a dynamic programming solution to compute the n-th Fibonacci number efficiently.

## Fibonacci Sequence

The Fibonacci sequence is defined as:
- F(0) = 0
- F(1) = 1
- F(n) = F(n-1) + F(n-2) for n > 1

The sequence begins: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ...

## Function Description

`fibonacci(n)` computes the n-th Fibonacci number using an iterative dynamic programming approach.

- **Input:** `n` (int) - The position in the Fibonacci sequence (0-based)
- **Output:** The n-th Fibonacci number

## Algorithm Overview

The function uses dynamic programming with tabulation (bottom-up approach):

1. Initialize a `sequence` list with the base cases: `[0, 1]`
2. For n = 0 or n = 1, return the corresponding value directly
3. For n >= 2, iteratively build the sequence up to the n-th number
4. Each new number is the sum of the two preceding numbers
5. Return the computed n-th Fibonacci number

## Example Usage

```python
# Basic Fibonacci numbers
fibonacci(0)  # Returns: 0
fibonacci(1)  # Returns: 1
fibonacci(2)  # Returns: 1
fibonacci(3)  # Returns: 2
fibonacci(4)  # Returns: 3
fibonacci(5)  # Returns: 5
fibonacci(10) # Returns: 55
```

## Time Complexity

- **O(n)** - Linear time complexity as we compute each Fibonacci number exactly once

## Space Complexity

- **O(n)** - Space used by the sequence list to store all computed values

## Why Dynamic Programming?

This approach avoids the exponential time complexity of naive recursion by computing each value only once and reusing previously computed results.

## Running the Code

```bash
cd fibonacci
python3 fibonacci.py
