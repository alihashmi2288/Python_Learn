"""
Python Variables and Data Types
===============================

This module demonstrates Python's core data types and variable handling.
Learn about numbers, strings, booleans, lists, tuples, dictionaries, and sets.
"""

# =============================================================================
# VARIABLES AND ASSIGNMENT
# =============================================================================

def demonstrate_variables():
    """Show how variables work in Python."""
    print("=== Variables and Assignment ===")
    
    # Variable assignment (no declaration needed)
    name = "Python"
    age = 30
    is_awesome = True
    
    print(f"Language: {name}")
    print(f"Age: {age}")
    print(f"Is awesome: {is_awesome}")
    
    # Multiple assignment
    x, y, z = 1, 2, 3
    print(f"Multiple assignment: x={x}, y={y}, z={z}")

# =============================================================================
# NUMERIC TYPES
# =============================================================================

def demonstrate_numbers():
    """Explore Python's numeric data types."""
    print("\n=== Numeric Types ===")
    
    # Integers
    integer_num = 42
    print(f"Integer: {integer_num} (type: {type(integer_num)})")
    
    # Floats
    float_num = 3.14159
    print(f"Float: {float_num} (type: {type(float_num)})")
    
    # Complex numbers
    complex_num = 3 + 4j
    print(f"Complex: {complex_num} (type: {type(complex_num)})")
    
    # Arithmetic operations
    print(f"Addition: 10 + 5 = {10 + 5}")
    print(f"Division: 10 / 3 = {10 / 3}")
    print(f"Floor division: 10 // 3 = {10 // 3}")
    print(f"Modulo: 10 % 3 = {10 % 3}")
    print(f"Exponentiation: 2 ** 3 = {2 ** 3}")

# =============================================================================
# STRINGS
# =============================================================================

def demonstrate_strings():
    """Learn about string manipulation and methods."""
    print("\n=== Strings ===")
    
    # String creation
    single_quote = 'Hello'
    double_quote = "World"
    triple_quote = """Multi-line
    string example"""
    
    print(f"Single quotes: {single_quote}")
    print(f"Double quotes: {double_quote}")
    print(f"Triple quotes: {repr(triple_quote)}")
    
    # String concatenation and formatting
    full_greeting = single_quote + " " + double_quote
    print(f"Concatenation: {full_greeting}")
    
    # F-strings (recommended)
    name = "Alice"
    age = 25
    print(f"F-string: Hello {name}, you are {age} years old")
    
    # String methods
    text = "  Python Programming  "
    print(f"Original: '{text}'")
    print(f"Strip: '{text.strip()}'")
    print(f"Upper: '{text.upper()}'")
    print(f"Lower: '{text.lower()}'")
    print(f"Replace: '{text.replace('Python', 'Java')}'")
    print(f"Split: {text.strip().split()}")

# =============================================================================
# BOOLEAN TYPE
# =============================================================================

def demonstrate_booleans():
    """Understand boolean values and operations."""
    print("\n=== Booleans ===")
    
    # Boolean values
    is_true = True
    is_false = False
    
    print(f"True: {is_true} (type: {type(is_true)})")
    print(f"False: {is_false} (type: {type(is_false)})")
    
    # Boolean operations
    print(f"True and False: {True and False}")
    print(f"True or False: {True or False}")
    print(f"not True: {not True}")
    
    # Truthiness in Python
    print(f"bool(1): {bool(1)}")
    print(f"bool(0): {bool(0)}")
    print(f"bool(''): {bool('')}")
    print(f"bool('hello'): {bool('hello')}")
    print(f"bool([]): {bool([])}")
    print(f"bool([1, 2]): {bool([1, 2])}")

# =============================================================================
# LISTS
# =============================================================================

def demonstrate_lists():
    """Explore Python lists - mutable, ordered collections."""
    print("\n=== Lists ===")
    
    # List creation
    fruits = ["apple", "banana", "cherry"]
    numbers = [1, 2, 3, 4, 5]
    mixed = [1, "hello", 3.14, True]
    
    print(f"Fruits: {fruits}")
    print(f"Numbers: {numbers}")
    print(f"Mixed types: {mixed}")
    
    # List operations
    print(f"First fruit: {fruits[0]}")
    print(f"Last fruit: {fruits[-1]}")
    print(f"Slice [1:3]: {fruits[1:3]}")
    
    # Modifying lists
    fruits.append("orange")
    print(f"After append: {fruits}")
    
    fruits.insert(1, "grape")
    print(f"After insert: {fruits}")
    
    fruits.remove("banana")
    print(f"After remove: {fruits}")
    
    # List methods
    numbers_copy = numbers.copy()
    numbers_copy.reverse()
    print(f"Reversed: {numbers_copy}")
    print(f"Length: {len(fruits)}")

# =============================================================================
# TUPLES
# =============================================================================

def demonstrate_tuples():
    """Learn about tuples - immutable, ordered collections."""
    print("\n=== Tuples ===")
    
    # Tuple creation
    coordinates = (10, 20)
    colors = ("red", "green", "blue")
    single_item = ("item",)  # Note the comma for single-item tuple
    
    print(f"Coordinates: {coordinates}")
    print(f"Colors: {colors}")
    print(f"Single item: {single_item}")
    
    # Tuple operations
    print(f"First coordinate: {coordinates[0]}")
    print(f"Color count: {len(colors)}")
    
    # Tuple unpacking
    x, y = coordinates
    print(f"Unpacked: x={x}, y={y}")
    
    # Tuples are immutable
    try:
        coordinates[0] = 15  # This will raise an error
    except TypeError as e:
        print(f"Error (expected): {e}")

# =============================================================================
# DICTIONARIES
# =============================================================================

def demonstrate_dictionaries():
    """Explore dictionaries - mutable, unordered key-value pairs."""
    print("\n=== Dictionaries ===")
    
    # Dictionary creation
    person = {
        "name": "John",
        "age": 30,
        "city": "New York"
    }
    
    # Alternative creation
    scores = dict(math=95, science=87, english=92)
    
    print(f"Person: {person}")
    print(f"Scores: {scores}")
    
    # Accessing values
    print(f"Name: {person['name']}")
    print(f"Age: {person.get('age', 'Unknown')}")
    
    # Modifying dictionaries
    person["email"] = "john@example.com"
    person["age"] = 31
    print(f"Updated person: {person}")
    
    # Dictionary methods
    print(f"Keys: {list(person.keys())}")
    print(f"Values: {list(person.values())}")
    print(f"Items: {list(person.items())}")

# =============================================================================
# SETS
# =============================================================================

def demonstrate_sets():
    """Learn about sets - mutable, unordered collections of unique items."""
    print("\n=== Sets ===")
    
    # Set creation
    fruits = {"apple", "banana", "cherry"}
    numbers = set([1, 2, 3, 4, 5, 5, 5])  # Duplicates removed
    
    print(f"Fruits set: {fruits}")
    print(f"Numbers set: {numbers}")
    
    # Set operations
    fruits.add("orange")
    print(f"After add: {fruits}")
    
    fruits.discard("banana")
    print(f"After discard: {fruits}")
    
    # Set mathematics
    set1 = {1, 2, 3, 4}
    set2 = {3, 4, 5, 6}
    
    print(f"Set1: {set1}")
    print(f"Set2: {set2}")
    print(f"Union: {set1 | set2}")
    print(f"Intersection: {set1 & set2}")
    print(f"Difference: {set1 - set2}")

# =============================================================================
# TYPE CONVERSION
# =============================================================================

def demonstrate_type_conversion():
    """Show how to convert between different data types."""
    print("\n=== Type Conversion ===")
    
    # String to number
    str_num = "123"
    int_num = int(str_num)
    float_num = float(str_num)
    
    print(f"String '{str_num}' to int: {int_num}")
    print(f"String '{str_num}' to float: {float_num}")
    
    # Number to string
    num = 456
    str_from_num = str(num)
    print(f"Number {num} to string: '{str_from_num}'")
    
    # List/tuple conversion
    list_data = [1, 2, 3]
    tuple_data = tuple(list_data)
    list_from_tuple = list(tuple_data)
    
    print(f"List to tuple: {list_data} → {tuple_data}")
    print(f"Tuple to list: {tuple_data} → {list_from_tuple}")
    
    # String to list
    text = "hello"
    char_list = list(text)
    print(f"String to list: '{text}' → {char_list}")

# =============================================================================
# MAIN EXECUTION
# =============================================================================

if __name__ == "__main__":
    """Run all demonstrations when script is executed directly."""
    print("Python Variables and Data Types Tutorial")
    print("=" * 50)
    
    demonstrate_variables()
    demonstrate_numbers()
    demonstrate_strings()
    demonstrate_booleans()
    demonstrate_lists()
    demonstrate_tuples()
    demonstrate_dictionaries()
    demonstrate_sets()
    demonstrate_type_conversion()
    
    print("\n" + "=" * 50)
    print("Tutorial completed! Practice with different values.")