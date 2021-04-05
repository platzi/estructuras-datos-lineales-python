"""
Code used for the 'Crear un array' class.

Array type class
Methods:
    1. Length
    2. String representation
    3. Membership
    4. Index.
    5. Replacement
"""

class Array(object):
    "Represents an array."

    def __init__(self, capacity, fill_value = None):
        """
        Args:
            capacity (int): static size of the array.
            fill_value (any, optional): value at each position. Defaults to None.
        """
        self.items = list()
        for i in range(capacity):
            self.items.append(fill_value)

    def __len__(self):
        """Returns capacity of the array."""
        return len(self.items)

    def __str__(self):
        """Returns string representation of the array"""
        return str(self.items)

    def __iter__(self):
        """Supports traversal with a for loop."""
        return iter(self.items)

    def __getitem__(self, index):
        """Subscrit operator for access at index."""
        return self.items[index]

    def __setitem__(self, index, new_item):
        """Subscript operator for replacement at index."""
        self.items[index] = new_item


"""
Code used in the shell to create an array
instance and methods.
"""

"""
from array import Array
menu = Array(5)
len(menu)
print(menu)
for i in range(len(menu)):
    menu[i] = i + 1
menu[0]
menu[2]
for item in menu:
    print(menu)

menu.__len__()
menu.__str__()
menu.__iter__()
menu.__getitem__(2)
menu.__setitem__(2, 100)
menu.__getitem__(2)
"""