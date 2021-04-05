"""
Code used during the class 'Queues basadas en listas'.
"""

class ListQueue:
    def __init__(self):
        self.items = []
        self.size = 0

    def enqueue(self, data):
        self.items.insert(0, data)
        self.size += 1

    def dequeue(self):
        data = self.items.pop()
        self.size -= 1
        return data

    def traverse(self):
        total_items = self.size

        for item in total_items:
            print(self.items[item])


"""
Code used in the shell

x = ListQueue()
x.enqueue('eegs')
x.enqueue('ham')
x.enqueue('spam')
x.items

for i in range(x.size):
    print(x.items[i])

"""