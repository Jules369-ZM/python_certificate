# Bisection Method for Square Root

This folder contains an implementation of the bisection method (also known as binary search method) for finding square roots of positive real numbers.

## Overview

The bisection method finds roots of continuous functions by repeatedly bisecting an interval and selecting the subinterval where the function changes sign. For square root calculation, we find `x` such that `x² = target` (or equivalently, solve `x² - target = 0`).

## Function Signature

```python
def square_root_bisection(square_target, tolerance=1e-7, max_iterations=100)
```

### Parameters
- `square_target`: The number for which to find the square root (must be non-negative)
- `tolerance`: Acceptable error margin (default: 1e-7)
- `max_iterations`: Maximum number of iterations (default: 100)

### Returns
- For valid inputs: The approximate square root value
- For convergence failure: `None`

### Raises
- `ValueError`: When `square_target` is negative

## Algorithm

1. **Input validation**: Check for negative numbers
2. **Special cases**: Handle 0 and 1 directly
3. **Initialization**: Set bounds `[low, high]` where `low = 0` and `high = max(1, square_target)`
4. **Iteration**: While within tolerance and iteration limits:
   - Calculate midpoint: `mid = (low + high) / 2`
   - Check convergence: `|mid² - target| ≤ tolerance`
   - Adjust bounds: If `mid² > target`, set `high = mid`; else `low = mid`
5. **Termination**: Return result or `None` if convergence fails

## Examples

```python
# Basic usage with defaults
result = square_root_bisection(25)  # Returns ~5.0

# Custom tolerance and iterations
result = square_root_bisection(2, tolerance=1e-10, max_iterations=50)

# Special cases
result = square_root_bisection(0)   # Returns 0
result = square_root_bisection(1)   # Returns 1

# Error case
square_root_bisection(-1)  # Raises ValueError
```

## Output Messages

- **Special cases**: "The square root of {number} is {number}"
- **Approximation**: "The square root of {target} is approximately {result}"
- **Failure**: "Failed to converge within the {max_iterations} iterations"

## Time Complexity

- **Worst case**: O(max_iterations) - bounded by iteration limit
- **Typical case**: O(log₂(1/tolerance)) - logarithmic convergence
- **Space complexity**: O(1) - constant space usage

## Convergence

The method converges linearly but reliably to the true square root within the specified tolerance. The number of iterations needed is approximately `log₂((high-low)/tolerance)`.
