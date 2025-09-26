# While Loops in Python

## Overview
While loops execute a block of code repeatedly as long as a condition remains true. They're useful when you don't know in advance how many iterations you need.

## Basic Syntax

```python
while condition:
    # Code to execute
    # Don't forget to update the condition!
    pass
```

## Simple Examples

### Counting
```python
count = 0
while count < 5:
    print(f"Count: {count}")
    count += 1  # Important: update the condition variable
```

### User Input Loop
```python
user_input = ""
while user_input != "quit":
    user_input = input("Enter 'quit' to exit: ")
    print(f"You entered: {user_input}")
```

## Loop Control Statements

### Break Statement
Exits the loop immediately:
```python
while True:
    user_input = input("Enter a number (or 'quit'): ")
    if user_input == 'quit':
        break
    print(f"You entered: {user_input}")
```

### Continue Statement
Skips the rest of the current iteration:
```python
count = 0
while count < 10:
    count += 1
    if count % 2 == 0:
        continue  # Skip even numbers
    print(f"Odd number: {count}")
```

## Else Clause with While

The `else` clause executes when the loop completes normally (not via `break`):

```python
count = 0
while count < 3:
    print(f"Count: {count}")
    count += 1
else:
    print("Loop completed normally")
```

## Common Patterns

### Validation Loop
```python
while True:
    try:
        age = int(input("Enter your age: "))
        if age >= 0:
            break
        else:
            print("Age cannot be negative")
    except ValueError:
        print("Please enter a valid number")
```

### Menu System
```python
while True:
    print("1. Option A")
    print("2. Option B")
    print("3. Exit")
    
    choice = input("Choose an option: ")
    
    if choice == "1":
        print("You chose Option A")
    elif choice == "2":
        print("You chose Option B")
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice")
```

### Processing Until Condition
```python
total = 0
while total < 100:
    value = int(input("Enter a number: "))
    total += value
    print(f"Current total: {total}")

print(f"Final total: {total}")
```

## Infinite Loops

### Intentional Infinite Loops
```python
# Server-like behavior
while True:
    # Process requests
    request = get_next_request()
    if request:
        process_request(request)
    else:
        time.sleep(0.1)  # Small delay
```

### Avoiding Infinite Loops
Always ensure the condition can become false:
```python
# Good: condition will eventually become false
count = 0
while count < 10:
    print(count)
    count += 1  # This ensures the loop will end

# Bad: infinite loop (count never changes)
count = 0
while count < 10:
    print(count)
    # Missing: count += 1
```

## Nested While Loops

```python
i = 1
while i <= 3:
    j = 1
    while j <= 3:
        print(f"i={i}, j={j}")
        j += 1
    i += 1
```

## Performance Considerations

### Minimize Work in Condition
```python
# Less efficient
while len(expensive_function()) > 0:
    process_item()

# More efficient
items = expensive_function()
while len(items) > 0:
    process_item()
    items = expensive_function()  # Update when needed
```

### Use Appropriate Data Structures
```python
# For known iterations, consider for loops
for i in range(10):
    print(i)

# Better than:
i = 0
while i < 10:
    print(i)
    i += 1
```

## Common Mistakes

1. **Forgetting to update the condition variable**
2. **Off-by-one errors**
3. **Using while when for would be better**
4. **Not handling edge cases (empty inputs, etc.)**

## When to Use While vs For

### Use While When:
- You don't know how many iterations you need
- Waiting for a condition to become true
- Processing user input until they quit
- Implementing game loops

### Use For When:
- You know the number of iterations
- Iterating over collections
- Working with ranges of numbers

## Best Practices

1. **Always ensure the loop can terminate**
2. **Use meaningful variable names**
3. **Keep loop bodies simple and focused**
4. **Consider using `break` and `continue` for clarity**
5. **Add comments for complex loop logic**