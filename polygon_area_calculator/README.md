# Polygon Area Calculator

This project implements a Polygon Area Calculator using object-oriented programming principles in Python.

## Classes Overview

### Rectangle Class

The Rectangle class provides functionality for creating and manipulating rectangle shapes.

**Methods:**
- `__init__(width, height)` - Initialize with width and height
- `set_width(width)` - Set the width of the rectangle
- `set_height(height)` - Set the height of the rectangle
- `get_area()` - Returns width × height
- `get_perimeter()` - Returns 2 × (width + height)
- `get_diagonal()` - Returns √(width² + height²)
- `get_picture()` - Returns a string representation using "*" characters (max 50x50)
- `get_amount_inside(shape)` - Returns how many of the passed shape can fit inside this rectangle

**String Representation:** `Rectangle(width=X, height=Y)`

### Square Class

The Square class inherits from Rectangle and represents square shapes.

**Additional Methods:**
- `__init__(side)` - Initialize with side length
- `set_side(side)` - Set the side length (affects both width and height)
- Overridden `set_width()` and `set_height()` - Both set width and height to maintain square properties

**String Representation:** `Square(side=X)`

## Usage Example

```python
from shapes import Rectangle, Square

# Create a rectangle
rect = Rectangle(10, 5)
print(rect.get_area())  # 50

rect.set_height(3)
print(rect.get_perimeter())  # 26

print(rect)  # Rectangle(width=10, height=3)
print(rect.get_picture())
# **********
# **********
# **********

# Create a square
sq = Square(9)
print(sq.get_area())  # 81

sq.set_side(4)
print(sq.get_diagonal())  # 5.656854249492381

print(sq)  # Square(side=4)
print(sq.get_picture())
# ****
# ****
# ****
# ****

# Check how many squares fit in a larger rectangle
rect.set_width(16)
rect.set_height(8)
print(rect.get_amount_inside(sq))  # 8
```

## Tests Covered

All user stories and test requirements have been implemented and verified:

1. ✅ Rectangle class exists
2. ✅ Square class exists
3. ✅ Square is a subclass of Rectangle
4. ✅ Square is distinct from Rectangle
5. ✅ Square instance is instance of both Square and Rectangle
6. ✅ Rectangle string representation: `Rectangle(width=3, height=6)`
7. ✅ Square string representation: `Square(side=5)`
8. ✅ Rectangle area calculation: `Rectangle(3, 6).get_area() == 18`
9. ✅ Square area calculation: `Square(5).get_area() == 25`
10. ✅ Rectangle perimeter calculation: `Rectangle(3, 6).get_perimeter() == 18`
11. ✅ Square perimeter calculation: `Square(5).get_perimeter() == 20`
12. ✅ Rectangle diagonal calculation: `Rectangle(3, 6).get_diagonal() ≈ 6.7082`
13. ✅ Square diagonal calculation: `Square(5).get_diagonal() ≈ 7.0711`
14. ✅ Rectangle string changes after setting new values
15. ✅ Square string changes after using set_side()
16. ✅ Square string changes after using set_width() or set_height()
17. ✅ Rectangle get_picture() returns correct representation
18. ✅ Square get_picture() returns correct representation
19. ✅ get_picture() returns "Too big for picture." when dimensions > 50
20. ✅ Rectangle(15,10).get_amount_inside(Square(5)) == 6
21. ✅ Rectangle(4,8).get_amount_inside(Rectangle(3, 6)) == 1
22. ✅ Rectangle(2,3).get_amount_inside(Rectangle(3, 6)) == 0

## Running the Project

To run the tests:
```bash
cd polygon_area_calculator
python3 test_shapes.py
```

To use the classes in your own code:
```python
from shapes import Rectangle, Square
