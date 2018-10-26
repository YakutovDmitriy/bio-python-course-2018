

class Stack:
    """ Stack: Class implementation """

    def __init__(stack):
        """ Initializes new stack """
        stack.elements = []

    def push(stack, elem):
        """ Pushes 'elem' to stack 'stack' """
        stack.elements.append(elem)

    def pop(stack):
        """ Removes head of stack 'stack' and returns it """
        elem = stack.elements[-1]
        del stack.elements[-1]
        return elem

    def empty(stack):
        """ Checks whether stack 'stack' is empty """
        return len(stack.elements) == 0


if __name__ == '__main__':
    n = 5

    print("stack:")
    stack = Stack()
    for i in range(n):
        Stack.push(stack, i ** 3)
    while not Stack.empty(stack):
        elem = Stack.pop(stack)
        print(elem)

    print("otherstack:")
    otherstack = Stack()
    for i in range(n):
        otherstack.push(1 / (i + 1))
    while not otherstack.empty():
        elem = otherstack.pop()
        print(elem)
