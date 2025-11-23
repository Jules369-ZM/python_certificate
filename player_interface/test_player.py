import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from player import Player, Pawn
import random

def test_player_abstract():
    # Test that Player is abstract
    try:
        p = Player()
        print("FAIL: Player should be abstract")
        return False
    except TypeError:
        print("PASS: Player is abstract")
        return True

def test_player_init():
    # Test Pawn initialization (can't test Player directly since abstract)
    pawn = Pawn()
    assert pawn.moves == [(0, 1), (0, -1), (1, 0), (-1, 0)], f"Expected moves, got {pawn.moves}"
    assert pawn.position == (0, 0), f"Expected position (0,0), got {pawn.position}"
    assert pawn.path == [(0, 0)], f"Expected path [(0,0)], got {pawn.path}"
    print("PASS: Player/Pawn initialization")
    return True

def test_pawn_moves():
    # Test that Pawn has the correct initial moves
    pawn = Pawn()
    expected_moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    assert pawn.moves == expected_moves, f"Expected {expected_moves}, got {pawn.moves}"
    print("PASS: Pawn initial moves")
    return True

def test_make_move():
    # Test make_move functionality
    random.seed(42)  # For reproducible results
    pawn = Pawn()
    initial_pos = pawn.position
    new_pos = pawn.make_move()
    assert new_pos != initial_pos, "Position should have changed"
    assert len(pawn.path) == 2, f"Path should have 2 positions, got {len(pawn.path)}"
    assert pawn.path[-1] == new_pos, "Last path position should match returned position"
    print("PASS: make_move functionality")
    return True

def test_level_up():
    # Test level_up adds diagonal moves
    pawn = Pawn()
    initial_moves = len(pawn.moves)
    pawn.level_up()
    diagonal_moves = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
    for move in diagonal_moves:
        assert move in pawn.moves, f"Missing diagonal move: {move}"
    assert len(pawn.moves) == initial_moves + 4, "Should have added 4 diagonal moves"
    print("PASS: level_up adds diagonal moves")
    return True

def run_tests():
    tests = [
        test_player_abstract,
        test_player_init,
        test_pawn_moves,
        test_make_move,
        test_level_up,
    ]

    passed = 0
    for test in tests:
        try:
            if test():
                passed += 1
        except Exception as e:
            print(f"FAIL: {test.__name__} - {e}")

    print(f"\nPassed {passed}/{len(tests)} tests")
    return passed == len(tests)

if __name__ == "__main__":
    success = run_tests()
    sys.exit(0 if success else 1)
