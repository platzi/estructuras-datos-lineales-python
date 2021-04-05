
"""
Code used for the 'Singly linked list' class.
"""

class Node:
    "Represents a single linked node."
    def __init__(self, data, next = None):
        self.data = data
        self.next = None

    def __str__(self):
        "String representation of the node data."
        return str(self.data)

    def __repr__(self):
        "Simple representation of the node."
        return self.data

class SinglyLinkedList:
    "Represents a singly linked list made of several Node instances."
    def __init__(self):
        self.tail = None
        self.size = 0

    def append(self, data):
        "Encapsulates the data in a Node class."
        node = Node(data)

        if self.tail == None:
            self.tail = node
        else:
            current = self.tail

            while current.next:
                current = current.next

            current.next = node

        self.size += 1

    def size(self):
        "Returns the number of nodes in the list."
        return str(self.size)

    def iter(self):
        "Iters through the list."
        current = self.tail

        while current:
            val = current.data
            current = current.next
            yield val

    def delete(self, data):
        "Removes an element in the singly linked list."
        current = self.tail
        previous = self.tail

        while current:
            if current.data == data:
                if current == self.tail:
                    self.tail = current.next
                else:
                    previous.next = current.next
                    self.size -= 1
                    return current.data

            previous = current
            current = current.next

    def search(self, data):
        "Looks for a specific element in the list."
        for node in self.iter():
            if data == node:
                print(f"Data {data} found")

    def clear(self):
        "Clear the entire list."
        self.tail = None
        self.head = None
        self.size = 0


"""
Ejemplo en shell de SinglyLinkedList con append

words = SinglyLinkedList()
words.append('egg')
words.append('ham')
words.append('spam')

current = words.tail

while current:
    print(current.data)
    current = current.next

for word in words.iter():
    print(word)

words.search('eggs')
"""