# Variables and Data Types in Python

## Overview
Python is a dynamically typed language, meaning you don't need to declare variable types explicitly. This guide covers all the fundamental data types and how to work with them.

## Variables

### Variable Assignment
```python
# Simple assignment
name = "Python"
age = 30
is_programming = True

# Multiple assignment
x, y, z = 1, 2, 3
a = b = c = 0  # Same value to multiple variables
```

### Variable Naming Rules
- Must start with a letter or underscore
- Can contain letters, numbers, and underscores
- Case-sensitive (`name` and `Name` are different)
- Cannot use Python keywords (`if`, `for`, `class`, etc.)

## Data Types

### 1. Numeric Types

#### Integer (int)
- Whole numbers without decimal points
- No size limit (limited by memory)
```python
age = 25
population = 7800000000
```

#### Float (float)
- Numbers with decimal points
- 64-bit precision
```python
pi = 3.14159
temperature = -5.5
```

#### Complex (complex)
- Numbers with real and imaginary parts
```python
z = 3 + 4j
```

### 2. Text Type

#### String (str)
- Sequence of characters
- Immutable (cannot be changed after creation)
```python
name = "Alice"
message = 'Hello World'
multiline = """This is a
multi-line string"""
```

**Common String Methods:**
- `strip()` - Remove whitespace
- `upper()`, `lower()` - Change case
- `replace(old, new)` - Replace text
- `split()` - Split into list
- `join()` - Join list into string

### 3. Boolean Type

#### Boolean (bool)
- Only two values: `True` or `False`
- Used in conditional statements
```python
is_valid = True
is_empty = False
```

**Truthiness:**
- `False`: `False`, `0`, `""`, `[]`, `{}`, `None`
- `True`: Everything else

### 4. Sequence Types

#### List (list)
- Ordered, mutable collection
- Can contain different data types
```python
fruits = ["apple", "banana", "cherry"]
mixed = [1, "hello", 3.14, True]
```

**Key Features:**
- Indexed (starting from 0)
- Sliceable
- Mutable (can be modified)

#### Tuple (tuple)
- Ordered, immutable collection
- Faster than lists for fixed data
```python
coordinates = (10, 20)
colors = ("red", "green", "blue")
```

**Key Features:**
- Indexed (starting from 0)
- Sliceable
- Immutable (cannot be modified)

### 5. Mapping Type

#### Dictionary (dict)
- Unordered collection of key-value pairs
- Keys must be unique and immutable
```python
person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
```

**Key Features:**
- Fast lookup by key
- Mutable
- Keys must be hashable

### 6. Set Types

#### Set (set)
- Unordered collection of unique items
- Mutable
```python
fruits = {"apple", "banana", "cherry"}
numbers = {1, 2, 3, 4, 5}
```

**Key Features:**
- No duplicates
- Fast membership testing
- Mathematical set operations

## Type Checking and Conversion

### Checking Types
```python
type(variable)      # Returns the type
isinstance(var, type)  # Checks if variable is of specific type
```

### Type Conversion
```python
int("123")      # String to integer
float("3.14")   # String to float
str(123)        # Number to string
list("hello")   # String to list
tuple([1,2,3])  # List to tuple
```

## Best Practices

1. **Use descriptive variable names**
   ```python
   # Good
   user_age = 25
   total_price = 99.99
   
   # Avoid
   x = 25
   p = 99.99
   ```

2. **Follow naming conventions**
   - Variables and functions: `snake_case`
   - Constants: `UPPER_CASE`
   - Classes: `PascalCase`

3. **Choose appropriate data types**
   - Use tuples for fixed data
   - Use lists for changing data
   - Use sets for unique items
   - Use dictionaries for key-value relationships

4. **Handle type conversion safely**
   ```python
   try:
       number = int(user_input)
   except ValueError:
       print("Invalid number")
   ```

## Common Pitfalls

1. **Mutable default arguments**
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

2. **Modifying lists while iterating**
   ```python
   # Wrong
   for item in my_list:
       if condition:
           my_list.remove(item)
   
   # Correct
   my_list = [item for item in my_list if not condition]
   ```

## Practice Exercises

1. Create variables of each data type
2. Practice string formatting with f-strings
3. Convert between different data types
4. Create nested data structures (list of dictionaries)
5. Use set operations to find common elements between lists