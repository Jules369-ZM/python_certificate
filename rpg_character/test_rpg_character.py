from rpg_character import create_character

def test_name_not_string():
    assert create_character(123, 1, 1, 2) == "The character name should be a string"

def test_name_too_long():
    assert create_character("verylongname", 1, 1, 2) == "The character name is too long"

def test_name_has_space():
    assert create_character("test name", 1, 1, 2) == "The character name should not contain spaces"

def test_stats_not_integers():
    assert create_character("test", 1.5, 1, 2) == "All stats should be integers"

def test_stats_below_1():
    assert create_character("test", 0, 1, 2) == "All stats should be no less than 1"

def test_stats_above_4():
    assert create_character("test", 5, 1, 2) == "All stats should be no more than 4"

def test_stats_sum_not_7():
    assert create_character("test", 3, 2, 1) == "The character should start with 7 points"

def test_valid_character():
    expected = "ren\nSTR ●●●●○○○○○○\nINT ●●○○○○○○○○\nCHA ●○○○○○○○○○"
    assert create_character("ren", 4, 2, 1) == expected

def test_valid_character_output():
    expected = "test\nSTR ●●●○○○○○○○\nINT ●●●○○○○○○○\nCHA ●○○○○○○○○○"
    assert create_character("test", 3, 3, 1) == expected

if __name__ == "__main__":
    test_name_not_string()
    test_name_too_long()
    test_name_has_space()
    test_stats_not_integers()
    test_stats_below_1()
    test_stats_above_4()
    test_stats_sum_not_7()
    test_valid_character()
    test_valid_character_output()
    print("All tests passed!")
