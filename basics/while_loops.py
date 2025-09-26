"""
Python While Loops
==================

This module demonstrates Python while loops - iteration based on conditions.
Learn about basic while loops, infinite loops, loop control, and practical applications.
"""

# =============================================================================
# BASIC WHILE LOOPS
# =============================================================================

def basic_while_examples():
    """Demonstrate basic while loop usage."""
    print("=== Basic While Loops ===")
    
    # Simple counting
    count = 0
    print("Counting to 5:")
    while count < 5:
        print(f"  Count: {count}")
        count += 1
    
    # Countdown
    countdown = 5
    print("\nCountdown:")
    while countdown > 0:
        print(f"  {countdown}")
        countdown -= 1
    print("  Blast off!")
    
    # Processing a list
    numbers = [1, 2, 3, 4, 5]
    index = 0
    total = 0
    
    print("\nSumming numbers:")
    while index < len(numbers):
        total += numbers[index]
        print(f"  Added {numbers[index]}, total: {total}")
        index += 1
    
    print(f"Final total: {total}")

# =============================================================================
# WHILE LOOPS WITH CONDITIONS
# =============================================================================

def conditional_while_loops():
    """Show while loops with various conditions."""
    print("\n=== Conditional While Loops ===")
    
    # User input simulation
    attempts = 0
    max_attempts = 3
    correct_password = "secret123"
    
    print("Password authentication simulation:")
    while attempts < max_attempts:
        # Simulate user input
        passwords = ["wrong1", "wrong2", "secret123"]
        user_input = passwords[attempts] if attempts < len(passwords) else "wrong"
        
        print(f"  Attempt {attempts + 1}: Trying password '{user_input}'")
        
        if user_input == correct_password:
            print("  ✓ Access granted!")
            break
        else:
            attempts += 1
            print(f"  ✗ Wrong password. {max_attempts - attempts} attempts left.")
    
    if attempts == max_attempts:
        print("  Account locked due to too many failed attempts.")
    
    # Finding elements
    numbers = [2, 4, 7, 8, 10, 15]
    target = 7
    index = 0
    found = False
    
    print(f"\nSearching for {target} in {numbers}:")
    while index < len(numbers) and not found:
        if numbers[index] == target:
            found = True
            print(f"  Found {target} at index {index}")
        else:
            print(f"  Checking index {index}: {numbers[index]}")
            index += 1
    
    if not found:
        print(f"  {target} not found in the list")

# =============================================================================
# INFINITE LOOPS AND BREAK
# =============================================================================

def demonstrate_infinite_loops():
    """Show controlled infinite loops with break statements."""
    print("\n=== Infinite Loops with Break ===")
    
    # Menu system simulation
    print("Simple menu system:")
    menu_choice = 0
    choices = [1, 2, 3, 0]  # Simulate user choices
    choice_index = 0
    
    while True:
        print("\n  Menu:")
        print("  1. Option A")
        print("  2. Option B") 
        print("  3. Option C")
        print("  0. Exit")
        
        # Simulate user input
        if choice_index < len(choices):
            choice = choices[choice_index]
            choice_index += 1
        else:
            choice = 0
        
        print(f"  User selected: {choice}")
        
        if choice == 1:
            print("  Executing Option A")
        elif choice == 2:
            print("  Executing Option B")
        elif choice == 3:
            print("  Executing Option C")
        elif choice == 0:
            print("  Goodbye!")
            break
        else:
            print("  Invalid choice, try again")
    
    # Number guessing game simulation
    print("\nNumber guessing game:")
    secret_number = 7
    guesses = [5, 8, 6, 7]  # Simulate user guesses
    guess_index = 0
    attempts = 0
    
    while True:
        attempts += 1
        
        # Simulate user guess
        if guess_index < len(guesses):
            guess = guesses[guess_index]
            guess_index += 1
        else:
            break
        
        print(f"  Attempt {attempts}: Guess is {guess}")
        
        if guess == secret_number:
            print(f"  🎉 Correct! You found it in {attempts} attempts!")
            break
        elif guess < secret_number:
            print("  Too low!")
        else:
            print("  Too high!")
        
        if attempts >= 5:
            print(f"  Game over! The number was {secret_number}")
            break

# =============================================================================
# CONTINUE STATEMENT
# =============================================================================

def demonstrate_continue():
    """Show the continue statement in while loops."""
    print("\n=== Continue Statement ===")
    
    # Skip even numbers
    number = 0
    print("Printing odd numbers from 1 to 10:")
    while number < 10:
        number += 1
        if number % 2 == 0:
            continue  # Skip even numbers
        print(f"  {number}")
    
    # Processing with validation
    data = [5, -2, 8, 0, 12, -1, 15]
    index = 0
    processed_count = 0
    
    print(f"\nProcessing positive numbers from {data}:")
    while index < len(data):
        current = data[index]
        index += 1
        
        if current <= 0:
            print(f"  Skipping non-positive number: {current}")
            continue
        
        # Process positive number
        result = current * 2
        processed_count += 1
        print(f"  Processed {current} -> {result}")
    
    print(f"Processed {processed_count} positive numbers")

# =============================================================================
# ELSE CLAUSE WITH WHILE
# =============================================================================

def demonstrate_while_else():
    """Show the else clause with while loops."""
    print("\n=== While-Else Clause ===")
    
    # Search with else clause
    numbers = [2, 4, 6, 8, 10]
    target = 5
    index = 0
    
    print(f"Searching for {target} in {numbers}:")
    while index < len(numbers):
        if numbers[index] == target:
            print(f"  Found {target} at index {index}")
            break
        print(f"  Checking {numbers[index]}...")
        index += 1
    else:
        # This executes only if the loop completed without break
        print(f"  {target} not found in the list")
    
    # Another example with break
    target = 6
    index = 0
    
    print(f"\nSearching for {target} in {numbers}:")
    while index < len(numbers):
        if numbers[index] == target:
            print(f"  Found {target} at index {index}")
            break
        print(f"  Checking {numbers[index]}...")
        index += 1
    else:
        print(f"  {target} not found in the list")

# =============================================================================
# NESTED WHILE LOOPS
# =============================================================================

def demonstrate_nested_while():
    """Show nested while loops."""
    print("\n=== Nested While Loops ===")
    
    # Multiplication table
    print("Multiplication table (3x3):")
    i = 1
    while i <= 3:
        j = 1
        row = ""
        while j <= 3:
            product = i * j
            row += f"{product:3} "
            j += 1
        print(f"  {row}")
        i += 1
    
    # Pattern printing
    print("\nPrinting a triangle pattern:")
    row = 1
    while row <= 4:
        col = 1
        line = "  "
        while col <= row:
            line += "* "
            col += 1
        print(line)
        row += 1

# =============================================================================
# PRACTICAL APPLICATIONS
# =============================================================================

def practical_applications():
    """Show practical uses of while loops."""
    print("\n=== Practical Applications ===")
    
    # File processing simulation
    print("Processing file lines (simulation):")
    file_lines = ["line 1", "line 2", "", "line 4", "END"]
    line_index = 0
    
    while line_index < len(file_lines):
        line = file_lines[line_index]
        line_index += 1
        
        if line == "END":
            print("  Reached end marker")
            break
        
        if not line.strip():  # Skip empty lines
            print("  Skipping empty line")
            continue
        
        print(f"  Processing: {line}")
    
    # Accumulator pattern
    print("\nCalculating factorial using while loop:")
    n = 5
    factorial = 1
    current = 1
    
    while current <= n:
        factorial *= current
        print(f"  {current}! = {factorial}")
        current += 1
    
    print(f"Final result: {n}! = {factorial}")
    
    # Validation loop
    print("\nInput validation simulation:")
    valid_inputs = ["", "abc", "123", "42"]
    input_index = 0
    
    while input_index < len(valid_inputs):
        user_input = valid_inputs[input_index]
        input_index += 1
        
        print(f"  User entered: '{user_input}'")
        
        if not user_input:
            print("  Error: Input cannot be empty")
            continue
        
        if not user_input.isdigit():
            print("  Error: Input must be a number")
            continue
        
        number = int(user_input)
        if number < 1 or number > 100:
            print("  Error: Number must be between 1 and 100")
            continue
        
        print(f"  ✓ Valid input: {number}")
        break
    else:
        print("  No valid input provided")

# =============================================================================
# PERFORMANCE AND OPTIMIZATION
# =============================================================================

def performance_considerations():
    """Show performance considerations for while loops."""
    print("\n=== Performance Considerations ===")
    
    # Avoid expensive operations in conditions
    print("Optimizing loop conditions:")
    
    # Less efficient (function called every iteration)
    def expensive_function():
        return [1, 2, 3, 4, 5]
    
    print("  Inefficient approach (calling function in condition):")
    i = 0
    # while i < len(expensive_function()):  # Don't do this!
    
    # More efficient (store result)
    print("  Efficient approach (store result once):")
    data = expensive_function()
    i = 0
    while i < len(data):
        print(f"    Processing item {i}: {data[i]}")
        i += 1
        if i >= 3:  # Limit for demo
            break
    
    # Use appropriate data structures
    print("\nChoosing right approach:")
    
    # While loop for unknown iterations
    print("  While loop (unknown iterations):")
    value = 100
    steps = 0
    while value > 1:
        value //= 2
        steps += 1
        if steps > 10:  # Safety break
            break
    print(f"    Took {steps} steps to reduce {100} to {value}")
    
    # For loop when iterations are known
    print("  For loop (known iterations):")
    for i in range(5):
        print(f"    Step {i}")

# =============================================================================
# COMMON PATTERNS AND IDIOMS
# =============================================================================

def common_patterns():
    """Show common while loop patterns."""
    print("\n=== Common Patterns ===")
    
    # Sentinel-controlled loop
    print("Sentinel-controlled loop:")
    values = [10, 20, 30, -1, 40]  # -1 is sentinel
    index = 0
    total = 0
    
    while index < len(values) and values[index] != -1:
        total += values[index]
        print(f"  Added {values[index]}, total: {total}")
        index += 1
    
    print(f"Sum before sentinel: {total}")
    
    # Flag-controlled loop
    print("\nFlag-controlled loop:")
    numbers = [2, 4, 6, 7, 8, 10]
    found_odd = False
    index = 0
    
    while index < len(numbers) and not found_odd:
        if numbers[index] % 2 == 1:
            found_odd = True
            print(f"  Found first odd number: {numbers[index]}")
        else:
            print(f"  {numbers[index]} is even")
        index += 1
    
    # Counter-controlled loop (alternative to for)
    print("\nCounter-controlled loop:")
    counter = 0
    limit = 5
    
    while counter < limit:
        print(f"  Iteration {counter}")
        counter += 1

# =============================================================================
# ERROR HANDLING IN WHILE LOOPS
# =============================================================================

def error_handling_examples():
    """Show error handling in while loops."""
    print("\n=== Error Handling ===")
    
    # Safe division with retry
    print("Safe division with retry:")
    dividends = [10, 15, 20]
    divisors = [2, 0, 4, 3]  # Contains zero
    
    dividend_index = 0
    while dividend_index < len(dividends):
        dividend = dividends[dividend_index]
        divisor_index = dividend_index
        
        while divisor_index < len(divisors):
            divisor = divisors[divisor_index]
            
            try:
                result = dividend / divisor
                print(f"  {dividend} / {divisor} = {result}")
                break
            except ZeroDivisionError:
                print(f"  Cannot divide {dividend} by {divisor} (zero)")
                divisor_index += 1
                continue
        else:
            print(f"  No valid divisor found for {dividend}")
        
        dividend_index += 1
    
    # Robust input processing
    print("\nRobust input processing:")
    inputs = ["abc", "12.5", "not_a_number", "42"]
    input_index = 0
    valid_numbers = []
    
    while input_index < len(inputs):
        user_input = inputs[input_index]
        input_index += 1
        
        try:
            number = float(user_input)
            valid_numbers.append(number)
            print(f"  ✓ Converted '{user_input}' to {number}")
        except ValueError:
            print(f"  ✗ Cannot convert '{user_input}' to number")
            continue
    
    print(f"Valid numbers collected: {valid_numbers}")

# =============================================================================
# MAIN EXECUTION
# =============================================================================

if __name__ == "__main__":
    """Run all demonstrations when script is executed directly."""
    print("Python While Loops Tutorial")
    print("=" * 50)
    
    basic_while_examples()
    conditional_while_loops()
    demonstrate_infinite_loops()
    demonstrate_continue()
    demonstrate_while_else()
    demonstrate_nested_while()
    practical_applications()
    performance_considerations()
    common_patterns()
    error_handling_examples()
    
    print("\n" + "=" * 50)
    print("While loops tutorial completed!")