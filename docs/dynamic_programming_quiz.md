# Dynamic Programming Quiz

To pass the quiz, you must correctly answer at least 9 of the 10 questions below.

## 1.

What are the two essential properties that must be present in a problem for dynamic programming to be an effective solution approach?

- Recursion capability and iterative loops
- Overlapping subproblems and optimal substructure
- Sequential processing and parallel computation
- Fast execution time and minimal memory usage

## 2.

What is the primary difference between the memoization and tabulation approaches in dynamic programming?

- Memoization is a top-down approach using recursion, while tabulation is a bottom-up approach using iteration.
- Memoization uses hash tables while tabulation uses arrays, making it more efficient.
- Memoization is faster but uses more memory and CPU cycles than tabulation.
- Memoization can only solve simpler problems than tabulation.

## 3.

Why do naive recursive solutions to dynamic programming problems typically have exponential time complexity?

- Because each recursive call branches multiple times, causing the same subproblems to be recalculated repeatedly.
- Because they use exponential amounts of memory to store variables.
- Because they must check all possible permutations of the input.
- Because they require sorting data in exponential time.

## 4.

What does optimal substructure mean in the context of dynamic programming?

- The problem must have a unique, single optimal solution.
- The optimal solution can be constructed from optimal solutions to its subproblems.
- The algorithm must use the most efficient data structure available.
- The solution must minimize both time and space complexity simultaneously.

## 5.

When implementing memoization, what happens when a function is called with arguments that have already been computed?

- An error is thrown because duplicate calculations are not allowed.
- The function averages the old and new results for better precision.
- The cached result is returned immediately without recomputation.
- The function recalculates the result to ensure accuracy.

## 6.

What is a key advantage of using tabulation instead of memoization?

- Tabulation always requires less memory than memoization.
- Tabulation avoids recursion overhead and provides predictable sequential execution.
- Tabulation can solve a broader class of problems.
- Tabulation is always easier to implement and understand.

## 7.

In a bottom-up dynamic programming solution, why are base cases initialized first?

- To prevent infinite loops in the algorithm.
- To allocate memory for the data structure efficiently.
- To improve the time complexity of the algorithm.
- To provide foundational values upon which all larger subproblems are built.

## 8.

How does dynamic programming transform the time complexity of problems that exhibit overlapping subproblems?

- From polynomial to logarithmic by dividing the problem efficiently.
- From exponential to polynomial by storing and reusing subproblem solutions.
- From linear to constant by using hash tables.
- From quadratic to linear by optimizing loop structures.

## 9.

What trade-off does dynamic programming typically make to achieve better time complexity?

- It sacrifices code readability for faster execution.
- It requires more complex algorithms that are harder to maintain.
- It uses additional space to store intermediate results.
- It limits the size of problems that can be solved.

## 10.

In which scenario would dynamic programming NOT be the appropriate algorithmic approach?

- When the problem can be broken into smaller subproblems.
- When subproblems are independent and don't overlap.
- When space complexity must be minimized.
- When the problem requires finding an optimal solution.
