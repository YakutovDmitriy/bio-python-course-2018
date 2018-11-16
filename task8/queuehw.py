class QueueNode:
    """ Node: Class for single node of LinkedQueue """

    def __init__(self, elem, nextnode):
        """ Initializes new node """
        pass


class QueueIterator:
    """ QueueIterator: Iterator for LinkedQueue """

    def __init__(self, node, emptynode):
        """ Initializes new Iterator """
        pass

    def __next__(self):
        """ Returns next element of queue: next(iter) """
        pass


class LinkedQueue:
    """ LinkedQueue """

    def __init__(self):
        """ Initializes new queue """
        pass

    def push(self, elem):
        """ Pushes 'elem' to queue """
        pass

    def pop(self):
        """ Removes front of queue and returns it """
        pass

    def front(self):
        """ Returns front of queue """
        pass

    def empty(self):
        """ Checks whether queue is empty """
        pass

    def __iter__(self):
        """ Returns Iterator for queue: iter(queue) """
        pass

    def __len__(self):
        """ Returns size of queue: len(queue) """
        pass

    def clear(self):
        """ Makes queue empty """
        pass
