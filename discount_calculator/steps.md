# Discount Calculator Workshop Steps

This document outlines the step-by-step implementation of a discount calculator system using object-oriented design principles in Python.

## Step 1
Define a class named `Product`. Give your class an `__init__` method with the following parameters: `self`, `name`, and `price`. Inside the `__init__` method, assign `name` and `price` parameters to instance attributes with the same name.

## Step 2
Add type hints to the `__init__` method parameters for the Product class:
- `name` parameter should have the type hint `str`
- `price` parameter should have the type hint `float`

## Step 3
Create a `__str__` method in the `Product` class that returns a string with the format "name - $price" (where name and price should be replaced with the values of the corresponding attributes).

## Step 4
Add a return type hint of `None` to the `__init__` method since constructors do not return a value.

## Step 5
Add a return type hint of `str` to the `__str__` method to clearly indicate it returns a string representation.

## Step 6
Create an instance of `Product` with the name "Wireless Mouse" and a price of 50.0. Assign it to a variable named `product`. Then, print product to the console to see what it looks like.

## Step 7
At the top of the code, add the following import statement: `from abc import ABC, abstractmethod`. This imports the ABC class and the `abstractmethod` decorator for creating abstract base classes.

## Step 8
Create a class named `DiscountStrategy` that inherits from `ABC`. This will be an abstract base class that defines the interface for all discount strategies.

## Step 9
Inside the `DiscountStrategy` class, define a method named `is_applicable`. Use the `@abstractmethod` decorator. The method should have parameters `self`, `product`, and `user_tier`. Add type hints: `product: Product`, `user_tier: str`.

## Step 10
Add a return type hint of `bool` to the `is_applicable` method.

## Step 11
Add a second abstract method named `apply_discount` to the `DiscountStrategy` class. Use the `@abstractmethod` decorator with parameters `self` and `product`. Add type hint `product: Product` and return type `float`.

## Step 12
Create a class named `PercentageDiscount` that inherits from `DiscountStrategy`. Give it an `__init__` method with parameters `self` and `percent` (type int, return type None). Store `percent` as an instance attribute.

## Step 13
Implement the `is_applicable` method in `PercentageDiscount`. Return `True` if `self.percent` is less than or equal to 70, otherwise `False`.

## Step 14
Implement the `apply_discount` method in `PercentageDiscount`. Calculate and return `product.price * (1 - self.percent / 100)`.

## Step 15
Create an instance of `PercentageDiscount` with 10 percent. Apply the discount to the product using `apply_discount` and print the result.

## Step 16
Create a class named `FixedAmountDiscount` that inherits from `DiscountStrategy`. Add an `__init__` method with parameters `self` and `amount` (type int, return type None). Store `amount` as an instance attribute.

## Step 17
Implement the `is_applicable` method in `FixedAmountDiscount`. Return `True` if `product.price * 0.9 > self.amount`, otherwise `False`.

## Step 18
Implement the `apply_discount` method in `FixedAmountDiscount`. Return `product.price - self.amount`.

## Step 19
Create an instance of `FixedAmountDiscount` with an amount of 5. Apply the discount to the product and print the result.

## Step 20
Create a class named `PremiumUserDiscount` that inherits from `DiscountStrategy`. Use `pass` in the class body.

## Step 21
Implement the `is_applicable` method in `PremiumUserDiscount`. Return `True` if `user_tier.lower() == 'premium'`, otherwise `False`.

## Step 22
Implement the `apply_discount` method in `PremiumUserDiscount`. Return `product.price * 0.8` (which represents 80% of the original price, i.e., 20% off).

## Step 23
Add an import for the `List` type from the `typing` module at the top of the file.

## Step 24
Create a class named `DiscountEngine`. Give it an `__init__` method with parameters `self` and `strategies` (type hint `List[DiscountStrategy]`, return type `None`). Store `strategies` as an instance attribute.

## Step 25
Add a method named `calculate_best_price` to `DiscountEngine` with parameters `self`, `product`, `user_tier` and return type `float`. Use `pass` in the method body.

## Step 26
Initialize a list named `prices` with `product.price` in the `calculate_best_price` method.

## Step 27
Create a for loop that iterates over `self.strategies`. For each strategy, check if it's applicable using `is_applicable`. If so, calculate the discounted price and append it to the `prices` list.

## Step 28
Return the minimum value from the `prices` list using `min(prices)`.

## Step 29
Remove the print statements from the file (the test code from Steps 6, 15, and 19).

## Step 30
Add an `if __name__ == '__main__'` block. Inside it, create a `Product` instance, set `user_tier` to 'Premium', and create a list of strategies with `PercentageDiscount(10)`, `FixedAmountDiscount(5)`, and `PremiumUserDiscount()`.

## Step 31
Create a `DiscountEngine` instance and calculate the best price using the `calculate_best_price` method.

## Step 32
Add a final print statement to display the best price with two decimal places using f-string formatting.

---

## Final Output
Running the completed discount calculator should output:
```
Best price for Wireless Mouse for Premium user: $40.00
```
