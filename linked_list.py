"""
Code used for the class 'Nodos y singly linked list'.

All the code but the 'Node' class is written in the shell
for demonstrative purposes.

The node methods should be incorporated into the Node class.
"""

class Node(object):
    "Represents a single linked node."
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

# Creating 3 differents nodes 
node1 = None
node2 = Node("A", None)
node3 = Node("B", node2)

# This causes an Atribute Error
# node1.next = node3

node1 = Node("C", node3)

# Creating a linked list
head = None
# Add five nodes to the beginning of the linked structure
for count in range(1, 3):
    head = Node(count, head)
# Print the contents of the structure

while head != None:
    print(head.data)
    head = head.next


""" Main linked lists operations """
# Traversal with 'probe' as aux. variable
probe = head

while probe != None:
    print(probe.data)
    probe = probe.next


# Search an item
probe = head
target_item = 2
while probe != None and target_item != probe.data:
    probe = probe.next

if probe != None:
    print(f"Target item {target_item} has been found")
else:
    print(f"Target item {target_item} is not in the linked list")


# Replacement
probe = head
target_item = 3
new_item = "Z"
while probe != None and target_item != probe.data:
    probe = probe.next

if probe != None:
    probe.data = new_item
    print(f"{new_item} replaced the old value in the node number {target_item}")
else:
    print(f"The target item {target_item} is not in the linked list")


# Insert new element at the beginning
head = Node("F", head)


# Insert at the end
new_node = Node("K")

if head is None:
    head = new_node
else:
    probe = head
    while probe.next != None:
        probe = probe.next

    probe.next = new_node


# Remove at the beginning
removed_item = head.data
head = head.next
print(removed_item)


# Remove at the end
removed_item = head.data

if head.next is None:
    head = None
else:
    probe = head

    while probe.next.next != None:
        probe = probe.next

    removed_item = probe.next.data
    probe.next = None

print(removed_item)


# Insert at any position
new_item = input("Enter the new item: ")
index = int(input("Enter the position to inser the new item: "))
if head is None or index < 0:
    head = Node("Py", head)
else:
    # Search for node at position index - 1 or the last position
    probe = head

    while index > 1 and probe.next != None:
        probe = probe.next
        index -= 1

    probe.next = Node(new_item, probe.next)


# Remove at any position
index = 3

if index <= 0 or head.next is None:
    removed_item = head.data
    head = head.next
    print(removed_item)
else:
    # Search for nod at position index - 1
    # or the next to last position
    probe = head

    while index > 1 and probe.next.next != None:
        probe = probe.next
        index -= 1

    removed_item = probe.next.data
    probe.next = probe.next.next
    print(removed_item)