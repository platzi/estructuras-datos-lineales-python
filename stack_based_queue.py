

class Queue:
    def __init__(self):
        self.inbound_stack = []
        self.outbound_stack = []

    def enqueue(self, data):
        self.inbound_stack.append(data)

    def dequeue(self):
        if not self.outbound_stack:
            while self.inbound_stack:
                self.outbound_stack.append(self.inbound_stack.pop())

        return self.outbound_stack.pop()

"""
x = Queue()
x.enqueue(5)
x.enqueue(6)
x.enqueue(7)
print(x.inbound_stack)
x.dequeue()
print(x.inbound_stack)
print(x.outbound_stack)
x.dequeue()
print(x.outbound_stack)
"""