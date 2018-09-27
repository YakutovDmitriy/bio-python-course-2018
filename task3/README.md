# Task 2

Do not forget to follow the rules from `pep8` and test your implementations with tests below.

## Implement the following generators in file `task3/task3.py`:

Your implementations should use `yield` and should not use a lot of memory.You can test your implementations using list construction from your iterable.

You can import any function from modules `itertools` and `functools`.


* `def squares(a):`

  `a` is sequence of integers. Return iterable with its sequares.

  For example:
    ```python
    squares([]) -> Nothing
    squares([1, 3, 5]) -> 1, 9, 25
    squares(range(10)) -> 0, 1, 4, 9, ..., 64, 81
    ```

* `def repeatntimes(elems, n):`

  This functions should yield elements from list `elems` `n` times.

  For example:
    ```python
    repeatntimes([1], 5) -> 1, 1, 1, 1, 1
    repeatntimes([1, 2, 3], 3) -> 1, 2, 3, 1, 2, 3, 1, 2, 3
    repeatntimes([1, 2], 0) -> Nothing
    ```

* `def evens(x):`

  `evens` should yield even numbers from `x` and larger that are even. Numbers should be yielded in ascending order.

  For example:
    ```python
    evens(0) -> 0, 2, 4, 6, ...
    evens(5) -> 6, 8, 10, 12, ...
    ```

* `def digitsumdiv(p):`

  `p` is positive integer. This function should yield positive integers with the following property: thier digit sum should be multiple of `p`. Numbers should be yielded in ascending order.

  For example:
    ```python
    digitsumdiv(1) -> 1, 2, 3, 4, 5, ...
    digitsumdiv(5) -> 5, 14, 19, 23, 28, 32, ...
    ```


## Implement the following functions in file `task3/task3.py` using `map`, `filter`, `zip`, `reduce`:

Use only one line of code inside on function!

For example:

  Good code:
  ```python
  def subtract_one(elements):
      return map(lambda x: x - 1, elements)
  ```

  Bad code:
  ```python
  def subtract_one(elements):
      for e in elements:
          yield e - 1
  ```

### Your tasks:

* `def extractnumbers(s):`
  
  `s` is string. Yield digits from string `s`. Their order should coincide with order in `s`.

  For example:
    ```python
    extractnumbers('12345') -> '1', '2', '3', '4', '5'
    extractnumbers('a1b2c3d4e5') -> '1', '2', '3', '4', '5'
    extractnumbers('abcde') -> Nothing
    extractnumbers('1213') -> '1', '2', '1', '3'
    ```

* `def changecase(s):`

  `s` is string. Yield all symbols from string `s`. If symbol is english letter change its case before yielding.

  For example:
    ```python
    changecase('Hello!') -> 'h', 'E', 'L', 'L', 'O', '!'
    ```

* `def productif(elems, conds):`

  `elems` is sequence of `int`, `conds` is sequence of `bool`. Return product of elements from `elems` such that corresponding element of `conds` is `True`. It is guaranteed that length of `conds` is greater than or equal to length of `elems`.

  For example:
    ```python
    productif([1, 2, 3], [True, True, True]) = 6
    productif(range(5), [False, False, True, False, True]) = 8
    productif([], [True, True, True, True]) = 1
    productif([100], [False]) = 1
    ```
