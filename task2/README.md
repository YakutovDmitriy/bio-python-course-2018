# Task 2

## Implement the following functions in file `task2/task2.py`:

Do not forget to follow the rules from `pep8` and test your implementations with tests below.


* `def listToString(a):`

  `a` is list of integers. Return string representing this list.

  For example:
    ```
    listToString([]) = "[]"
    listToString([1, 2, 3]) = "[1, 2, 3]"
    listToString(['some string']) = "['some string']"
    ```


* `def addBorder(a):`

  `a` is picture (nonempty list of nonempty strings of equal lengths). Add border around it.

  For example:
    ```
    addBorder(['abc',
               'def']) = ['+---+',
                          '|abc|',
                          '|def|',
                          '+---+']
    ```


* `def shorting(e):`

  This function should return `reductions` of strings of list `e`.

  `Reduction` of string `s` is:
  * If length of `s` is less or equal to `10`, then it is string `s` itself;
  * Otherwise it is first letter of `s` and last letter of `s` and the number of symbols between this two symbols in `s` between them.

  For example:
    ```
    shorting(['word', 'localization', 'internationalization',
              'pneumonoultramicroscopicsilicovolcanoconiosis'])
              = ['word', 'l10n', 'i18n', 'p43s']
    ```


* `def competition(e, k):`

  You have a list of non-negative integers `e`. `e[i]` is score of `i`-th participant if competition. Number in `e` are in descending order. 

  An excerpt from competition rules: "Contestant who earns a score equal to or greater than the `k`-th place (in `0`-enumeration) finisher's score will advance to the next round, as long as the contestant earns a positive score..."

  Return number of participants who will advance to the next round.

  For example:
    ```
    competition([5, 4, 3, 2, 1], 2) = 3            # Participants with scores 5, 4, 3 are advanced
    competition([1, 0, 0, 0], 3) = 1               # Participants with zeros won't advance
    competition([10, 9, 8, 7, 7, 7, 5, 5], 4) = 6  # Participants with scores 10, 9, 8, 7, 7, 7 are advanced
    ```


* `def goodPairs(a, b):`

  `a`  and `b` are lists of positive integers. Consider a pair of integers `(i, j)` to be good if `i * j` is divisible by `i + j`. Return sorted list of integers `s` such that:

  * There exist two numbers `i`, `j` from list `a`;
  * `i` is in list `a`;
  * `j` is in list `b`;
  * Pair `(i, j)` is good;
  * `s = i ** 2 + j ** 2`.

  For example:
    ```
    goodPairs([4, 5, 6, 7, 8], [8, 9, 10, 11, 12]) = [128, 160, 180]
    goodPairs([2], [2]) = [8]
    goodPairs([7, 8, 9], [5, 3, 2]) = []
    ```
  Note: in first tests pairs `(i, j)` are `(8, 8)`, `(4, 12)` and `(6, 12)`.


* `def makeShell(n):`

  `n` is positive integer. You should return list `a` of length `2 n + 1`. Its `i`-th element is list of some zeros. 

  * `a[0]` should contain `1` zero;
  * `a[1]` should contain `2` zeros;
  * ...
  * `a[n - 2]` should contains `n - 1` zeros;
  * `a[n - 1]` should contains `n` zeros;
  * `a[n]` should contains `n - 1` zeros;
  * ...
  * `a[2 * n - 3]` should contains `2` zeros;
  * `a[2 * n - 2]` should contains `1` zero.

  For example:
    ```
    makeShell(1) = [[0]]
    makeShell(2) = [[0], [0, 0], [0]]
    makeShell(3) = [[0], [0, 0], [0, 0, 0], [0, 0], [0]]
    ```
