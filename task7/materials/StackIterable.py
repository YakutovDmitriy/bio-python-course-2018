

class Node:
    """ Node: Class for single node of Stack """

    def __init__(self, elem, nextnode):
        """ Initializes new node """
        self.elem = elem
        self.nextnode = nextnode


class LinkedStackIterator:
    """ LinkedStackIterator: Iterator for LinkedStack """

    def __init__(self, node, emptynode):
        """ Initializes new Iterator """
        self.node = node
        self.emptynode = emptynode

    def __next__(self):
        """ Returns next element of stack: next(iter) """
        if self.node is self.emptynode:
            raise StopIteration
        else:
            elem = self.node.elem
            self.node = self.node.nextnode
            return elem


class LinkedStack:
    """ Iterable LinkedStack: Class implementation """

    def __init__(self):
        """ Initializes new stack """
        self.emptynode = Node(None, None)
        self.head = self.emptynode
        self.size = 0

    def push(self, elem):
        """ Pushes 'elem' to stack 'self' """
        newhead = Node(elem, self.head)
        self.head = newhead
        self.size += 1

    def pop(self):
        """ Removes head of stack 'self' and returns it """
        elem = self.head.elem
        newhead = self.head.nextnode
        self.head = newhead
        self.size -= 1
        return elem

    def empty(self):
        """ Checks whether stack 'self' is empty """
        return self.head is self.emptynode

    def __iter__(self):
        """ Returns Iterator for stack: iter(stack) """
        return LinkedStackIterator(self.head, self.emptynode)

    def __len__(self):
        """ Returns size of stack: len(stack) """
        return self.size


if __name__ == '__main__':
    n = 5

    stack = LinkedStack()
    for i in range(5):
        stack.push(i * 10)

    for x in stack:
        print(x)

    print(list(stack))
