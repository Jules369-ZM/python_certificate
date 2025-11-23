# Employee Salary Tracking System - Workshop Steps

## Step 1
Create a class named Employee. Inside it, create an __init__ method with self, name, and level parameters. Within the __init__ method, assign name and level to the instance attributes with the same name.

## Step 2
Create an instance of the Employee class passing in the strings "Charlie Brown" and "trainee". Assign the instance to a variable named charlie_brown.

## Step 3
Modify both name and level attributes into _name and _level, since these are not supposed to be modified from outside their class.

## Step 4
Add a __str__ method to the Employee class. Make it return an f-string with the format name: level, replacing name and level with the corresponding attributes.

After that, print charlie_brown to the console.

## Step 5
Create a method named name with a self parameter and decorate it with @property. Inside the method, return self._name.

## Step 6
Print charlie_brown.name to the console.

## Step 7
Create a method named level with a self parameter and decorate it with @property. Inside the method, return self._level.

## Step 8
Print charlie_brown.level to the console.

## Step 9
Update the string returned by __str__ to use self.name and self.level.

## Step 10
Remove the last two print calls.

## Step 11
Give your Employee class a __repr__ method with a self parameter, and make it return a string that can be used to instantiate the object.

## Step 12
Print the result of calling repr(charlie_brown).

## Step 13
Remove the last print call.

## Step 14
Add validation in __init__ to raise TypeError if name or level is not str.

## Step 15
Add a class attribute named _base_salaries with the dictionary {'trainee': 1000, 'junior': 2000, 'mid-level': 3000, 'senior': 4000}.

## Step 16
In __init__, after type checks, raise ValueError if level not in _base_salaries.

## Step 17
At the bottom of __init__, set self._salary to the value from _base_salaries for level.

## Step 18
Add a salary property getter.

## Step 19
At the bottom, print Base salary: $ followed by charlie_brown's salary.

## Step 20
Add a name setter with validation.

## Step 21
Add type validation in name setter.

## Step 22
Print 'name' updated to 'new_name' in name setter.

## Step 23
Try updating charlie_brown's name to a different name.

## Step 24
Restore charlie_brown's name by removing change lines.

## Step 25
Create level setter.

## Step 26
Add level validation (in dict).

## Step 27
Add check for unchanged level.

## Step 28
Add check for lower level.

## Step 29
Update salary to new level before setting level.

## Step 30
Add print for promotion: '{name}' promoted to '{new_level}'.

## Step 31
Set charlie_brown.level to 'junior'.

## Step 32
Add salary setter with simple update and print.

## Step 33
Add type validation in salary setter (int or float).

## Step 34
Add check for minimum salary (higher than base for current level).

## Step 35
In level setter, use self.salary = ... instead of self._salary = ...
