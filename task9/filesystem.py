import os


class FileSystemError(Exception):
    ''' Class for errors in filesystem module '''
    pass


class FSItem(object):
    ''' Common class for OS items OS: Files and Directories '''

    def __init__(self, path):
        ''' Creates new FSItem instance by given path to file '''
        pass

    def rename(self, newname):
        ''' Renames current item
                raise FileSystemError if item does not exist
                raise FileSystemError if item "newname" already exists '''
        pass

    def create(self):
        ''' Creates new item in OS
                raise FileSystemError if item with such path already exists '''
        pass

    def getname(self):
        ''' Returns name of current item '''
        pass

    def isfile(self):
        ''' Returns True if current item exists and current item is file, False otherwise '''
        pass

    def isdirectory(self):
        ''' Returns True if current item exists and current item is directory, False otherwise '''
        pass



class File(FSItem):
    ''' Class for working with files '''

    def __init__(self, path):
        ''' Creates new File instance by given path to file
                raise FileSystemError if there exists directory with the same path '''
        pass

    def __len__(self):
        ''' Returns size of file in bytes
                raise FileSystemError if file does not exist '''
        pass

    def getcontent(self):
        ''' Returns list of lines in file (without trailing end-of-line)
                raise FileSystemError if file does not exist '''
        pass

    def __iter__(self):
        ''' Returns iterator for lines of this file
                raise FileSystemError if file does not exist '''
        pass


class Directory(FSItem):
    ''' Class for working with directories '''

    def __init__(self, path):
        ''' Creates new Directory instance by given path
                raise FileSystemError if there exists file with the same path '''
        pass

    def items(self):
        ''' Yields FSItem instances of items inside of current directory
                raise FileSystemError if current directory does not exists '''
        pass

    def files(self):
        ''' Yields File instances of files inside of current directory
                raise FileSystemError if current directory does not exists '''
        pass

    def subdirectories(self):
        ''' Yields Directory instances of directories inside of current directory
                raise FileSystemError if current directory does not exists '''
        pass

    def filesrecursive(self):
        ''' Yields File instances of files inside of this directory,
                inside of subdirectories of this directory and so on...
                raise FileSystemError if directory does not exist '''
        pass

    def getsubdirectory(self, name):
        ''' Returns Directory instance with subdirectory of current directory with name "name"
                raise FileSystemError if item "name" already exists and item "name" is not directory '''
        pass
