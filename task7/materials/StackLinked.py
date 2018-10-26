

class Node:
    """ Node: Class for single node of Stack """

    def __init__(self, elem, nextnode):
        """ Initializes new node """
        self.elem = elem
        self.nextnode = nextnode


class LinkedStack:
    """ LinkedStack: Class implementation """

    def __init__(self):
        """ Initializes new stack """
        self.emptynode = Node(None, None)
        self.head = self.emptynode

    def push(self, elem):
        """ Pushes 'elem' to stack 'self' """
        newhead = Node(elem, self.head)
        self.head = newhead

    def pop(self):
        """ Removes head of stack 'self' and returns it """
        elem = self.head.elem
        newhead = self.head.nextnode
        self.head = newhead
        return elem

    def empty(self):
        """ Checks whether stack 'self' is empty """
        return self.head is self.emptynode


if __name__ == '__main__':
    n = 5

    print("stack:")
    stack = LinkedStack()
    for i in range(n):
        LinkedStack.push(stack, i ** 3)
    while not LinkedStack.empty(stack):
        elem = LinkedStack.pop(stack)
        print(elem)

    print("otherstack:")
    otherstack = LinkedStack()
    for i in range(n):
        otherstack.push(1 / (i + 1))
    while not otherstack.empty():
        elem = otherstack.pop()
        print(elem)
