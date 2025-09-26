# Common Python Mistakes and How to Avoid Them

**Created by: Syed Ali Hashmi**  
**LinkedIn: [https://www.linkedin.com/in/hashmiali2288](https://www.linkedin.com/in/hashmiali2288)**

## 1. Mutable Default Arguments

### The Problem
```python
# WRONG - Dangerous mutable default
def add_item(item, my_list=[]):
    my_list.append(item)
    return my_list

# This causes unexpected behavior
list1 = add_item("apple")      # ["apple"]
list2 = add_item("banana")     # ["apple", "banana"] - Unexpected!
```

### The Solution
```python
# CORRECT - Use None as default
def add_item(item, my_list=None):
    if my_list is None:
        my_list = []
    my_list.append(item)
    return my_list

# Or use copy for existing list
def add_item(item, my_list=None):
    if my_list is None:
        my_list = []
    else:
        my_list = my_list.copy()  # Don't modify original
    my_list.append(item)
    return my_list
```

## 2. Late Binding Closures

### The Problem
```python
# WRONG - All functions will return 3
functions = []
for i in range(4):
    functions.append(lambda: i)

# All functions return 3 (the final value of i)
for f in functions:
    print(f())  # 3, 3, 3, 3
```

### The Solution
```python
# CORRECT - Capture the variable
functions = []
for i in range(4):
    functions.append(lambda x=i: x)  # Capture current value

# Or use a closure
functions = []
for i in range(4):
    def make_func(n):
        return lambda: n
    functions.append(make_func(i))

# Now each function returns its expected value
for f in functions:
    print(f())  # 0, 1, 2, 3
```

## 3. Modifying Lists While Iterating

### The Problem
```python
# WRONG - Modifying list during iteration
numbers = [1, 2, 3, 4, 5, 6]
for num in numbers:
    if num % 2 == 0:
        numbers.remove(num)  # This skips elements!

print(numbers)  # [1, 3, 5, 6] - 6 wasn't removed!
```

### The Solution
```python
# CORRECT - Iterate over a copy
numbers = [1, 2, 3, 4, 5, 6]
for num in numbers[:]:  # Iterate over a copy
    if num % 2 == 0:
        numbers.remove(num)

# Or use list comprehension
numbers = [1, 2, 3, 4, 5, 6]
numbers = [num for num in numbers if num % 2 != 0]

# Or iterate backwards
numbers = [1, 2, 3, 4, 5, 6]
for i in range(len(numbers) - 1, -1, -1):
    if numbers[i] % 2 == 0:
        del numbers[i]
```

## 4. Using `is` Instead of `==`

### The Problem
```python
# WRONG - Using 'is' for value comparison
a = 1000
b = 1000
if a is b:  # May be False due to integer caching
    print("Same object")

# WRONG - Using 'is' with strings
name = "Alice"
if name is "Alice":  # Unreliable
    print("Name is Alice")
```

### The Solution
```python
# CORRECT - Use '==' for value comparison
a = 1000
b = 1000
if a == b:  # Always works for value comparison
    print("Same value")

# Use 'is' only for identity comparison
if value is None:  # Correct use of 'is'
    print("Value is None")

if value is True:  # Correct for singleton objects
    print("Value is True")
```

## 5. Catching Too Broad Exceptions

### The Problem
```python
# WRONG - Catching all exceptions
try:
    result = risky_operation()
    process_result(result)
except:  # Catches everything, including KeyboardInterrupt!
    print("Something went wrong")

# WRONG - Too broad exception handling
try:
    value = int(user_input)
    result = 100 / value
except Exception:  # Still too broad
    print("Error occurred")
```

### The Solution
```python
# CORRECT - Catch specific exceptions
try:
    value = int(user_input)
    result = 100 / value
except ValueError:
    print("Invalid number format")
except ZeroDivisionError:
    print("Cannot divide by zero")
except KeyboardInterrupt:
    print("Operation cancelled by user")
    raise  # Re-raise to allow proper handling
```

## 6. Not Using Context Managers

### The Problem
```python
# WRONG - Manual file handling
file = open("data.txt", "r")
data = file.read()
file.close()  # Easy to forget, especially with exceptions

# WRONG - Not handling exceptions
file = open("data.txt", "r")
data = file.read()
# If an exception occurs here, file won't be closed
process_data(data)
file.close()
```

### The Solution
```python
# CORRECT - Use context managers
with open("data.txt", "r") as file:
    data = file.read()
    process_data(data)
# File is automatically closed, even if exceptions occur

# For multiple resources
with open("input.txt", "r") as infile, \
     open("output.txt", "w") as outfile:
    data = infile.read()
    outfile.write(process_data(data))
```

## 7. Inefficient String Concatenation

### The Problem
```python
# WRONG - Inefficient string building
result = ""
for item in large_list:
    result += str(item) + ", "  # Creates new string each time

# WRONG - Using % formatting in loops
html = ""
for item in items:
    html += "<li>%s</li>" % item
```

### The Solution
```python
# CORRECT - Use join()
result = ", ".join(str(item) for item in large_list)

# For HTML
html = "".join(f"<li>{item}</li>" for item in items)

# Or use list and join
parts = []
for item in large_list:
    parts.append(str(item))
result = ", ".join(parts)
```

## 8. Not Understanding Truthiness

### The Problem
```python
# WRONG - Explicit comparison with True/False
if flag == True:  # Unnecessary
    do_something()

if len(my_list) > 0:  # Verbose
    process_list()

if my_string != "":  # Verbose
    process_string()
```

### The Solution
```python
# CORRECT - Use truthiness
if flag:  # More Pythonic
    do_something()

if my_list:  # Empty lists are falsy
    process_list()

if my_string:  # Empty strings are falsy
    process_string()

# Be explicit when checking for None
if value is not None:  # Correct
    process_value()

# Not this:
if value:  # Wrong if value could be 0, [], "", etc.
    process_value()
```

## 9. Using Global Variables Incorrectly

### The Problem
```python
# WRONG - Overusing global variables
counter = 0

def increment():
    global counter
    counter += 1  # Hard to test and debug

def get_count():
    global counter
    return counter
```

### The Solution
```python
# CORRECT - Use classes or pass parameters
class Counter:
    def __init__(self):
        self._count = 0
    
    def increment(self):
        self._count += 1
    
    def get_count(self):
        return self._count

# Or use function parameters
def increment(counter):
    return counter + 1

def process_with_counter(initial_count=0):
    count = initial_count
    # ... do work ...
    count = increment(count)
    return count
```

## 10. Not Using List Comprehensions Appropriately

### The Problem
```python
# WRONG - Overcomplicating simple loops
result = []
for item in items:
    result.append(item.upper())

# WRONG - Complex logic in comprehensions
result = [item.process().transform().validate() 
          if item.is_valid() and item.check_status() and complex_condition(item)
          else default_value if item.has_default() 
          else fallback_process(item) 
          for item in items 
          if item and item.active and item.type == 'special']
```

### The Solution
```python
# CORRECT - Simple list comprehension
result = [item.upper() for item in items]

# CORRECT - Use regular loop for complex logic
result = []
for item in items:
    if not item or not item.active or item.type != 'special':
        continue
    
    if item.is_valid() and item.check_status() and complex_condition(item):
        processed = item.process().transform().validate()
        result.append(processed)
    elif item.has_default():
        result.append(default_value)
    else:
        result.append(fallback_process(item))
```

## 11. Ignoring PEP 8 Style Guidelines

### The Problem
```python
# WRONG - Poor naming and formatting
def calculateUserAge(birthYear,currentYear):
    return currentYear-birthYear

class userAccount:
    def __init__(self,userName,userEmail):
        self.userName=userName
        self.userEmail=userEmail
```

### The Solution
```python
# CORRECT - Follow PEP 8
def calculate_user_age(birth_year, current_year):
    """Calculate user age from birth year."""
    return current_year - birth_year

class UserAccount:
    """Represents a user account."""
    
    def __init__(self, user_name, user_email):
        self.user_name = user_name
        self.user_email = user_email
```

## 12. Not Handling Unicode Properly

### The Problem
```python
# WRONG - Assuming ASCII
def process_text(text):
    return text.upper().encode('ascii')  # Fails with non-ASCII

# WRONG - Not specifying encoding
with open('file.txt', 'r') as f:  # Uses system default
    content = f.read()
```

### The Solution
```python
# CORRECT - Handle Unicode properly
def process_text(text):
    return text.upper()  # Works with Unicode

# CORRECT - Specify encoding explicitly
with open('file.txt', 'r', encoding='utf-8') as f:
    content = f.read()

# Handle encoding errors gracefully
try:
    with open('file.txt', 'r', encoding='utf-8') as f:
        content = f.read()
except UnicodeDecodeError:
    with open('file.txt', 'r', encoding='latin-1') as f:
        content = f.read()
```

## 13. Memory Leaks with Circular References

### The Problem
```python
# WRONG - Circular references
class Parent:
    def __init__(self):
        self.children = []
    
    def add_child(self, child):
        child.parent = self  # Circular reference
        self.children.append(child)

class Child:
    def __init__(self):
        self.parent = None
```

### The Solution
```python
# CORRECT - Use weak references
import weakref

class Parent:
    def __init__(self):
        self.children = []
    
    def add_child(self, child):
        child.parent = weakref.ref(self)  # Weak reference
        self.children.append(child)

class Child:
    def __init__(self):
        self.parent = None
    
    def get_parent(self):
        if self.parent is not None:
            return self.parent()  # Call weak reference
        return None
```

## 14. Not Using Generators for Large Data

### The Problem
```python
# WRONG - Loading everything into memory
def read_large_file(filename):
    with open(filename, 'r') as f:
        return f.readlines()  # Loads entire file

def process_numbers(n):
    return [i ** 2 for i in range(n)]  # Creates large list
```

### The Solution
```python
# CORRECT - Use generators
def read_large_file(filename):
    with open(filename, 'r') as f:
        for line in f:  # Generator - one line at a time
            yield line.strip()

def process_numbers(n):
    return (i ** 2 for i in range(n))  # Generator expression

# Usage
for line in read_large_file('huge_file.txt'):
    process_line(line)

for square in process_numbers(1000000):
    if square > 1000:
        break
```

## 15. Premature Optimization

### The Problem
```python
# WRONG - Optimizing before measuring
def process_data(data):
    # Complex optimization that may not be needed
    cached_results = {}
    optimized_lookup = create_lookup_table(data)
    
    for item in data:
        if item in cached_results:
            result = cached_results[item]
        else:
            result = complex_calculation(item, optimized_lookup)
            cached_results[item] = result
        
        yield result
```

### The Solution
```python
# CORRECT - Write clear code first
def process_data(data):
    """Process data items."""
    for item in data:
        yield complex_calculation(item)

# Profile and optimize only if needed
import cProfile

def profile_and_optimize():
    # First, measure performance
    profiler = cProfile.Profile()
    profiler.enable()
    
    list(process_data(test_data))
    
    profiler.disable()
    profiler.print_stats()
    
    # Then optimize bottlenecks if necessary
```

## Quick Reference: Common Fixes

| Problem | Wrong | Correct |
|---------|-------|---------|
| Mutable defaults | `def func(lst=[]):` | `def func(lst=None):` |
| Value comparison | `if x is 5:` | `if x == 5:` |
| Identity check | `if x == None:` | `if x is None:` |
| Exception handling | `except:` | `except SpecificError:` |
| File handling | `f = open(); f.close()` | `with open() as f:` |
| String building | `s += item` | `"".join(items)` |
| Boolean check | `if flag == True:` | `if flag:` |
| List modification | `for x in lst: lst.remove(x)` | `for x in lst[:]: lst.remove(x)` |

Remember: Write clear, readable code first. Optimize only when necessary and after profiling!