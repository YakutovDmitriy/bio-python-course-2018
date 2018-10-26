

class StackSingle:
    """ Stack: Module implementation """
    elements = []

    @staticmethod
    def push(elem):
        """ Pushes 'elem' to stack """
        StackSingle.elements.append(elem)

    @staticmethod
    def pop():
        """ Removes head of stack and returns it """
        elem = StackSingle.elements[-1]
        del StackSingle.elements[-1]
        return elem

    @staticmethod
    def empty():
        """ Checks whether stack is empty """
        return len(StackSingle.elements) == 0


if __name__ == '__main__':
    n = 5

    print("stack:")
    for i in range(n):
        StackSingle.push(i ** 3)
    while not StackSingle.empty():
        elem = StackSingle.pop()
        print(elem)
