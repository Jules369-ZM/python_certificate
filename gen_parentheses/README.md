# Generate Parentheses Workshop

This workshop implements a function that generates all valid combinations of parentheses using a breadth-first search (BFS) approach.

## Workshop Steps

**Step 1:** Create a function named `gen_parentheses` with a single parameter `pairs`. For now, return an empty list from the function.

**Step 2:** Add input validation. Check if `pairs` is not an integer using `isinstance()`. If not an integer, return the string "The number of pairs should be an integer."

**Step 3:** Add validation to ensure pairs is at least 1. Check if `pairs < 1`. If true, return the string "The number of pairs should be at least 1."

**Step 4:** Create a `result` variable initialized as an empty list to store valid parentheses combinations. Update the return statement to return `result` instead of an empty list.

**Step 5:** Create a `queue` variable initialized with a list containing one tuple: `('', 0, 0)`. This represents the starting state with an empty string and zero parentheses used. Each tuple contains: (current_string, opening_count, closing_count)

**Step 6:** Add a `while queue:` loop to process states from the queue using BFS.

**Step 7:** Inside the loop, dequeue the first element and unpack it into `current`, `opens_used`, and `closes_used` variables.

**Step 8:** Add a test call `print(gen_parentheses(1))` to verify the function works.

**Step 9:** Add a check for complete combinations: if `len(current) == 2 * pairs`, append `current` to `result`.

**Step 10:** In the else clause, add logic to append opening parentheses when `opens_used < pairs`.

**Step 11:** Add logic to append closing parentheses when `closes_used < opens_used`.

**Step 12:** Update the test call to `print(gen_parentheses(2))`.

**Step 13:** Remove any debug print statements.

**Step 14:** Final test with `print(gen_parentheses(3))` - generates all 5 valid combinations for 3 pairs.

## Objective

Generate all valid combinations of n pairs of parentheses. For example:
- For 1 pair: `["()"]`
- For 2 pairs: `["(())", "()()"]`
- For 3 pairs: `["((()))", "(()())", "(())()", "()(())", "()()()"]`

## Function Signature

```python
def gen_parentheses(pairs):
    # Implementation using BFS
    pass
```

## Running the Code

```bash
cd gen_parentheses
python3 gen_parentheses.py
