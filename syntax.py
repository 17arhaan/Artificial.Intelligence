# Variables and Data Types
x = 10  # Integer
y = 3.14  # Float
name = "Alice"  # String
is_active = True  # Boolean
numbers = [1, 2, 3, 4, 5]  # List
coordinates = (10.0, 20.0)  # Tuple
person = {"name": "Alice", "age": 30}  # Dictionary
unique_numbers = {1, 2, 3, 4, 5}  # Set

# Control Flow
# If Statements
if x > 5:
    print("x is greater than 5")
elif x == 5:
    print("x is 5")
else:
    print("x is less than 5")

# For Loop
for number in numbers:
    print(number)

# While Loop
count = 0
while count < 5:
    print(count)
    count += 1

# Functions
def greet(name):
    return f"Hello, {name}!"

message = greet("Alice")
print(message)

# Classes and Objects
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."

# Creating an object
person1 = Person("Alice", 30)
print(person1.greet())

# List Comprehensions
squares = [x**2 for x in range(10)]
print(squares)

# Exception Handling
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
finally:
    print("This will always execute.")

# File Operations
# Writing to a file
with open('example.txt', 'w') as file:
    file.write("Hello, World!")

# Reading from a file
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)

# Modules and Imports
import math

print(math.sqrt(16))  # Output: 4.0

# Lambda Functions
add = lambda a, b: a + b
print(add(2, 3))  # Output: 5

# Map, Filter, Reduce
from functools import reduce

# Using map
squared_numbers = list(map(lambda x: x**2, numbers))
print(squared_numbers)

# Using filter
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)

# Using reduce
sum_of_numbers = reduce(lambda a, b: a + b, numbers)
print(sum_of_numbers)
