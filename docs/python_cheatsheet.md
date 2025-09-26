# Python Quick Reference Cheat Sheet

**Created by: Syed Ali Hashmi**  
**LinkedIn: [https://www.linkedin.com/in/hashmiali2288](https://www.linkedin.com/in/hashmiali2288)**

## 📋 Basic Syntax

### Variables and Data Types
```python
# Numbers
integer = 42
float_num = 3.14
complex_num = 3 + 4j

# Strings
name = "Alice"
message = f"Hello, {name}!"

# Booleans
is_active = True
is_complete = False

# Collections
my_list = [1, 2, 3, 4]
my_tuple = (1, 2, 3)
my_dict = {"key": "value", "age": 30}
my_set = {1, 2, 3, 4}
```

### Control Flow
```python
# If statements
if condition:
    pass
elif other_condition:
    pass
else:
    pass

# For loops
for item in iterable:
    pass

for i in range(10):
    pass

# While loops
while condition:
    pass

# Loop control
break    # Exit loop
continue # Skip to next iteration
```

### Functions
```python
# Basic function
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

# Lambda function
square = lambda x: x ** 2

# Decorator
@decorator
def function():
    pass
```

### Classes
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greet(self):
        return f"Hi, I'm {self.name}"
    
    @property
    def adult(self):
        return self.age >= 18
```

## 🔧 Built-in Functions

### Common Functions
```python
len(obj)           # Length of object
type(obj)          # Type of object
str(obj)           # Convert to string
int(obj)           # Convert to integer
float(obj)         # Convert to float
bool(obj)          # Convert to boolean

print(*args)       # Print to console
input(prompt)      # Get user input

min(iterable)      # Minimum value
max(iterable)      # Maximum value
sum(iterable)      # Sum of values
sorted(iterable)   # Sorted list
reversed(iterable) # Reversed iterator

enumerate(iterable)    # Index-value pairs
zip(iter1, iter2)     # Combine iterables
range(start, stop, step) # Number sequence
```

### String Methods
```python
s = "Hello World"

s.upper()          # "HELLO WORLD"
s.lower()          # "hello world"
s.strip()          # Remove whitespace
s.replace(old, new) # Replace substring
s.split(delimiter) # Split into list
s.join(iterable)   # Join with separator
s.startswith(prefix) # Check prefix
s.endswith(suffix)   # Check suffix
s.find(substring)    # Find position
s.count(substring)   # Count occurrences
```

### List Methods
```python
lst = [1, 2, 3]

lst.append(item)     # Add to end
lst.insert(i, item)  # Insert at position
lst.remove(item)     # Remove first occurrence
lst.pop(i)          # Remove and return item
lst.index(item)     # Find position
lst.count(item)     # Count occurrences
lst.sort()          # Sort in place
lst.reverse()       # Reverse in place
lst.copy()          # Shallow copy
```

### Dictionary Methods
```python
d = {"a": 1, "b": 2}

d.keys()           # Dict keys
d.values()         # Dict values
d.items()          # Key-value pairs
d.get(key, default) # Safe get
d.pop(key)         # Remove and return
d.update(other)    # Merge dictionaries
d.clear()          # Remove all items
```

## 📁 File Operations

### Basic File I/O
```python
# Read file
with open("file.txt", "r") as f:
    content = f.read()
    lines = f.readlines()

# Write file
with open("file.txt", "w") as f:
    f.write("Hello")
    f.writelines(["line1\n", "line2\n"])

# Append to file
with open("file.txt", "a") as f:
    f.write("More content")
```

### JSON Operations
```python
import json

# Read JSON
with open("data.json", "r") as f:
    data = json.load(f)

# Write JSON
with open("data.json", "w") as f:
    json.dump(data, f, indent=2)

# String conversion
json_string = json.dumps(data)
data = json.loads(json_string)
```

## 🚨 Error Handling

### Try-Except
```python
try:
    risky_operation()
except SpecificError as e:
    handle_error(e)
except (Error1, Error2):
    handle_multiple_errors()
except Exception as e:
    handle_any_error(e)
else:
    # Runs if no exception
    pass
finally:
    # Always runs
    cleanup()
```

### Common Exceptions
```python
ValueError      # Invalid value
TypeError       # Wrong type
KeyError        # Missing dict key
IndexError      # List index out of range
FileNotFoundError # File doesn't exist
ZeroDivisionError # Division by zero
AttributeError    # Missing attribute
ImportError       # Import failed
```

## 📦 Modules and Packages

### Importing
```python
import module
import module as alias
from module import function
from module import function as alias
from module import *

# Relative imports (in packages)
from . import module
from ..parent import module
```

### Standard Library
```python
import os          # Operating system
import sys         # System-specific
import math        # Mathematical functions
import random      # Random numbers
import datetime    # Date and time
import json        # JSON handling
import re          # Regular expressions
import collections # Specialized containers
import itertools   # Iterator functions
import functools   # Higher-order functions
```

## 🎯 List Comprehensions

### Basic Syntax
```python
# List comprehension
[expression for item in iterable]
[expression for item in iterable if condition]

# Examples
squares = [x**2 for x in range(10)]
evens = [x for x in range(20) if x % 2 == 0]
words = [word.upper() for word in text.split()]

# Nested
matrix = [[i*j for j in range(3)] for i in range(3)]
flattened = [item for row in matrix for item in row]
```

### Other Comprehensions
```python
# Dictionary comprehension
{k: v for k, v in items}
{x: x**2 for x in range(5)}

# Set comprehension
{expression for item in iterable}
{x**2 for x in range(10)}

# Generator expression
(expression for item in iterable)
sum(x**2 for x in range(1000000))
```

## 🔄 Iterators and Generators

### Generators
```python
# Generator function
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Generator expression
squares = (x**2 for x in range(10))

# Using generators
for num in fibonacci():
    if num > 100:
        break
    print(num)
```

### Iterator Protocol
```python
class Counter:
    def __init__(self, max_count):
        self.max_count = max_count
        self.count = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.count < self.max_count:
            self.count += 1
            return self.count
        raise StopIteration
```

## 🎨 Decorators

### Function Decorators
```python
def my_decorator(func):
    def wrapper(*args, **kwargs):
        # Before function
        result = func(*args, **kwargs)
        # After function
        return result
    return wrapper

@my_decorator
def my_function():
    pass

# Parameterized decorator
def repeat(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def greet():
    print("Hello!")
```

### Built-in Decorators
```python
class MyClass:
    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, val):
        self._value = val
    
    @staticmethod
    def static_method():
        pass
    
    @classmethod
    def class_method(cls):
        pass
```

## 🧮 Regular Expressions

```python
import re

# Common patterns
re.match(pattern, string)    # Match at start
re.search(pattern, string)   # Search anywhere
re.findall(pattern, string)  # Find all matches
re.sub(pattern, repl, string) # Replace matches

# Pattern examples
r'\d+'          # One or more digits
r'\w+'          # One or more word characters
r'\s+'          # One or more whitespace
r'[a-zA-Z]+'    # Letters only
r'^\w+@\w+\.\w+$' # Simple email pattern

# Groups
match = re.search(r'(\d{4})-(\d{2})-(\d{2})', '2023-12-25')
year, month, day = match.groups()
```

## 🕒 Date and Time

```python
from datetime import datetime, date, timedelta

# Current time
now = datetime.now()
today = date.today()

# Create specific date/time
dt = datetime(2023, 12, 25, 10, 30, 0)
d = date(2023, 12, 25)

# Formatting
dt.strftime('%Y-%m-%d %H:%M:%S')  # "2023-12-25 10:30:00"
dt.strftime('%B %d, %Y')          # "December 25, 2023"

# Parsing
dt = datetime.strptime('2023-12-25', '%Y-%m-%d')

# Arithmetic
tomorrow = today + timedelta(days=1)
week_ago = now - timedelta(weeks=1)
```

## 🔢 Math Operations

```python
import math

# Basic operations
abs(-5)        # Absolute value: 5
round(3.7)     # Round: 4
pow(2, 3)      # Power: 8
divmod(17, 5)  # Division and remainder: (3, 2)

# Math module
math.ceil(3.2)   # Ceiling: 4
math.floor(3.8)  # Floor: 3
math.sqrt(16)    # Square root: 4.0
math.log(10)     # Natural log
math.log10(100)  # Base-10 log: 2.0
math.sin(math.pi/2) # Sine: 1.0
math.pi          # Pi constant
math.e           # Euler's number
```

## 🎲 Random Operations

```python
import random

random.random()              # Float 0.0 to 1.0
random.randint(1, 10)        # Integer 1 to 10
random.choice([1, 2, 3])     # Random choice
random.shuffle(my_list)      # Shuffle in place
random.sample(population, k) # Sample k items
```

## 💾 Collections Module

```python
from collections import Counter, defaultdict, deque, namedtuple

# Counter
count = Counter(['a', 'b', 'a', 'c', 'b', 'a'])
# Counter({'a': 3, 'b': 2, 'c': 1})

# defaultdict
dd = defaultdict(list)
dd['key'].append('value')  # No KeyError

# deque (double-ended queue)
dq = deque([1, 2, 3])
dq.appendleft(0)  # [0, 1, 2, 3]
dq.pop()          # 3

# namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p.x, p.y)  # 1 2
```

## 🔍 Useful Patterns

### Enumerate with Start
```python
for i, item in enumerate(items, start=1):
    print(f"{i}. {item}")
```

### Zip for Parallel Iteration
```python
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]
for name, age in zip(names, ages):
    print(f"{name} is {age} years old")
```

### Dictionary from Lists
```python
keys = ['a', 'b', 'c']
values = [1, 2, 3]
d = dict(zip(keys, values))  # {'a': 1, 'b': 2, 'c': 3}
```

### Swapping Variables
```python
a, b = b, a
```

### Multiple Assignment
```python
x, y, z = 1, 2, 3
first, *middle, last = [1, 2, 3, 4, 5]
```

### Conditional Assignment
```python
value = x if condition else y
```

### Safe Dictionary Access
```python
value = d.get('key', 'default')
```

### String Formatting
```python
# f-strings (Python 3.6+)
name = "Alice"
age = 30
message = f"Hello, {name}! You are {age} years old."

# Format method
message = "Hello, {}! You are {} years old.".format(name, age)
message = "Hello, {name}! You are {age} years old.".format(name=name, age=age)

# % formatting (older)
message = "Hello, %s! You are %d years old." % (name, age)
```