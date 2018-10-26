

class StackADT:
    """ Stack: Abstract Data Type (ADT) implementation """

    @staticmethod
    def createstack():
        """ Creates and returns new stack """
        return []

    @staticmethod
    def push(elements, elem):
        """ Pushes 'elem' to stack 'elements' """
        elements.append(elem)

    @staticmethod
    def pop(elements):
        """ Removes head of stack 'elements' and returns it """
        elem = elements[-1]
        del elements[-1]
        return elem

    @staticmethod
    def empty(elements):
        """ Checks whether stack 'elements' is empty """
        return len(elements) == 0


if __name__ == '__main__':
    n = 5

    print("stack:")
    stack = StackADT.createstack()
    for i in range(n):
        StackADT.push(stack, i ** 3)
    while not StackADT.empty(stack):
        elem = StackADT.pop(stack)
        print(elem)
