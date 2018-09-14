# Task 1

## Implement the following functions in file `task1/task1.py`:

* `def unique(e):`

  This function should return sorted list of distinct elements of `e`.

  For example:
    ```
    unique([1, 2, 1, 3]) = [1, 2, 3]
    unique({5, 1, 3}) = [1, 3, 5]
    unique('adsfasdf') = ['a', 'd', 'f', 's']
    ```

* `def transposeDict(d):`

  This function should return transposed dict `d`. It is garantueed that all the values of dict `d` are distinct.

  For example:
    ```
    transposeDict({1: 'a', 2: 'b'}) = {'a': 1, 'b': 2}
    transposeDict({1: 1}) = {1: 1}
    transposeDict({}) = {}
    ```

* `def mex(e):`

  This function should return minimal positive integer which is not present at list `e`.

  For example:
    ```
    mex([1, 2, 3]) = 4
    mex(['asdf', 123]) = 1
    mex([0, 0, 1, 0]) = 2
    ```
* `frequencyDict(s):`

  This function should return dict with counts of every symbol from string `s`.

  For example:
    ```
    frequencyDict('') = {}
    frequencyDict('abacaba') = {'a': 4, 'b': 2, 'c': 1}
    ```

<b>
  It is possible to implement each function using one line of code.
  Maybe such implementation will be encouraged :)
</b>
