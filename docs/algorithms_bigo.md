"What Is an Algorithm and How Does Big O Notation Work?
Every computer program that runs on your device has a specific set of instructions, which are executed in a specific order to complete a task.

The task could be sorting a set of numbers, modifying an image, tracking inventory, or even running your favorite video game.

This is where algorithms come into play. An algorithm is a set of unambiguous instructions for solving a problem or carrying out a task.

You can think of algorithms as \"recipes\". When you cook, recipes list all the ingredients that you'll need, and provide step by step instructions on how to prepare a dish.

Equivalently, you can think of algorithms as \"recipes\" that tell computers exactly what should be done and how to do it.

Algorithms have two key characteristics:

They cannot continue indefinitely. They must finish in a finite number of steps.

Each step must be precise and unambiguous.

They may have zero, one, or more inputs, and generate one or more outputs.

The steps of an algorithm are independent from any programming language.

But to actually make them run on a computer, you need to implement them in a programming language, like Python or JavaScript.

If an algorithm is correct, the output for any valid input should match the expected output.

In addition to being correct, algorithms should also be efficient.

Algorithm efficiency can be measured in terms of how long they take to run and how much space they require in memory to complete the task.

Knowing an algorithm's efficiency is very important because it gives you an idea of how well it will perform as the input size grows.

For example, sorting 15 integers is not the same as sorting 1 million integers.

As the process grows in size and complexity, if the algorithm is not efficient enough to handle it, you might end up with a very slow computer program that may even crash the entire system.

That's why it's very important to develop and choose the most efficient algorithms possible.

This is where Big O notation becomes very important.

Big O notation describes the worst-case performance, or growth rate, of an algorithm as the input size increases.

The growth rate of an algorithm refers to how the resources it requires increase as the input size grows.

Big O notation focuses on the worst-case performance because this case is very important to understand how efficient the algorithm can be, even in the worst case scenario, regardless of the input.

Going back to our sorting example, sorting 1 million integers should intuitively take more time and resources than sorting 15 integers.

But how much more?

This really depends on the algorithm that you choose to sort them.

Big O notation will not give you an exact number to describe the algorithm's efficiency, but it will give you an idea of how it scales as the input size grows, based on the number of operations performed by the algorithm.

In Big O notation, we usually denote input size with the letter n. For example, if the input is a list, n would denote the number of elements in that list.

Constant factors and lower-order terms are not taken into account to find the time complexity of an algorithm based on the number of operations. That's because as the size of n grows, the impact of these smaller terms in the total number of operations performed will become smaller and smaller.

The term that will dominate the overall behavior of the algorithm will the term with n, the input size.

For example, if an algorithm performs 7n + 20 operations to be completed, the impact of the constant 20 on the final result will be smaller and smaller as n grows. The term 7n will tend to dominate and this will define the overall behavior and efficiency of the algorithm.

Another example would be an algorithm that takes 20n² + 15n + 7 operations to be completed. The term 20n² will tend to dominate as n grows, so this algorithm would have a quadratic time complexity because the dominant term has n².

Quadratic time complexity is one of many different types of time complexities that you can find in the world of algorithms.

Let's learn about some of the most common ones.

O(1) is known as \"Constant Time Complexity\". When an algorithm has constant time complexity, it takes the same amount of time to run, regardless of input size.

For example, checking if a number is even or odd will always take the same amount of time, regardless of the number itself.

Example Code
def check_even_or_odd(number):
    if number % 2 == 0:
        return 'Even'
    else:
        return 'Odd'
O(log n) is known as \"Logarithmic Time Complexity\". This means that the time required by the algorithm increases slowly as the input size grows. This is common in problems in which the size of the problem is repeatedly reduced by a constant fraction.

For example, a popular search algorithm called Binary Search has O(log n) worst-case time complexity. This is because it eliminates half of the remaining elements in each comparison, which makes it more efficient overall.

O(n) is known as \"Linear Time Complexity\". The running time of algorithms with this time complexity increases proportionally to the input size.

For example, a for loop that iterates over all the elements of a list will perform more iterations as the number of list elements increases. If the list is doubled in size, the number of operations will approximately double as well.

Example Code
for grade in grades:  # grades is a list.
    print(grade)
O(n log n) is known as \"Log-Linear Time Complexity\". This is a common time complexity of efficient sorting algorithms, like Merge Sort and Quick Sort.

O(n²) is known as \"Quadratic Time Complexity\". The running time of these algorithms increases quadratically relative to the input size, which is generally not efficient for real-world problems.

Nested loops are a common example of quadratic time complexity. The inner loop will perform n iterations for each one of the n iterations of the outer loop, resulting in n squared iterations.

Example Code
for i in range(n):
    for j in range(n):
        print(\"Hello, World!\")
Other time complexities include \"Exponential Time Complexity\", denoted as O(2^n), and \"Factorial Time Complexity\", denoted as O(n!). Both are inefficient for real-world scenarios.

In this graph, you can compare the growth of the mathematical functions that represent the most common time complexities. Think of the x-axis (horizontal) as the input size and the y-axis (vertical) as the running time of the algorithm.

You can see that the Quadratic Time Complexity (O(n²)) (yellow) grows much faster than the other ones, while the Constant Time Complexity (O(1)) (red) stays constant, even if the input gets larger.

graph comparing time complexity
Great. So far, you've learned about Big O notation in terms of time requirements, but this notation can also be applied to the context of space requirements.

In this context, it describes how the memory space required by the algorithm grows as the input size grows.

Algorithms with \"Constant Space Complexity\" O(1) always require a constant amount of memory space, even as the input gets larger.

An example would be an algorithm that only creates and stores a few variables in memory.

In contrast, the space required by algorithms with \"Linear Space Complexity\" O(n) increases proportionally as the input size grows.

An example of this would be an algorithm that creates and stores a copy of a list of length n.

And finally, the space requirements of an algorithm with \"Quadratic Space Complexity\" O(n²) increase quadratically as the input size grows.

An example of this would be creating a 2D matrix, where the dimensions are determined by the input size, storing all possible pairs.

Algorithms are the building-blocks of computer programs, while Big O notation is a powerful framework for analyzing how efficient they are, based on how their time and space requirements in the worst-case scenario scale as the input size grows. Understanding their efficiency is very important for developing software that works efficiently in real-world scenarios.

Questions

Which of the following best describes an algorithm?


A specific programming language used to write code.

A set of step-by-step instructions designed to solve a problem or perform a task.

A type of computer hardware component.

A software application used for developing and playing games.

What is the primary purpose of Big O notation in the context of algorithms?


To measure the exact time an algorithm takes to run on a specific computer in seconds.

To count the total number of lines of code in an algorithm.

To describe how the resource usage of an algorithm grows as the input size increases.

To determine the best-case performance of an algorithm.

If an algorithm has a time complexity of O(n), what does this mean about its performance?


The algorithm's running time increases proportionally with the input size.

The algorithm's running time remains constant regardless of the input size.

The algorithm's running time grows exponentially with the input size.

The algorithm's running time decreases as the input size gets larger.

What Is Binary Search and How Does It Differ From Linear Search?
Searching through a list of items is a common occurrence in computer science. There are two key algorithms you should know about when it comes to searching: linear search and binary search.

Linear search starts at the beginning of a list and iterates through each item until it finds the target value it is looking for.

If the target value is found, the index where it's located in the list is returned. If the target value isn't found, -1 is returned. We return -1 because it's not a valid index in most programming languages.

Here is what the code looks like for linear search:

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1
If the list we'll search through is [13, 4, 7, 9, 10] and the target value is 9, the function would return 3 because 9 is at index 3.

If we changed the target value to 5, the function would return -1 because 5 is not in the list.

While this is a relatively straightforward algorithm, it is not the most efficient. If you have a large list of items, linear search can take a long time to find the target value.

The time complexity of linear search is O(n) because the time it takes to search through the list grows linearly with the size of the list.

The space complexity of linear search is O(1) because it doesn't require any additional space to search through the list.

Binary search is a more efficient algorithm for searching through a large list of items. The condition here is that the list must be sorted in ascending order.

Binary search works by dividing the list in half and checking if the target value is in the middle of the list. If the target value is in the middle of the list, the index of the target value is returned. Otherwise, the algorithm checks if the target value is in the left or right half of the list.

It continues to divide the remaining parts of the list into halves until the target value is found. If the target value is not in the list, it returns -1

Here is what the code looks like for binary search:

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1
We start by identifying a low and high index. This represents the range of the list we are searching through.

We then check the condition of low being less than or equal to high. If low is greater than high, we have searched through the entire list and the target value is not found. In that case we stop the search and return -1.

If the low index is less than or equal to the high index, we calculate the middle index of the list, mid. We then check if the target value is at the middle index. If it is, we return the middle index.

Otherwise, we check if the value at the midpoint is less than the target. If it is, we update the low index to be the middle index plus one. This means we will search the right half of the list.

Lastly, if none of the other conditions are True, we update the high index to be the middle index minus one. This means we will search the left half of the list.

We continue to repeat this process until we find the target or determine that the target is not in the list.

The time complexity of binary search is O(log n) because the time it takes to search through the list grows logarithmically with the size of the list.

The space complexity of binary search is O(1) because it doesn't require any additional space to search through the list.

Binary search and linear search can be used for a variety of problems you will encounter in computer science. It is important to understand the differences between the two algorithms and when to use each one.

Questions

What is the main difference between linear search and binary search?


Linear search is faster than binary search.

Binary search requires a sorted list, while linear search does not.

Linear search can only be used with numbers.

Binary search always returns the first occurrence of a target.

What is the time complexity of linear search?


O(1)

O(log n)

O(n)

O(n²)

In binary search, what happens if the target value is not found in the list?


It returns the middle index.

It returns -1.

It returns the last index checked.

It enters an infinite loop.

What Is Divide and Conquer, and How Does Merge Sort Work?
The divide and conquer paradigm in computer science is a technique for recursively breaking down problems into smaller sub problems. One of the key aspects of this technique is recursion, which happens when a function calls itself repeatedly until a base case is reached. In this lesson, we will take a look at the merge sort algorithm to better understand how the divide and conquer technique works.

Let's say we had this list of numbers:

42 37 53 17
The goal is to sort that list from smallest to largest using the merge sort algorithm. The first step is to divide that list in half:

42 37 | 53 17
Then we need to look at the left side of the list:

42 37
We take that sub list and divide in half again until each sub list has only one item in it:

42 | 37
A list with only one item in it is sorted by default. Next we need to merge each of those one element sub lists into a sorted list:

37 42
Then we follow the same process for the right side of the original list:

# right side of original list
53 17

# divide the list in half
53 | 17

# merge the lists in sorted order
17 53
Now that both halves of the original list are sorted, we merge those two halves together and sort the elements:

17 37 42 53
Here is what the algorithm looks like in code:

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    sorted_list = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1

    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])

    return sorted_list
The time complexity for merge sort would be O(n log n) because the list is continuously divided in half (log n) and then merged together (O(n)). Unlike other sorting algorithms like bubble sort, merge sort is not sorted in place and has a space complexity of O(n).

Questions

What is the divide and conquer paradigm in computer science?


A technique for detecting a cycle in function value iterations using just two iterators.

An algorithm for comparing two elements and swapping them from smallest to largest if needed.

A technique for recursively breaking down problems into smaller sub problems.

An algorithm to compute the shortest connecting network for points in a plane.

What is the time complexity for the merge sort algorithm?


O(n log n)

O(log n²)

O(n³ log n)

O(log n³)

What is the space complexity for the merge sort algorithm?


O(n²)

O(1)

O(n log n)

O(n)
