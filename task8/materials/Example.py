

class MathFunctions:
    """ Namespace with mathematical functions """

    @staticmethod
    def factorial(n):
        """ Returns factorial of non-negative integer n """
        if n == 0:
            return 1
        return n * MathFunctions.factorial(n - 1)

    @staticmethod
    def cube(n):
        """ Returns n ** 3 """
        return n ** 3


class ListFunctions:
    """ Namespace with operations with lists """

    @staticmethod
    def twice(a):
        """ Modify list a:  a = a + a """
        a.extend(a)

    @staticmethod
    def gethead(a):
        """ returns first element of list a """
        return a[0]


if __name__ == '__main__':
    print(MathFunctions.factorial(4))
    print(MathFunctions.cube(20))

    a = [1, 2, 3]
    ListFunctions.twice(a)
    print(a)
    print(ListFunctions.gethead(a))
