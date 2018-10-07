# Task 4

## Implement the following functions in file `task4/task4.py`:

Your implementations should use recursion.
You can not import any modules (`math`, `itertools`, etc).


These functions have different difficulty. You can implement only some of them and pass the task.

* `def factorial(n):`

  Calculate factorial of `n`. `n >= 0`

  For Example:
    ```python
    factorial(0) = 1
    factorial(2) = 2
    factorial(4) = 24
    ```

* `def fibonacci(n):`

  Calculate `n`-th Fibonacci number. Fibonacci numbers are defined as follows:

  * `F(1) = F(2) = 1`;
  * `F(n) = F(n - 1) + F(n - 2)`, `n >= 3`.

  Prefix of Fibonacci numbers sequence: `1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...`

  For example:
    ```python
    fibonacci(1) = 1
    fibonacci(4) = 3
    fibonacci(10) = 55
    ```

* `def recurrent(n):`

  Calculate `n`-th number of the following reccurent:

  * `f(0) = 0`
  * `f(1) = 1`
  * `f(2 n) = f(n)`
  * `f(2 n + 1) = f(n + 1) + f(n)`

  For example:
    ```python
    reccurent(2) = 1
    reccurent(3) = 2
    recurrent(5) = 3
    recurrent(7) = 3
    ```

* `def digitsum(n):`

  Calculate the sum of digits of decimal representation of number `n`.

  For example:
    ```python
    digitsum(0) = 0
    digitsum(123) = 6
    digitsum(192837465) = 45
    ```

* `def reversestring(s):`

  Return reversed string `s`

  For example:
    ```python
    reversestring('') = ''
    reversestring('1') = '1'
    reversestring('asdf') = 'fdsa'
    reversestring('abacaba') = 'abacaba'
    ```


* `def ackermann(m, n):`

  Ackermann number can be calculated with the following recurrent formula:

  * `A(0, n) = n + 1`
  * `A(m, 0) = A(m - 1, 1)`
  * `A(m, n) = A(m - 1, A(m, n - 1))`

  Return `A(m, n)`

  For example:
    ```python
    ackermann(0, 10) = 11
    ackermann(1, 1) = 3
    ackermann(2, 2) = 7
    ackermann(2, 5) = 13
    ackermann(3, 3) = 61
    ```

* `def drawborders(n):`

  You task is to create some borders in picture `n x n`.

  For example:
    ```python
    drawborders(1) = ['+']

    drawborders(2) = ['++',
                      '++']

    drawborders(3) = ['+-+',
                      '|+|',
                      '+-+']

    drawborders(4) = ['+--+',
                      '|++|',
                      '|++|',
                      '+--+']

    drawborders(5) = ['+---+'
                      '|+-+|',
                      '||+||',
                      '|+-+|',
                      '+---+']
    ```

* `def genbinarystrings(n):`

  Return list of all binary strings (i.e. strings of characters `0` and `1`) of length `n`.
  String should be ordered in lexicographical order.

  For example:
    ```python
    genbinarystrings(0) = ['']
    genbinarystrings(1) = ['0', '1']
    genbinarystrings(2) = ['00', '01', '10', '11']
    genbinarystrings(3) = ['000', '001', '010', '011', '100', '101', '110', '111']
    ```

* `def istwopower(n):`

  Given integer `n` find if it is power of `2` or not.

  For example:
    ```python
    istwopower(-5) = False
    istwopower(0) = False
    istwopower(1) = True
    istwopower(2) = True
    istwopower(4) = True
    istwopower(67) = False
    istwopower(1024) = True
    ```


* `def concatnumbers(a, b):`

  You are given positive integers `a` and `b`. Find integer `c` such that its decimal representation equals to concatenation of decimal representations of `a` and `b`.

  For example:
    ```python
    concatnumbers(1, 2) = 12
    concatnumbers(55, 88) = 5588
    concatnumbers(123, 789) = 123789
    concatnumbers(1000, 2) = 10002
    ```


* `def abacaba(n):`

  You are given positive integer `n`. Think about name of this function and examples and implement a function which generates similar lists. :)

  For example:
    ```python
    abacaba(1) = [1]
    abacaba(2) = [1, 2, 1]
    abacaba(3) = [1, 2, 1, 3, 1, 2, 1]
    abacaba(4) = [1, 2, 1, 3, 1, 2, 1, 4, 1, 2, 1, 3, 1, 2, 1]
    ```

* `def parentheses(s):`

  You are given a string. Add some parentheses pairs. Please find out the exact task from the examples.

  For example:
    ```python
    parentheses('example') = '(e(x(a(m)p)l)e)'
    parentheses('odd') = '(o(d)d)'
    parentheses('even') = '(e(ve)n)'
    ```


* `def gcd(a, b):`

  You are given positive integers `a` and `b`. Find their greatest common divisor using [Euclead algorithm](https://en.wikipedia.org/wiki/Greatest_common_divisor#Using_Euclid's_algorithm).

  Note that you can't use `math.gcd`, etc.

  For example:
    ```python
    gcd(1, 5) = 1
    gcd(4, 6) = 2
    gcd(18, 12) = 6
    gcd(283918822, 595730520) = 22
    ```

* `def mergesort(a):`

  You are given a list of integers `a`. Sort it using  [Merge sort algorithm](https://en.wikipedia.org/wiki/Merge_sort).

  Note that you can't use `list.sort()`, `sorted()`, etc.

  For example:
    ```python
    mergesort([]) = []
    mergesort([100]) = [100]
    mergesort([1, 3, 2]) = [1, 2, 3]
    mergesort([1, 3, 5, 4, 2]) = [1, 2, 3, 4, 5]
    ```
