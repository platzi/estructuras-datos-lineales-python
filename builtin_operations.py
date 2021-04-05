"""
Code used during the class 'Operaciones esenciales en colecciones'
Demonstration of common methods for data structures.
"""

# Creating list with different elements
[]
["Isabel"]
["Isabel", "Mulan"]
["Isabel", "Mulan", 255]
["Isabel", ["Mulan", 255]]

# Typical data structure operations in Python
fruits = []
fruits.append("Kiwi")
fruits.append("Berry")
fruits.append("Melon")
fruits.sort()
fruits.pop()
fruits.insert(0, "Apple")
fruits.insert(1, "Strawberry")
fruits.pop(1)
fruits.remove("Apple")
# fruits.remove("Dragon fruit")

def pyramid_sum(lower, upper, margin = 0):
    """Returns the sum of the numbers from lower to upper,
    and outputs a trace of the arguments and return values
    on each call."""
    blanks = " " * margin
    print(blanks, lower, upper) # Print the arguments

    if lower > upper:
        print(blanks, 0) # Print the returned value
        return 0
    else:
        result = lower + pyramid_sum(lower + 1, upper, margin + 4)
        print(blanks, result) # Print the returned value
        return result

pyramid_sum(1, 4)