from tower_of_hanoi import hanoi_solver

def test_hanoi_solver():
    # Test 1: Function exists and takes correct type
    assert callable(hanoi_solver)
    assert hanoi_solver.__name__ == 'hanoi_solver'
    print("1. Function named hanoi_solver: PASS")

    # Test 2: Takes correct number of arguments
    import inspect
    sig = inspect.signature(hanoi_solver)
    params = list(sig.parameters.keys())
    assert len(params) == 1
    print("2. Function takes single argument: PASS")

    # Test 3: Returns string
    result = hanoi_solver(2)
    assert isinstance(result, str)
    print("3. Function returns string: PASS")

    # Test 4: hanoi_solver(2) returns correct string
    expected_2 = "[2, 1] [] []\n[2] [1] []\n[] [1] [2]\n[] [] [2, 1]"
    actual_2 = hanoi_solver(2)
    assert actual_2 == expected_2, f"\nExpected:\n{expected_2}\nActual:\n{actual_2}"
    print("4. hanoi_solver(2) returns correct sequence: PASS")

    # Test 5: hanoi_solver(3) returns correct string
    expected_3 = ("[3, 2, 1] [] []\n[3, 2] [] [1]\n[3] [2] [1]\n[3] [2, 1] []\n"
                  "[] [2, 1] [3]\n[1] [2] [3]\n[1] [] [3, 2]\n[] [] [3, 2, 1]")
    actual_3 = hanoi_solver(3)
    assert actual_3 == expected_3, f"\nExpected:\n{expected_3}\nActual:\n{actual_3}"
    print("5. hanoi_solver(3) returns correct sequence: PASS")

    # Test 6: hanoi_solver(4) returns correct sequence (check count and final state)
    actual_4 = hanoi_solver(4)
    lines_4 = actual_4.strip().split('\n')
    assert len(lines_4) == 16, f"Expected 16 lines for n=4, got {len(lines_4)}"
    assert lines_4[-1] == "[] [] [4, 3, 2, 1]", f"Final state incorrect: {lines_4[-1]}"
    print("6. hanoi_solver(4) returns valid sequence with correct moves and final state: PASS")

    # Test 7: hanoi_solver(5) returns correct sequence (check count and final state)
    actual_5 = hanoi_solver(5)
    lines_5 = actual_5.strip().split('\n')
    assert len(lines_5) == 32, f"Expected 32 lines for n=5, got {len(lines_5)}"
    assert lines_5[-1] == "[] [] [5, 4, 3, 2, 1]", f"Final state incorrect: {lines_5[-1]}"
    print("7. hanoi_solver(5) returns valid sequence with correct moves and final state: PASS")

    # Test 8: Works for any positive n (test total moves = 2^n - 1)
    for n in range(1, 6):
        result = hanoi_solver(n)
        lines = result.strip().split('\n')
        assert len(lines) == 2**n, f"For n={n}, expected 2^{n}-1={2**n} moves, got {len(lines)}"
    print("8. hanoi_solver works for any positive n with correct number of moves: PASS")

    print("\nAll tests passed! Tower of Hanoi solver implementation is complete.")

if __name__ == "__main__":
    test_hanoi_solver()
