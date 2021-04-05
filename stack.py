"""
Code used for the class 'Crear un stack'.
"""


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, data):
        """ Appends an element on top. """
        node = Node(data)

        if self.top:
            node.next = self.top
            self.top = node
        else:
            self.top = node

        self.size += 1

    def pop(self):
        """ Removes and returns the element on top. """
        if self.top:
            data = self.top.data
            self.size -= 1

            if self.top.next:
                self.top = self.top.next
            else:
                self.top = None

            return data
        else:
            return "The stack is empty"

    def peek(self):
        if self.top:
            return self.top.data
        else:
            return "The stack is empty"

    def clear(self):
        while self.top:
            self.pop()