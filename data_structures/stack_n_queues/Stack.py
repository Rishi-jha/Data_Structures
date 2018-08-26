#/usr/bin/python


class Stack(object):
    """
    Implementation of Stack in python.
    Usage:
        s = Stack([size])
        Optional Argument size, Restricts the size of Stack.
    """
    MAXSIZE = None

    def __init__(self, size=None):
        """
        :param size: Max Size limit of stack
        :type size: Integer
        """
        self.top = 0
        if size is not None and size <= 0:
            raise ValueError("Size Could not be less than 1 if provided")
        self.MAXSIZE = size
        self.stack = []

    def push(self, val):
        """
        Add the element in the stack.
        :param val: value to be added
        :type val: Object
        """
        if self.MAXSIZE is not None:
            if self.top + 1 > self.MAXSIZE:
                raise RuntimeError("StackOverFlow Exception: MAXSIZE of Stack: {}".format(self.MAXSIZE))
        self.stack.append(val)
        self.top += 1

    def pop(self):
        """
        Return the last object added in the Stack and removes it.
        """
        if self.top == 0:
            raise RuntimeError("UnderFlow Exception: No Elements in the Stack")
        self.top -= 1
        return self.stack.pop()
        

    def peek(self):
        """
        Returns the last inserted element without removing it from the Stack
        """
        if self.top == 0:
            return None
        return self.stack[-1]

    def is_empty(self):
        """
        Method to check if the current Stack is empty
        """
        return self.top == 0

