# Task 9

## Implement classes `FSItem`, `File` and `Directory`

You can find the specification in [file `filesystem.py`](filesystem.py).

You should use `os` and `os.path` modules and `file` built-in class. Read the documentation.

You should avoid code duplication. Reuse code you wrote in some methods inside of other methods. You can create your own methods and call them to avoid code duplication.

There is a help class `FileSystemError`. You may change its implementation. You should raise `FileSystemError` when it is needed. You should provide short description of every error you raises. For example:
  ```python
  raise FileSystemError("Can't create file: {0} already exist".format(self.getname()))
  ```

You can implement only some of the methods below. Also you can ignore some requirements above, but you will lose some points in such case. There can be some inaccuracies in method descriptions. You can choose the way to understand them and implement such methods as you want.

### Class `FSItem`

Common class for OS items: Files and Directories.

Class `FSItem` is parent class for classes `File` and `Directory`. It contains interface of classes `File` and `Directory`. Some of its methods can be implemented in this class (e.g. `getname`), but other methods should be implemented inside of child classes `File` and `Directory` with different implementation (e.g. `isfile` and `isdirectory`). Think about common properties of `File` and `Directory` and implement all the common methods in `FSItem`. Methods of `FSItem` class which depend on type of `FSItem` (`File` or `Directory`) should raise `FileSystemError` with description like `"Method 'isfile' is not implemented for abstract FSItem"`

* `def __init__(self, path):`

  Creates new `FSItem` instance by given path to file. Note that you don't need to create new file or directory in OS when someone calls `File.__init__`. You just create instance of this class.

* `def rename(self, newname):`

  Renames current `FSItem`. Raises `FileSystemError` if item does not exist. `FileSystemError` if item `"newname"` already exists.

* `def create(self):`
  
  Creates new item in OS. This item should be file if `self` is instance of `File`-class and directory if `self` is instance of `Directory`-class. Raise `FileSystemError` if item with such path already exists.

* `def getname(self):`

  Returns name of current item. It should return item of current name even if this item does not exist in OS.

* `def isfile(self):`

  Returns `True` if current item exists in OS and current item is file, `False` otherwise.

* `def isdirectory(self):`

  Returns `True` if current item exists in OS and current item is directory, `False` otherwise.


### Class File(FSItem)

Child class of `FSItem`-class. Class for working with files.

* `def __init__(self, path):`

  Creates new File instance by given path to file. Raises `FileSystemError` if there exists directory with the same path.

* `def __len__(self):`

  Returns size of file in bytes. Raises `FileSystemError` if file does not exist.
 
* `def getcontent(self):`

  Returns list of lines in file. Raises `FileSystemError` if file does not exist.

* `def __iter__(self):`

  Returns iterator for lines of this file. Raises `FileSystemError` if file does not exist. It is not necessary to create new class like `FileIterator`. Reuse method `getcontent` here.


### class Directory(FSItem)

Child class of `FSItem`-class. Class for working with directories.

* `def __init__(self, path):`

  Creates new `Directory` instance by given path. Raises `FileSystemError` if there exists file with the same path.

* `def items(self):`

  Yields `FSItem` instances of items inside of current directory. Raise `FileSystemError` if current directory does not exists in OS.

* `def files(self):`

  Yields `File` instances of files inside of current directory. Raises `FileSystemError` if current directory does not exists in OS. Try to reuse other methods here to make this method one-liner.

* `def subdirectories(self):`

  Yields `Directory` instances of directories inside of current directory. Raises `FileSystemError` if current directory does not exists in OS. Try to reuse other methods here to make this method one-liner.

* `def filesrecursive(self):`

  Yields File instances of files inside of this directory, inside of subdirectories of this directory and so on... Raises `FileSystemError` if directory does not exist in OS. You should use recursive approach in this method.

* `def getsubdirectory(self, name):`

  Returns `Directory` instance with subdirectory of current directory with name `"name"`. Raise `FileSystemError` if item `"name"` already exists and item `"name"` is not directory.
