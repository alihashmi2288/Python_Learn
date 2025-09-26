"""
Python Decorators
=================

This module demonstrates Python decorators - functions that modify other functions.
Learn about function decorators, class decorators, and built-in decorators.
"""

import time
import functools
from datetime import datetime

# =============================================================================
# BASIC DECORATORS
# =============================================================================

def simple_decorator(func):
    """A simple decorator that prints before and after function execution."""
    def wrapper():
        print("Before function execution")
        result = func()
        print("After function execution")
        return result
    return wrapper

@simple_decorator
def say_hello():
    """Function decorated with simple_decorator."""
    print("Hello, World!")
    return "greeting_sent"

def demonstrate_basic_decorators():
    """Show basic decorator usage."""
    print("=== Basic Decorators ===")
    
    # Call decorated function
    result = say_hello()
    print(f"Function returned: {result}")

# =============================================================================
# DECORATORS WITH ARGUMENTS
# =============================================================================

def decorator_with_args(func):
    """Decorator that handles function arguments."""
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args: {args}, kwargs: {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned: {result}")
        return result
    return wrapper

@decorator_with_args
def add_numbers(a, b):
    """Add two numbers."""
    return a + b

@decorator_with_args
def greet_person(name, greeting="Hello"):
    """Greet a person with optional greeting."""
    return f"{greeting}, {name}!"

def demonstrate_decorator_args():
    """Show decorators with function arguments."""
    print("\n=== Decorators with Arguments ===")
    
    result1 = add_numbers(5, 3)
    result2 = greet_person("Alice", greeting="Hi")

# =============================================================================
# TIMING DECORATOR
# =============================================================================

def timing_decorator(func):
    """Decorator to measure function execution time."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"{func.__name__} executed in {execution_time:.4f} seconds")
        return result
    return wrapper

@timing_decorator
def slow_function():
    """A function that takes some time to execute."""
    time.sleep(0.1)  # Simulate work
    return "Task completed"

@timing_decorator
def calculate_factorial(n):
    """Calculate factorial (recursive)."""
    if n <= 1:
        return 1
    return n * calculate_factorial(n - 1)

def demonstrate_timing_decorator():
    """Show timing decorator in action."""
    print("\n=== Timing Decorator ===")
    
    result1 = slow_function()
    result2 = calculate_factorial(10)
    print(f"Factorial result: {result2}")

# =============================================================================
# CACHING DECORATOR
# =============================================================================

def memoize(func):
    """Decorator to cache function results."""
    cache = {}
    
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Create cache key from arguments
        key = str(args) + str(sorted(kwargs.items()))
        
        if key in cache:
            print(f"Cache hit for {func.__name__}{args}")
            return cache[key]
        
        print(f"Computing {func.__name__}{args}")
        result = func(*args, **kwargs)
        cache[key] = result
        return result
    
    # Add cache inspection methods
    wrapper.cache = cache
    wrapper.cache_clear = lambda: cache.clear()
    
    return wrapper

@memoize
def fibonacci(n):
    """Calculate Fibonacci number with memoization."""
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

@memoize
def expensive_calculation(x, y):
    """Simulate expensive calculation."""
    time.sleep(0.1)  # Simulate work
    return x ** 2 + y ** 2

def demonstrate_caching_decorator():
    """Show caching decorator benefits."""
    print("\n=== Caching Decorator ===")
    
    # First calculation
    print("First Fibonacci calculation:")
    result1 = fibonacci(10)
    print(f"fibonacci(10) = {result1}")
    
    # Second calculation (should use cache)
    print("\nSecond Fibonacci calculation:")
    result2 = fibonacci(10)
    print(f"fibonacci(10) = {result2}")
    
    # Expensive calculation
    print("\nExpensive calculations:")
    result3 = expensive_calculation(5, 3)
    result4 = expensive_calculation(5, 3)  # Should use cache
    print(f"Results: {result3}, {result4}")
    
    # Show cache contents
    print(f"Fibonacci cache size: {len(fibonacci.cache)}")

# =============================================================================
# PARAMETRIZED DECORATORS
# =============================================================================

def retry(max_attempts=3, delay=1):
    """Decorator that retries function execution on failure."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None
            
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_exception = e
                    print(f"Attempt {attempt + 1} failed: {e}")
                    if attempt < max_attempts - 1:
                        time.sleep(delay)
            
            print(f"All {max_attempts} attempts failed")
            raise last_exception
        
        return wrapper
    return decorator

def log_calls(log_file=None):
    """Decorator to log function calls."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            log_message = f"[{timestamp}] Called {func.__name__} with args={args}, kwargs={kwargs}"
            
            if log_file:
                with open(log_file, 'a') as f:
                    f.write(log_message + '\n')
            else:
                print(log_message)
            
            return func(*args, **kwargs)
        return wrapper
    return decorator

@retry(max_attempts=3, delay=0.1)
def unreliable_function(success_rate=0.3):
    """Function that randomly fails."""
    import random
    if random.random() < success_rate:
        return "Success!"
    raise Exception("Random failure")

@log_calls()
def important_function(data):
    """Function that should be logged."""
    return f"Processed: {data}"

def demonstrate_parametrized_decorators():
    """Show parametrized decorators."""
    print("\n=== Parametrized Decorators ===")
    
    # Retry decorator
    try:
        result = unreliable_function(success_rate=0.8)
        print(f"Unreliable function result: {result}")
    except Exception as e:
        print(f"Function ultimately failed: {e}")
    
    # Logging decorator
    result = important_function("test data")
    print(f"Important function result: {result}")

# =============================================================================
# CLASS DECORATORS
# =============================================================================

def add_string_representation(cls):
    """Class decorator to add string representation."""
    def __str__(self):
        attrs = ', '.join(f"{k}={v}" for k, v in self.__dict__.items())
        return f"{cls.__name__}({attrs})"
    
    cls.__str__ = __str__
    return cls

def singleton(cls):
    """Class decorator to implement singleton pattern."""
    instances = {}
    
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    
    return get_instance

@add_string_representation
class Person:
    """Person class with automatic string representation."""
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

@singleton
class DatabaseConnection:
    """Singleton database connection class."""
    
    def __init__(self):
        self.connection_id = id(self)
        print(f"Creating database connection: {self.connection_id}")

def demonstrate_class_decorators():
    """Show class decorators."""
    print("\n=== Class Decorators ===")
    
    # String representation decorator
    person = Person("Alice", 30)
    print(f"Person object: {person}")
    
    # Singleton decorator
    db1 = DatabaseConnection()
    db2 = DatabaseConnection()
    print(f"Same instance? {db1 is db2}")
    print(f"Connection IDs: {db1.connection_id}, {db2.connection_id}")

# =============================================================================
# BUILT-IN DECORATORS
# =============================================================================

class MathOperations:
    """Class demonstrating built-in decorators."""
    
    def __init__(self, value):
        self._value = value
    
    @property
    def value(self):
        """Get the value."""
        return self._value
    
    @value.setter
    def value(self, new_value):
        """Set the value with validation."""
        if not isinstance(new_value, (int, float)):
            raise TypeError("Value must be a number")
        self._value = new_value
    
    @staticmethod
    def add(a, b):
        """Static method to add two numbers."""
        return a + b
    
    @classmethod
    def create_zero(cls):
        """Class method to create instance with zero value."""
        return cls(0)
    
    @classmethod
    def create_from_string(cls, value_str):
        """Class method to create instance from string."""
        return cls(float(value_str))

def demonstrate_builtin_decorators():
    """Show built-in decorators."""
    print("\n=== Built-in Decorators ===")
    
    # Property decorator
    math_op = MathOperations(10)
    print(f"Initial value: {math_op.value}")
    
    math_op.value = 20
    print(f"Updated value: {math_op.value}")
    
    try:
        math_op.value = "invalid"
    except TypeError as e:
        print(f"Validation error: {e}")
    
    # Static method
    result = MathOperations.add(5, 3)
    print(f"Static method result: {result}")
    
    # Class methods
    zero_instance = MathOperations.create_zero()
    string_instance = MathOperations.create_from_string("42.5")
    
    print(f"Zero instance value: {zero_instance.value}")
    print(f"String instance value: {string_instance.value}")

# =============================================================================
# DECORATOR CHAINING
# =============================================================================

def bold(func):
    """Decorator to make output bold."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return f"**{result}**"
    return wrapper

def italic(func):
    """Decorator to make output italic."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return f"*{result}*"
    return wrapper

def uppercase(func):
    """Decorator to make output uppercase."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper

@bold
@italic
@uppercase
def format_message(message):
    """Function with multiple decorators."""
    return f"Message: {message}"

def demonstrate_decorator_chaining():
    """Show decorator chaining."""
    print("\n=== Decorator Chaining ===")
    
    result = format_message("hello world")
    print(f"Formatted message: {result}")
    
    # Show execution order
    print("Execution order: uppercase -> italic -> bold")

# =============================================================================
# PRACTICAL EXAMPLES
# =============================================================================

def validate_types(**expected_types):
    """Decorator to validate function argument types."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Get function signature
            import inspect
            sig = inspect.signature(func)
            bound_args = sig.bind(*args, **kwargs)
            bound_args.apply_defaults()
            
            # Validate types
            for param_name, expected_type in expected_types.items():
                if param_name in bound_args.arguments:
                    value = bound_args.arguments[param_name]
                    if not isinstance(value, expected_type):
                        raise TypeError(
                            f"Parameter '{param_name}' must be of type {expected_type.__name__}, "
                            f"got {type(value).__name__}"
                        )
            
            return func(*args, **kwargs)
        return wrapper
    return decorator

@validate_types(name=str, age=int, salary=float)
def create_employee(name, age, salary=50000.0):
    """Create employee with type validation."""
    return {"name": name, "age": age, "salary": salary}

def rate_limit(calls_per_second=1):
    """Decorator to limit function call rate."""
    def decorator(func):
        last_called = [0.0]
        
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            now = time.time()
            time_since_last = now - last_called[0]
            min_interval = 1.0 / calls_per_second
            
            if time_since_last < min_interval:
                sleep_time = min_interval - time_since_last
                print(f"Rate limiting: sleeping for {sleep_time:.2f} seconds")
                time.sleep(sleep_time)
            
            last_called[0] = time.time()
            return func(*args, **kwargs)
        
        return wrapper
    return decorator

@rate_limit(calls_per_second=2)
def api_call(endpoint):
    """Simulate API call with rate limiting."""
    return f"Called API endpoint: {endpoint}"

def demonstrate_practical_decorators():
    """Show practical decorator examples."""
    print("\n=== Practical Decorators ===")
    
    # Type validation
    try:
        employee = create_employee("Alice", 30, 75000.0)
        print(f"Valid employee: {employee}")
        
        invalid_employee = create_employee("Bob", "thirty", 60000.0)
    except TypeError as e:
        print(f"Type validation error: {e}")
    
    # Rate limiting
    print("\nRate limiting demo:")
    for i in range(3):
        result = api_call(f"/users/{i}")
        print(f"  {result}")

# =============================================================================
# MAIN EXECUTION
# =============================================================================

if __name__ == "__main__":
    """Run all demonstrations when script is executed directly."""
    print("Python Decorators Tutorial")
    print("=" * 50)
    
    demonstrate_basic_decorators()
    demonstrate_decorator_args()
    demonstrate_timing_decorator()
    demonstrate_caching_decorator()
    demonstrate_parametrized_decorators()
    demonstrate_class_decorators()
    demonstrate_builtin_decorators()
    demonstrate_decorator_chaining()
    demonstrate_practical_decorators()
    
    print("\n" + "=" * 50)
    print("Decorators tutorial completed!")