# Task 10

## Subset of bash - `biosh`

### Implement classes `FSItem`, `File` and `Directory` from HW-9

You can add some new methods, maybe they will help you to implement HW-A

### Implement biosh - bio-shell

You can implement this using [this template](biosh.py).

Commands you should implement are listed below. Argument `<dir>` is absolute or relative path to directory. Argument `<file>` is absolute or relative path to file.

* `ls`
  
  List of all items of current directory. This command is already implemented.

* `cd <dir>`

  Changes current directory to `<dir>`.

* `cat <file>`

  Prints content of `<file>` to stdout. If file does not exist, `cat` should print special message like `"There is no file <file>"`

* `head <file>`

  The same as `cat` but prints no more than first `10` lines.

* `tail <file>`

  The same as `cat` but prints no more than last `10` lines.

* `pwd`

  Prints path to current directory.

* `touch <file>`

  Creates `<file>` if it doesn't exists.

* `find <name>`

  prints paths to all files in subdirectory of current directory with name `<name>`.

* `exit`

  Terminates work of biosh. It is already implemented with simple `break` from main loop.


You can find examles of working with biosh below.

```bash

~/work/> python biosh.py
~/work/$ ls

a.txt    FILE    6
b.txt    FILE    0
cdir     DIRECTORY

~/work/$ cat a.txt
HELLO
~/work/$ cd cdir
~/work/cdir/$ ls

ddir     DIRECTORY

~/work/cdir/$ touch b.txt
~/work/cdir/$ ls

b.txt    FILE    0
ddir     DIRECTORY

~/work/cdir/$ pwd
~/work/cdir/
~/work/cdir/$ find hoba.txt

~/work/cdir/ddir/a/hoba.txt
~/work/cdir/ddir/a/b/c/hoba.txt
~/work/cdir/ddir/a/Q/c/hoba.txt

~/work/cdir/$ exit
Bye bye!
```
