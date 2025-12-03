def square_root_bisection(square_target, tolerance=1e-7, max_iterations=100):
    if square_target < 0:
        raise ValueError("Square root of negative number is not defined in real numbers")

    if square_target == 0 or square_target == 1:
        print(f"The square root of {square_target} is {square_target}")
        return square_target

    # Initialize bounds for bisection
    low = 0
    high = max(1, square_target)

    for iteration in range(max_iterations):
        mid = (low + high) / 2
        if high - low <= tolerance:
            print(f"The square root of {square_target} is approximately {mid}")
            return mid
        elif mid * mid > square_target:
            high = mid
        else:
            low = mid

    print(f"Failed to converge within {max_iterations} iterations")
    return None

# Test cases
if __name__ == "__main__":
    # Test negative number
    try:
        square_root_bisection(-1)
    except ValueError as e:
        print(f"Error: {e}")

    # Test 0
    print("Test 0:")
    result = square_root_bisection(0)
    print(f"Returned: {result}\n")

    # Test 1
    print("Test 1:")
    result = square_root_bisection(1)
    print(f"Returned: {result}\n")

    # Test 0.001
    print("Test 0.001:")
    result = square_root_bisection(0.001, 1e-7, 50)
    print(f"Returned: {result}\n")

    # Test 0.25
    print("Test 0.25:")
    result = square_root_bisection(0.25, 1e-7, 50)
    print(f"Returned: {result}\n")

    # Test 81
    print("Test 81:")
    result = square_root_bisection(81, 1e-3, 50)
    print(f"Returned: {result}\n")

    # Test 225 with different tolerances
    print("Test 225 (1e-3):")
    result = square_root_bisection(225, 1e-3, 100)
    print(f"Returned: {result}\n")

    print("Test 225 (1e-5):")
    result = square_root_bisection(225, 1e-5, 100)
    print(f"Returned: {result}\n")

    print("Test 225 (1e-7):")
    result = square_root_bisection(225, 1e-7, 100)
    print(f"Returned: {result}\n")

    # Test convergence failure
    print("Test 225 (1e-7, 10 iterations - should fail):")
    result = square_root_bisection(225, 1e-7, 10)
    print(f"Returned: {result}\n")
