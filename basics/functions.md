# Functions in Python

## Overview
Functions are reusable blocks of code that perform specific tasks. They help organize code, reduce repetition, and make programs more modular and maintainable.

## Basic Function Syntax

```python
def function_name(parameters):
    """Optional docstring"""
    # Function body
    return value  # Optional
```

## Function Components

### 1. Function Definition
```python
def greet(name):
    """Greet a person by name."""
    return f"Hello, {name}!"
```

### 2. Function Call
```python
message = greet("Alice")
print(message)  # Output: Hello, Alice!
```

## Parameters and Arguments

### Positional Parameters
```python
def add(a, b):
    return a + b

result = add(5, 3)  # a=5, b=3
```

### Default Parameters
```python
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

print(greet("Alice"))           # Hello, Alice!
print(greet("Bob", "Hi"))       # Hi, Bob!
```

### Keyword Arguments
```python
def create_user(name, age, city="Unknown"):
    return f"{name}, {age}, {city}"

# Using keyword arguments
user = create_user(age=25, name="Alice", city="NYC")
```

### Variable-Length Arguments

#### *args (Positional)
```python
def sum_all(*args):
    return sum(args)

print(sum_all(1, 2, 3, 4))  # 10
```

#### **kwargs (Keyword)
```python
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=30, city="NYC")
```

#### Combined
```python
def flexible_func(*args, **kwargs):
    print("Args:", args)
    print("Kwargs:", kwargs)

flexible_func(1, 2, 3, name="Alice", age=30)
```

## Return Values

### Single Return
```python
def square(x):
    return x ** 2
```

### Multiple Returns
```python
def divide_with_remainder(a, b):
    quotient = a // b
    remainder = a % b
    return quotient, remainder

q, r = divide_with_remainder(17, 5)  # q=3, r=2
```

### No Return (None)
```python
def print_message(msg):
    print(msg)
    # Implicitly returns None
```

## Variable Scope

### Local Scope
```python
def my_function():
    local_var = "I'm local"
    print(local_var)

# local_var is not accessible outside the function
```

### Global Scope
```python
global_var = "I'm global"

def access_global():
    print(global_var)  # Can read global

def modify_global():
    global global_var
    global_var = "Modified"  # Can modify with 'global'
```

### Nonlocal Scope
```python
def outer():
    x = "outer"
    
    def inner():
        nonlocal x
        x = "modified by inner"
    
    inner()
    print(x)  # "modified by inner"
```

## Advanced Function Concepts

### Lambda Functions
```python
# Regular function
def square(x):
    return x ** 2

# Lambda equivalent
square_lambda = lambda x: x ** 2

# Common use with higher-order functions
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
```

### Higher-Order Functions
Functions that take other functions as arguments or return functions.

```python
def apply_operation(numbers, operation):
    return [operation(x) for x in numbers]

def double(x):
    return x * 2

result = apply_operation([1, 2, 3], double)  # [2, 4, 6]
```

### Closures
```python
def create_multiplier(factor):
    def multiplier(number):
        return number * factor
    return multiplier

double = create_multiplier(2)
triple = create_multiplier(3)

print(double(5))  # 10
print(triple(5))  # 15
```

### Decorators (Basic)
```python
def my_decorator(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
# Output:
# Before function call
# Hello!
# After function call
```

## Recursion

### Basic Recursion
```python
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))  # 120
```

### Tail Recursion (Optimization)
```python
def factorial_tail(n, accumulator=1):
    if n <= 1:
        return accumulator
    return factorial_tail(n - 1, n * accumulator)
```

## Function Annotations

### Type Hints
```python
def add_numbers(a: int, b: int) -> int:
    """Add two integers and return the result."""
    return a + b

def process_names(names: list[str]) -> dict[str, int]:
    """Return a dictionary with name lengths."""
    return {name: len(name) for name in names}
```

## Built-in Functions for Functional Programming

### map()
```python
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
# [1, 4, 9, 16, 25]
```

### filter()
```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = list(filter(lambda x: x % 2 == 0, numbers))
# [2, 4, 6, 8, 10]
```

### reduce()
```python
from functools import reduce

numbers = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers)
# 120 (1*2*3*4*5)
```

## Best Practices

### 1. Function Naming
```python
# Good
def calculate_area(length, width):
    return length * width

# Avoid
def calc(l, w):
    return l * w
```

### 2. Single Responsibility
```python
# Good - each function has one responsibility
def read_file(filename):
    with open(filename, 'r') as f:
        return f.read()

def process_text(text):
    return text.upper().strip()

# Avoid - function doing too much
def read_and_process_file(filename):
    with open(filename, 'r') as f:
        text = f.read()
    return text.upper().strip()
```

### 3. Use Docstrings
```python
def calculate_bmi(weight, height):
    """
    Calculate Body Mass Index.
    
    Args:
        weight (float): Weight in kilograms
        height (float): Height in meters
    
    Returns:
        float: BMI value
    
    Raises:
        ValueError: If height is zero or negative
    """
    if height <= 0:
        raise ValueError("Height must be positive")
    return weight / (height ** 2)
```

### 4. Avoid Mutable Default Arguments
```python
# Wrong
def add_item(item, my_list=[]):
    my_list.append(item)
    return my_list

# Correct
def add_item(item, my_list=None):
    if my_list is None:
        my_list = []
    my_list.append(item)
    return my_list
```

## Common Patterns

### Factory Functions
```python
def create_person(name, age):
    return {
        'name': name,
        'age': age,
        'greet': lambda: f"Hi, I'm {name}"
    }

person = create_person("Alice", 30)
print(person['greet']())  # Hi, I'm Alice
```

### Callback Functions
```python
def process_data(data, callback):
    result = [x * 2 for x in data]
    callback(result)

def print_result(result):
    print(f"Result: {result}")

process_data([1, 2, 3], print_result)
```

## Error Handling in Functions

```python
def safe_divide(a, b):
    """Safely divide two numbers."""
    try:
        return a / b
    except ZeroDivisionError:
        return None
    except TypeError:
        raise ValueError("Arguments must be numbers")

# Usage
result = safe_divide(10, 2)  # 5.0
result = safe_divide(10, 0)  # None
```

## Practice Exercises

1. **Basic Functions**: Create functions for mathematical operations
2. **Parameter Practice**: Write functions with different parameter types
3. **Return Values**: Create functions that return multiple values
4. **Recursion**: Implement recursive algorithms (factorial, Fibonacci)
5. **Higher-Order**: Write functions that accept other functions
6. **Decorators**: Create simple decorators for logging or timing
7. **Lambda**: Use lambda functions with map, filter, and sorted
8. **Error Handling**: Add proper error handling to functions