# Conditionals in Python

**Created by: Syed Ali Hashmi**  
**LinkedIn: [https://www.linkedin.com/in/hashmiali2288](https://www.linkedin.com/in/hashmiali2288)**

## Overview
Conditional statements allow programs to make decisions and execute different code paths based on conditions. Python uses `if`, `elif`, and `else` statements for control flow.

## Basic Syntax

```python
if condition:
    # Execute if condition is True
    pass
elif another_condition:
    # Execute if another_condition is True
    pass
else:
    # Execute if all conditions are False
    pass
```

## Comparison Operators

| Operator | Description | Example |
|----------|-------------|---------|
| `==` | Equal to | `x == 5` |
| `!=` | Not equal to | `x != 5` |
| `>` | Greater than | `x > 5` |
| `<` | Less than | `x < 5` |
| `>=` | Greater than or equal | `x >= 5` |
| `<=` | Less than or equal | `x <= 5` |

## Logical Operators

### AND Operator
```python
if age >= 18 and has_license:
    print("Can drive")
```

### OR Operator
```python
if is_weekend or is_holiday:
    print("No work today")
```

### NOT Operator
```python
if not is_raining:
    print("Good weather for a walk")
```

## Truthiness in Python

### Falsy Values
- `False`
- `0` (zero)
- `0.0` (zero float)
- `""` (empty string)
- `[]` (empty list)
- `{}` (empty dictionary)
- `set()` (empty set)
- `None`

### Truthy Values
Everything else is considered truthy, including:
- `True`
- Non-zero numbers
- Non-empty strings
- Non-empty collections
- Objects

## Conditional Expressions (Ternary Operator)

```python
# Basic syntax
value = expression_if_true if condition else expression_if_false

# Examples
status = "adult" if age >= 18 else "minor"
max_value = a if a > b else b
```

## Match Statements (Python 3.10+)

```python
def handle_status_code(code):
    match code:
        case 200:
            return "OK"
        case 404:
            return "Not Found"
        case 500:
            return "Server Error"
        case _:  # Default case
            return "Unknown"
```

## Best Practices

1. **Use clear, descriptive conditions**
2. **Avoid deep nesting with early returns**
3. **Use parentheses for complex conditions**
4. **Consider using constants for magic numbers**

## Common Patterns

### Input Validation
```python
def validate_age(age):
    if not isinstance(age, int):
        return False, "Age must be an integer"
    if age < 0:
        return False, "Age cannot be negative"
    if age > 150:
        return False, "Age seems unrealistic"
    return True, "Valid age"
```

### Grade Assignment
```python
def get_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"
```