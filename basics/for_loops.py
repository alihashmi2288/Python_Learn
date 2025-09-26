"""
Python For Loops
================

This module demonstrates Python for loops - iteration over sequences and iterables.
Learn about basic loops, range(), enumerate(), zip(), and advanced iteration techniques.
"""

# =============================================================================
# BASIC FOR LOOPS
# =============================================================================

def basic_list_iteration():
    """Demonstrate basic iteration over lists."""
    print("=== Basic List Iteration ===")
    
    fruits = ["apple", "banana", "cherry", "date"]
    
    # Simple iteration
    print("Fruits:")
    for fruit in fruits:
        print(f"  - {fruit}")
    
    # Iteration with processing
    print("\nFruit lengths:")
    for fruit in fruits:
        print(f"  {fruit}: {len(fruit)} characters")

def basic_string_iteration():
    """Demonstrate iteration over strings."""
    print("\n=== String Iteration ===")
    
    word = "Python"
    
    # Iterate over characters
    print("Characters in 'Python':")
    for char in word:
        print(f"  '{char}'")
    
    # Count vowels
    vowels = "aeiou"
    vowel_count = 0
    for char in word.lower():
        if char in vowels:
            vowel_count += 1
    print(f"Vowels in '{word}': {vowel_count}")

# =============================================================================
# RANGE FUNCTION
# =============================================================================

def demonstrate_range():
    """Show different ways to use range() function."""
    print("\n=== Range Function ===")
    
    # range(stop)
    print("range(5):")
    for i in range(5):
        print(f"  {i}")
    
    # range(start, stop)
    print("\nrange(2, 8):")
    for i in range(2, 8):
        print(f"  {i}")
    
    # range(start, stop, step)
    print("\nrange(0, 10, 2):")
    for i in range(0, 10, 2):
        print(f"  {i}")
    
    # Negative step
    print("\nrange(10, 0, -2):")
    for i in range(10, 0, -2):
        print(f"  {i}")

def practical_range_examples():
    """Show practical uses of range()."""
    print("\n=== Practical Range Examples ===")
    
    # Creating multiplication table
    number = 5
    print(f"Multiplication table for {number}:")
    for i in range(1, 11):
        print(f"  {number} × {i} = {number * i}")
    
    # Accessing list indices
    colors = ["red", "green", "blue", "yellow"]
    print("\nColors with indices:")
    for i in range(len(colors)):
        print(f"  Index {i}: {colors[i]}")

# =============================================================================
# ENUMERATE FUNCTION
# =============================================================================

def demonstrate_enumerate():
    """Show how to use enumerate() for index-value pairs."""
    print("\n=== Enumerate Function ===")
    
    languages = ["Python", "Java", "JavaScript", "C++"]
    
    # Basic enumerate
    print("Programming languages:")
    for index, language in enumerate(languages):
        print(f"  {index}: {language}")
    
    # Enumerate with custom start
    print("\nLanguages (starting from 1):")
    for index, language in enumerate(languages, start=1):
        print(f"  {index}. {language}")
    
    # Finding index of specific item
    search_lang = "JavaScript"
    for index, language in enumerate(languages):
        if language == search_lang:
            print(f"\nFound '{search_lang}' at index {index}")
            break

# =============================================================================
# ZIP FUNCTION
# =============================================================================

def demonstrate_zip():
    """Show how to use zip() to iterate over multiple sequences."""
    print("\n=== Zip Function ===")
    
    names = ["Alice", "Bob", "Charlie"]
    ages = [25, 30, 35]
    cities = ["New York", "London", "Tokyo"]
    
    # Basic zip
    print("People information:")
    for name, age, city in zip(names, ages, cities):
        print(f"  {name} is {age} years old and lives in {city}")
    
    # Zip with different length lists
    scores = [95, 87]  # Shorter list
    print("\nNames and scores (note: zip stops at shortest):")
    for name, score in zip(names, scores):
        print(f"  {name}: {score}")
    
    # Creating dictionary from two lists
    student_grades = dict(zip(names, scores))
    print(f"\nStudent grades dictionary: {student_grades}")

# =============================================================================
# NESTED LOOPS
# =============================================================================

def demonstrate_nested_loops():
    """Show nested loop patterns."""
    print("\n=== Nested Loops ===")
    
    # Multiplication table
    print("Multiplication table (1-5):")
    for i in range(1, 6):
        for j in range(1, 6):
            print(f"{i*j:3}", end=" ")
        print()  # New line after each row
    
    # Matrix iteration
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    
    print("\nMatrix elements:")
    for row_index, row in enumerate(matrix):
        for col_index, value in enumerate(row):
            print(f"  matrix[{row_index}][{col_index}] = {value}")

# =============================================================================
# LOOP CONTROL STATEMENTS
# =============================================================================

def demonstrate_break_continue():
    """Show break and continue statements."""
    print("\n=== Break and Continue ===")
    
    # Break example
    print("Finding first even number:")
    numbers = [1, 3, 5, 8, 9, 12, 15]
    for num in numbers:
        if num % 2 == 0:
            print(f"  First even number: {num}")
            break
        print(f"  Checking {num}... odd")
    
    # Continue example
    print("\nPrinting only positive numbers:")
    mixed_numbers = [-2, 5, -1, 8, -3, 12]
    for num in mixed_numbers:
        if num < 0:
            continue  # Skip negative numbers
        print(f"  Positive: {num}")
    
    # Break in nested loops
    print("\nBreaking out of nested loops:")
    for i in range(3):
        print(f"  Outer loop: {i}")
        for j in range(5):
            if j == 2:
                print(f"    Breaking inner loop at j={j}")
                break
            print(f"    Inner loop: {j}")

# =============================================================================
# ELSE CLAUSE WITH LOOPS
# =============================================================================

def demonstrate_loop_else():
    """Show the else clause with loops."""
    print("\n=== Loop Else Clause ===")
    
    # Else with for loop (executes if loop completes normally)
    print("Searching for number 7:")
    numbers = [1, 3, 5, 9, 11]
    for num in numbers:
        if num == 7:
            print(f"  Found 7!")
            break
        print(f"  Checking {num}...")
    else:
        print("  7 not found in the list")
    
    # Else with break
    print("\nSearching for number 5:")
    for num in numbers:
        if num == 5:
            print(f"  Found 5!")
            break
        print(f"  Checking {num}...")
    else:
        print("  5 not found in the list")

# =============================================================================
# LIST COMPREHENSIONS
# =============================================================================

def demonstrate_list_comprehensions():
    """Show list comprehensions as alternative to loops."""
    print("\n=== List Comprehensions ===")
    
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    # Traditional loop
    squares_loop = []
    for num in numbers:
        squares_loop.append(num ** 2)
    print(f"Squares (loop): {squares_loop}")
    
    # List comprehension
    squares_comp = [num ** 2 for num in numbers]
    print(f"Squares (comprehension): {squares_comp}")
    
    # With condition
    even_squares = [num ** 2 for num in numbers if num % 2 == 0]
    print(f"Even squares: {even_squares}")
    
    # Nested comprehension
    matrix = [[i * j for j in range(1, 4)] for i in range(1, 4)]
    print(f"Matrix: {matrix}")

# =============================================================================
# ITERATING OVER DICTIONARIES
# =============================================================================

def demonstrate_dict_iteration():
    """Show different ways to iterate over dictionaries."""
    print("\n=== Dictionary Iteration ===")
    
    student_grades = {
        "Alice": 95,
        "Bob": 87,
        "Charlie": 92,
        "Diana": 98
    }
    
    # Iterate over keys (default)
    print("Student names:")
    for name in student_grades:
        print(f"  {name}")
    
    # Iterate over values
    print("\nGrades:")
    for grade in student_grades.values():
        print(f"  {grade}")
    
    # Iterate over key-value pairs
    print("\nStudent grades:")
    for name, grade in student_grades.items():
        print(f"  {name}: {grade}")
    
    # With enumerate
    print("\nRanked students:")
    sorted_students = sorted(student_grades.items(), key=lambda x: x[1], reverse=True)
    for rank, (name, grade) in enumerate(sorted_students, start=1):
        print(f"  {rank}. {name}: {grade}")

# =============================================================================
# ADVANCED ITERATION TECHNIQUES
# =============================================================================

def demonstrate_advanced_iteration():
    """Show advanced iteration patterns."""
    print("\n=== Advanced Iteration ===")
    
    # Iterating with itertools
    import itertools
    
    # Infinite counter
    print("First 5 numbers from itertools.count(10, 2):")
    counter = itertools.count(10, 2)
    for i, num in enumerate(counter):
        if i >= 5:
            break
        print(f"  {num}")
    
    # Cycle through items
    colors = ["red", "green", "blue"]
    print("\nCycling through colors (first 8):")
    color_cycle = itertools.cycle(colors)
    for i, color in enumerate(color_cycle):
        if i >= 8:
            break
        print(f"  {i}: {color}")
    
    # Chain multiple iterables
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    list3 = [7, 8, 9]
    
    print("\nChaining lists:")
    for num in itertools.chain(list1, list2, list3):
        print(f"  {num}")

# =============================================================================
# PERFORMANCE CONSIDERATIONS
# =============================================================================

def demonstrate_performance():
    """Show performance considerations for loops."""
    print("\n=== Performance Tips ===")
    
    # Avoid repeated lookups
    data = {"items": [1, 2, 3, 4, 5]}
    
    # Inefficient (repeated dictionary lookup)
    print("Inefficient approach (repeated lookups):")
    for i in range(len(data["items"])):
        print(f"  Item {i}: {data['items'][i]}")
    
    # Efficient (store reference)
    print("\nEfficient approach (store reference):")
    items = data["items"]
    for i, item in enumerate(items):
        print(f"  Item {i}: {item}")
    
    # Use built-in functions when possible
    numbers = [1, 2, 3, 4, 5]
    
    # Manual sum
    total = 0
    for num in numbers:
        total += num
    print(f"\nManual sum: {total}")
    
    # Built-in sum (faster)
    total_builtin = sum(numbers)
    print(f"Built-in sum: {total_builtin}")

# =============================================================================
# MAIN EXECUTION
# =============================================================================

if __name__ == "__main__":
    """Run all demonstrations when script is executed directly."""
    print("Python For Loops Tutorial")
    print("=" * 50)
    
    basic_list_iteration()
    basic_string_iteration()
    demonstrate_range()
    practical_range_examples()
    demonstrate_enumerate()
    demonstrate_zip()
    demonstrate_nested_loops()
    demonstrate_break_continue()
    demonstrate_loop_else()
    demonstrate_list_comprehensions()
    demonstrate_dict_iteration()
    demonstrate_advanced_iteration()
    demonstrate_performance()
    
    print("\n" + "=" * 50)
    print("For loops tutorial completed!")