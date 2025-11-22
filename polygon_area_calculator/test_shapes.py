from shapes import Rectangle, Square

# Basic tests from the user story
print("Testing Rectangle and Square classes...")

# Test Rectangle
rect = Rectangle(10, 5)
print(f"Rectangle area: {rect.get_area()}")  # Should be 50
rect.set_height(3)
print(f"Rectangle perimeter: {rect.get_perimeter()}")  # Should be 26
print(f"Rectangle string: {rect}")  # Should be Rectangle(width=10, height=3)
print("Rectangle picture:")
print(rect.get_picture())  # Should show picture

# Test Square
sq = Square(9)
print(f"Square area: {sq.get_area()}")  # Should be 81
sq.set_side(4)
print(f"Square diagonal: {sq.get_diagonal()}")  # Should be 5.656854249492381
print(f"Square string: {sq}")  # Should be Square(side=4)
print("Square picture:")
print(sq.get_picture())  # Should show picture

# Test get_amount_inside
rect.set_height(8)
rect.set_width(16)
result = rect.get_amount_inside(sq)
print(f"Amount inside: {result}")  # Should be 8

# Additional tests for edge cases
print("\nTesting edge cases...")

# Test picture too big
big_rect = Rectangle(51, 51)
print("Big rectangle picture:")
print(big_rect.get_picture())  # Should be "Too big for picture."

big_sq = Square(51)
print("Big square picture:")
print(big_sq.get_picture())  # Should be "Too big for picture."

# Test get_amount_inside with different shapes
small_rect = Rectangle(4, 8)
medium_rect = Rectangle(3, 6)
amount = small_rect.get_amount_inside(medium_rect)
print(f"Rectangle(4,8) can fit {amount} Rectangle(3,6)")  # Should be 1

small_sq = Square(5)
large_rect = Rectangle(15, 10)
amount = large_rect.get_amount_inside(small_sq)
print(f"Rectangle(15,10) can fit {amount} Square(5)")  # Should be 6

rect2 = Rectangle(2, 3)
amount = rect2.get_amount_inside(medium_rect)
print(f"Rectangle(2,3) can fit {amount} Rectangle(3,6)")  # Should be 0

print("\nAll tests completed!")
