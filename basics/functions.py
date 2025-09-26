"""
Python Functions
================

Created by: Syed Ali Hashmi
LinkedIn: https://www.linkedin.com/in/hashmiali2288

This module demonstrates Python functions - reusable blocks of code that perform specific tasks.
Learn about function definition, parameters, return values, scope, and advanced concepts.
"""

# =============================================================================
# BASIC FUNCTION DEFINITION
# =============================================================================

def greet():
    """A simple function with no parameters."""
    print("Hello, World!")

def greet_person(name):
    """Function with a single parameter."""
    print(f"Hello, {name}!")

def add_numbers(a, b):
    """Function with multiple parameters that returns a value."""
    return a + b

# =============================================================================
# DEFAULT PARAMETERS
# =============================================================================

def greet_with_title(name, title="Mr./Ms."):
    """Function with default parameter value."""
    return f"Hello, {title} {name}!"

def create_profile(name, age=18, city="Unknown"):
    """Function with multiple default parameters."""
    return {
        "name": name,
        "age": age,
        "city": city
    }

# =============================================================================
# VARIABLE-LENGTH ARGUMENTS
# =============================================================================

def sum_all(*args):
    """Function that accepts any number of positional arguments."""
    total = 0
    for num in args:
        total += num
    return total

def print_info(**kwargs):
    """Function that accepts any number of keyword arguments."""
    for key, value in kwargs.items():
        print(f"{key}: {value}")

def flexible_function(*args, **kwargs):
    """Function that accepts both *args and **kwargs."""
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

# =============================================================================
# RETURN VALUES
# =============================================================================

def calculate_rectangle(length, width):
    """Function returning multiple values."""
    area = length * width
    perimeter = 2 * (length + width)
    return area, perimeter  # Returns a tuple

def divide_numbers(a, b):
    """Function with conditional return."""
    if b == 0:
        return None, "Cannot divide by zero"
    return a / b, "Success"

def get_user_info():
    """Function returning different data types."""
    return {
        "name": "Alice",
        "scores": [95, 87, 92],
        "is_active": True
    }

# =============================================================================
# SCOPE AND GLOBAL VARIABLES
# =============================================================================

# Global variable
global_counter = 0

def increment_global():
    """Function modifying global variable."""
    global global_counter
    global_counter += 1
    return global_counter

def local_scope_demo():
    """Demonstrate local variable scope."""
    local_var = "I'm local"
    print(f"Inside function: {local_var}")
    return local_var

# =============================================================================
# NESTED FUNCTIONS AND CLOSURES
# =============================================================================

def outer_function(x):
    """Outer function demonstrating closures."""
    
    def inner_function(y):
        """Inner function that has access to outer function's variables."""
        return x + y
    
    return inner_function

def create_multiplier(factor):
    """Factory function that creates multiplier functions."""
    
    def multiplier(number):
        """Inner function that multiplies by the factor."""
        return number * factor
    
    return multiplier

# =============================================================================
# LAMBDA FUNCTIONS
# =============================================================================

def demonstrate_lambda():
    """Show various uses of lambda functions."""
    
    # Simple lambda
    square = lambda x: x ** 2
    print(f"Square of 5: {square(5)}")
    
    # Lambda with multiple parameters
    add = lambda x, y: x + y
    print(f"Add 3 and 7: {add(3, 7)}")
    
    # Lambda in higher-order functions
    numbers = [1, 2, 3, 4, 5]
    
    # Using lambda with map()
    squared = list(map(lambda x: x ** 2, numbers))
    print(f"Squared numbers: {squared}")
    
    # Using lambda with filter()
    evens = list(filter(lambda x: x % 2 == 0, numbers))
    print(f"Even numbers: {evens}")
    
    # Using lambda with sorted()
    students = [("Alice", 85), ("Bob", 90), ("Charlie", 78)]
    sorted_by_grade = sorted(students, key=lambda student: student[1])
    print(f"Students sorted by grade: {sorted_by_grade}")

# =============================================================================
# DECORATORS (BASIC)
# =============================================================================

def timing_decorator(func):
    """A simple decorator that prints when a function is called."""
    
    def wrapper(*args, **kwargs):
        print(f"Calling function: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Function {func.__name__} completed")
        return result
    
    return wrapper

@timing_decorator
def slow_function():
    """Function decorated with timing_decorator."""
    import time
    time.sleep(1)
    return "Task completed"

# =============================================================================
# RECURSIVE FUNCTIONS
# =============================================================================

def factorial(n):
    """Calculate factorial using recursion."""
    if n <= 1:
        return 1
    return n * factorial(n - 1)

def fibonacci(n):
    """Calculate Fibonacci number using recursion."""
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

def fibonacci_optimized(n, memo={}):
    """Optimized Fibonacci using memoization."""
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci_optimized(n - 1, memo) + fibonacci_optimized(n - 2, memo)
    return memo[n]

# =============================================================================
# HIGHER-ORDER FUNCTIONS
# =============================================================================

def apply_operation(numbers, operation):
    """Apply an operation to all numbers in a list."""
    return [operation(num) for num in numbers]

def create_validator(min_value, max_value):
    """Create a validation function with specific range."""
    
    def validate(value):
        """Validate if value is within the specified range."""
        return min_value <= value <= max_value
    
    return validate

# =============================================================================
# FUNCTION ANNOTATIONS
# =============================================================================

def calculate_bmi(weight: float, height: float) -> float:
    """
    Calculate Body Mass Index.
    
    Args:
        weight (float): Weight in kilograms
        height (float): Height in meters
    
    Returns:
        float: BMI value
    """
    return weight / (height ** 2)

def process_data(data: list[int], multiplier: int = 2) -> list[int]:
    """
    Process a list of integers by multiplying each by a factor.
    
    Args:
        data: List of integers to process
        multiplier: Factor to multiply each number by
    
    Returns:
        List of processed integers
    """
    return [num * multiplier for num in data]

# =============================================================================
# DEMONSTRATION FUNCTIONS
# =============================================================================

def demonstrate_basic_functions():
    """Demonstrate basic function concepts."""
    print("=== Basic Functions ===")
    
    # Simple function call
    greet()
    greet_person("Alice")
    
    # Function with return value
    result = add_numbers(5, 3)
    print(f"5 + 3 = {result}")
    
    # Default parameters
    print(greet_with_title("Smith"))
    print(greet_with_title("Johnson", "Dr."))

def demonstrate_variable_arguments():
    """Demonstrate *args and **kwargs."""
    print("\n=== Variable Arguments ===")
    
    # *args example
    print(f"Sum of 1,2,3,4,5: {sum_all(1, 2, 3, 4, 5)}")
    
    # **kwargs example
    print("User info:")
    print_info(name="Alice", age=30, city="New York", job="Engineer")
    
    # Combined *args and **kwargs
    flexible_function(1, 2, 3, name="Bob", age=25)

def demonstrate_return_values():
    """Demonstrate different return value patterns."""
    print("\n=== Return Values ===")
    
    # Multiple return values
    area, perimeter = calculate_rectangle(5, 3)
    print(f"Rectangle (5x3): Area={area}, Perimeter={perimeter}")
    
    # Conditional return
    result, message = divide_numbers(10, 2)
    print(f"10 / 2 = {result} ({message})")
    
    result, message = divide_numbers(10, 0)
    print(f"10 / 0 = {result} ({message})")

def demonstrate_scope():
    """Demonstrate variable scope."""
    print("\n=== Variable Scope ===")
    
    # Global variable
    print(f"Global counter before: {global_counter}")
    increment_global()
    print(f"Global counter after: {global_counter}")
    
    # Local variable
    local_scope_demo()
    # print(local_var)  # This would cause an error

def demonstrate_closures():
    """Demonstrate nested functions and closures."""
    print("\n=== Closures ===")
    
    # Closure example
    add_10 = outer_function(10)
    print(f"add_10(5) = {add_10(5)}")
    
    # Factory function
    double = create_multiplier(2)
    triple = create_multiplier(3)
    
    print(f"double(4) = {double(4)}")
    print(f"triple(4) = {triple(4)}")

def demonstrate_recursion():
    """Demonstrate recursive functions."""
    print("\n=== Recursion ===")
    
    # Factorial
    print(f"Factorial of 5: {factorial(5)}")
    
    # Fibonacci
    print(f"Fibonacci of 10: {fibonacci(10)}")
    print(f"Optimized Fibonacci of 10: {fibonacci_optimized(10)}")

def demonstrate_higher_order():
    """Demonstrate higher-order functions."""
    print("\n=== Higher-Order Functions ===")
    
    numbers = [1, 2, 3, 4, 5]
    
    # Apply operation
    squared = apply_operation(numbers, lambda x: x ** 2)
    print(f"Squared: {squared}")
    
    # Validator
    age_validator = create_validator(18, 65)
    print(f"Is 25 valid age? {age_validator(25)}")
    print(f"Is 70 valid age? {age_validator(70)}")

# =============================================================================
# MAIN EXECUTION
# =============================================================================

if __name__ == "__main__":
    """Run all demonstrations when script is executed directly."""
    print("Python Functions Tutorial")
    print("=" * 50)
    
    demonstrate_basic_functions()
    demonstrate_variable_arguments()
    demonstrate_return_values()
    demonstrate_scope()
    demonstrate_closures()
    demonstrate_lambda()
    demonstrate_recursion()
    demonstrate_higher_order()
    
    # Decorator example
    print("\n=== Decorators ===")
    result = slow_function()
    print(f"Result: {result}")
    
    # Function annotations
    print("\n=== Function Annotations ===")
    bmi = calculate_bmi(70.0, 1.75)
    print(f"BMI: {bmi:.2f}")
    
    processed = process_data([1, 2, 3, 4], 3)
    print(f"Processed data: {processed}")
    
    print("\n" + "=" * 50)
    print("Functions tutorial completed!")