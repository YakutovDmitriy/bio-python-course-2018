# Task 5

## Implement the following functions in file `task5/task5.py`:

Your implementations should use recursive object generating.

Objects should be generated in lexicographical order. Please look at examples for better understanding of ordering.


* `def permutations(n):`

  Return list of all permutations of size `n` (`n >= 1`). Every permutation should be represented as `tuple` object.

  For Example:
    ```python
    permutations(1) = [(1,)]
    permutations(2) = [(1, 2), (2, 1)]
    permutations(3) = [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]
    ```

* `def correctbracketsequences(n):`

  Return list of all correct bracket sequences with `n` pairs of brackets. Every sequence should be represented as `str` object.

  For example:
    ```python
    correctbracketsequences(1) = ['()']
    correctbracketsequences(2) = ['(())', '()()']
    correctbracketsequences(3) = ['((()))', '(()())', '(())()', '()(())', '()()()']
    ```

* `def combinationswithrepeats(n, k):`

  Return list of all combinations of numbers from `1` to `n` with repeats of size `k`. Every combination should be sorted `tuple` of numbers.

  For example:
    ```python
    combinationswithrepeats(1, 1) = [(1,)]
    combinationswithrepeats(2, 2) = [(1, 1), (1, 2), (2, 2)]
    combinationswithrepeats(3, 2) = [(1, 1), (1, 2), (1, 3), (2, 2), (2, 3), (3, 3)]
    ```

* `def unorderedpartitions(n):`

  Return list of all unordered partitions of number `n`. Every partition should be sorted `tuple` of numbers.

  For example:
    ```python
    unorderedpartitions(1) = [(1,)]
    unorderedpartitions(3) = [(1, 1, 1), (1, 2), (3,)]
    unorderedpartitions(5) = [(1, 1, 1, 1, 1), (1, 1, 1, 2), (1, 1, 3), (1, 2, 2), (1, 4), (2, 3), (5,)]
    ```
