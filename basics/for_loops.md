# For Loops in Python

**Created by: Syed Ali Hashmi**  
**LinkedIn: [https://www.linkedin.com/in/hashmiali2288](https://www.linkedin.com/in/hashmiali2288)**

## Overview
For loops in Python are used to iterate over sequences (lists, tuples, strings) and other iterable objects. They provide a clean and efficient way to repeat operations.

## Basic Syntax

```python
for item in iterable:
    # Code to execute for each item
    pass
```

## Iterating Over Different Data Types

### Lists
```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```

### Strings
```python
word = "Python"
for char in word:
    print(char)
```

### Tuples
```python
coordinates = (10, 20, 30)
for coord in coordinates:
    print(coord)
```

### Dictionaries
```python
person = {"name": "Alice", "age": 30, "city": "NYC"}

# Iterate over keys (default)
for key in person:
    print(key)

# Iterate over values
for value in person.values():
    print(value)

# Iterate over key-value pairs
for key, value in person.items():
    print(f"{key}: {value}")
```

## The range() Function

### Basic Usage
```python
# range(stop)
for i in range(5):
    print(i)  # 0, 1, 2, 3, 4

# range(start, stop)
for i in range(2, 7):
    print(i)  # 2, 3, 4, 5, 6

# range(start, stop, step)
for i in range(0, 10, 2):
    print(i)  # 0, 2, 4, 6, 8
```

### Negative Steps
```python
# Counting backwards
for i in range(10, 0, -1):
    print(i)  # 10, 9, 8, 7, 6, 5, 4, 3, 2, 1
```

### Practical Examples
```python
# Accessing list indices
colors = ["red", "green", "blue"]
for i in range(len(colors)):
    print(f"Index {i}: {colors[i]}")

# Creating multiplication table
for i in range(1, 11):
    print(f"5 × {i} = {5 * i}")
```

## enumerate() Function

Get both index and value while iterating:

```python
languages = ["Python", "Java", "JavaScript"]

# Basic enumerate
for index, language in enumerate(languages):
    print(f"{index}: {language}")

# Custom start value
for index, language in enumerate(languages, start=1):
    print(f"{index}. {language}")
```

## zip() Function

Iterate over multiple sequences simultaneously:

```python
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
cities = ["NYC", "LA", "Chicago"]

for name, age, city in zip(names, ages, cities):
    print(f"{name} is {age} years old and lives in {city}")

# Creating dictionaries
student_grades = dict(zip(names, [95, 87, 92]))
```

## Nested Loops

### Basic Nested Loops
```python
# Multiplication table
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} × {j} = {i * j}")
```

### Matrix Operations
```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in matrix:
    for element in row:
        print(element, end=" ")
    print()  # New line after each row
```

## Loop Control Statements

### break Statement
Exits the loop prematurely:

```python
numbers = [1, 3, 5, 8, 9, 12]
for num in numbers:
    if num % 2 == 0:
        print(f"First even number: {num}")
        break
    print(f"Odd number: {num}")
```

### continue Statement
Skips the current iteration:

```python
numbers = [-2, 5, -1, 8, -3, 12]
for num in numbers:
    if num < 0:
        continue  # Skip negative numbers
    print(f"Positive: {num}")
```

### pass Statement
Does nothing (placeholder):

```python
for i in range(5):
    if i == 2:
        pass  # TODO: Add special handling later
    else:
        print(i)
```

## else Clause with Loops

The `else` clause executes if the loop completes normally (not broken):

```python
numbers = [1, 3, 5, 7, 9]
search_target = 6

for num in numbers:
    if num == search_target:
        print(f"Found {search_target}!")
        break
else:
    print(f"{search_target} not found in the list")
```

## List Comprehensions

A concise way to create lists using loops:

### Basic Syntax
```python
# Traditional loop
squares = []
for x in range(10):
    squares.append(x ** 2)

# List comprehension
squares = [x ** 2 for x in range(10)]
```

### With Conditions
```python
# Even squares only
even_squares = [x ** 2 for x in range(10) if x % 2 == 0]

# Conditional expression
abs_values = [x if x >= 0 else -x for x in [-2, 1, -3, 4]]
```

### Nested Comprehensions
```python
# Matrix creation
matrix = [[i * j for j in range(3)] for i in range(3)]

# Flattening a matrix
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in matrix for num in row]
```

## Advanced Iteration Techniques

### itertools Module
```python
import itertools

# Infinite sequences
counter = itertools.count(10, 2)  # 10, 12, 14, 16, ...

# Cycling through values
colors = itertools.cycle(['red', 'green', 'blue'])

# Chaining iterables
list1 = [1, 2, 3]
list2 = [4, 5, 6]
chained = itertools.chain(list1, list2)
```

### Generator Expressions
```python
# Memory-efficient iteration
squares_gen = (x ** 2 for x in range(1000000))
for square in squares_gen:
    if square > 100:
        break
    print(square)
```

## Performance Considerations

### Efficient Patterns
```python
# Good: Store reference to avoid repeated lookups
data = {"items": [1, 2, 3, 4, 5]}
items = data["items"]
for item in items:
    process(item)

# Avoid: Repeated dictionary lookup
for i in range(len(data["items"])):
    process(data["items"][i])
```

### Use Built-in Functions
```python
numbers = [1, 2, 3, 4, 5]

# Manual sum (slower)
total = 0
for num in numbers:
    total += num

# Built-in sum (faster)
total = sum(numbers)
```

## Common Patterns

### Processing Files
```python
with open('file.txt', 'r') as f:
    for line_num, line in enumerate(f, 1):
        print(f"Line {line_num}: {line.strip()}")
```

### Batch Processing
```python
def process_in_batches(items, batch_size):
    for i in range(0, len(items), batch_size):
        batch = items[i:i + batch_size]
        yield batch

data = list(range(100))
for batch in process_in_batches(data, 10):
    print(f"Processing batch: {batch}")
```

### Finding Items
```python
# Find first match
def find_first(items, condition):
    for item in items:
        if condition(item):
            return item
    return None

numbers = [1, 3, 5, 8, 9, 12]
first_even = find_first(numbers, lambda x: x % 2 == 0)
```

## Best Practices

### 1. Use Descriptive Variable Names
```python
# Good
for student_name in student_names:
    print(student_name)

# Avoid
for x in y:
    print(x)
```

### 2. Avoid Modifying Lists While Iterating
```python
# Wrong
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    if num % 2 == 0:
        numbers.remove(num)  # Dangerous!

# Correct
numbers = [num for num in numbers if num % 2 != 0]
```

### 3. Use enumerate() Instead of range(len())
```python
# Good
items = ['a', 'b', 'c']
for i, item in enumerate(items):
    print(f"{i}: {item}")

# Avoid
for i in range(len(items)):
    print(f"{i}: {items[i]}")
```

### 4. Use zip() for Parallel Iteration
```python
# Good
names = ['Alice', 'Bob']
ages = [25, 30]
for name, age in zip(names, ages):
    print(f"{name}: {age}")

# Avoid
for i in range(len(names)):
    print(f"{names[i]}: {ages[i]}")
```

## Common Mistakes

### 1. Late Binding in Loops
```python
# Problem
functions = []
for i in range(3):
    functions.append(lambda: i)  # All will return 2!

# Solution
functions = []
for i in range(3):
    functions.append(lambda x=i: x)  # Capture current value
```

### 2. Unnecessary List Creation
```python
# Inefficient
sum(range(1000000))  # Creates list in memory

# Efficient (Python 3)
sum(range(1000000))  # range is already an iterator
```

## Practice Exercises

1. **Basic Iteration**: Print all items in different data structures
2. **Range Practice**: Create patterns using range() with different parameters
3. **Enumerate Usage**: Number lines in a text file
4. **Zip Operations**: Combine multiple lists into structured data
5. **Nested Loops**: Create multiplication tables and patterns
6. **List Comprehensions**: Convert traditional loops to comprehensions
7. **Control Flow**: Use break/continue to control loop execution
8. **Performance**: Compare different iteration methods for speed