"""
Python Error Handling (Exception Handling)
==========================================

Created by: Syed Ali Hashmi
LinkedIn: https://www.linkedin.com/in/hashmiali2288

This module demonstrates Python's error handling mechanisms using try/except/finally.
Learn about different exception types, custom exceptions, and best practices.
"""

# =============================================================================
# BASIC EXCEPTION HANDLING
# =============================================================================

def basic_exception_handling():
    """Demonstrate basic try/except usage."""
    print("=== Basic Exception Handling ===")
    
    # Basic try/except
    try:
        result = 10 / 0
        print(f"Result: {result}")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
    
    # Multiple exception types
    try:
        numbers = [1, 2, 3]
        index = int("abc")  # This will raise ValueError
        print(numbers[index])
    except ValueError:
        print("Error: Invalid number format!")
    except IndexError:
        print("Error: Index out of range!")
    
    # Catching multiple exceptions in one block
    try:
        value = int(input("Enter a number (simulation): "))  # Simulated input
        result = 100 / value
        print(f"100 / {value} = {result}")
    except (ValueError, ZeroDivisionError) as e:
        print(f"Input error: {e}")

def demonstrate_exception_hierarchy():
    """Show Python's exception hierarchy."""
    print("\n=== Exception Hierarchy ===")
    
    test_cases = [
        lambda: 10 / 0,                    # ZeroDivisionError
        lambda: int("abc"),                # ValueError
        lambda: [1, 2, 3][10],            # IndexError
        lambda: {"a": 1}["b"],             # KeyError
        lambda: open("nonexistent.txt"),   # FileNotFoundError
    ]
    
    for i, test_func in enumerate(test_cases):
        try:
            test_func()
        except ArithmeticError:
            print(f"Test {i+1}: Caught ArithmeticError (ZeroDivisionError parent)")
        except ValueError:
            print(f"Test {i+1}: Caught ValueError")
        except LookupError:
            print(f"Test {i+1}: Caught LookupError (IndexError/KeyError parent)")
        except OSError:
            print(f"Test {i+1}: Caught OSError (FileNotFoundError parent)")
        except Exception as e:
            print(f"Test {i+1}: Caught general Exception: {type(e).__name__}")

# =============================================================================
# ELSE AND FINALLY CLAUSES
# =============================================================================

def demonstrate_else_finally():
    """Show else and finally clauses in exception handling."""
    print("\n=== Else and Finally Clauses ===")
    
    def safe_divide(a, b):
        """Demonstrate try/except/else/finally."""
        print(f"Attempting to divide {a} by {b}")
        
        try:
            result = a / b
        except ZeroDivisionError:
            print("  Error: Division by zero!")
            return None
        else:
            # Executes only if no exception occurred
            print(f"  Success: {a} / {b} = {result}")
            return result
        finally:
            # Always executes, regardless of exceptions
            print("  Division operation completed")
    
    # Test cases
    test_cases = [(10, 2), (10, 0), (15, 3)]
    
    for a, b in test_cases:
        result = safe_divide(a, b)
        print(f"Returned result: {result}\n")

# =============================================================================
# EXCEPTION INFORMATION
# =============================================================================

def demonstrate_exception_info():
    """Show how to get information about exceptions."""
    print("=== Exception Information ===")
    
    import traceback
    import sys
    
    def problematic_function():
        """Function that will raise an exception."""
        data = {"name": "Alice", "age": 30}
        return data["salary"]  # KeyError
    
    try:
        problematic_function()
    except Exception as e:
        print(f"Exception type: {type(e).__name__}")
        print(f"Exception message: {str(e)}")
        print(f"Exception args: {e.args}")
        
        # Get traceback information
        print("\nTraceback information:")
        traceback.print_exc()
        
        # Get exception info
        exc_type, exc_value, exc_traceback = sys.exc_info()
        print(f"\nException info:")
        print(f"  Type: {exc_type}")
        print(f"  Value: {exc_value}")
        print(f"  Traceback: {exc_traceback}")

# =============================================================================
# CUSTOM EXCEPTIONS
# =============================================================================

class CustomError(Exception):
    """Base class for custom exceptions."""
    pass

class ValidationError(CustomError):
    """Raised when validation fails."""
    
    def __init__(self, message, field_name=None):
        super().__init__(message)
        self.field_name = field_name

class BusinessLogicError(CustomError):
    """Raised when business logic rules are violated."""
    
    def __init__(self, message, error_code=None):
        super().__init__(message)
        self.error_code = error_code

def demonstrate_custom_exceptions():
    """Show how to create and use custom exceptions."""
    print("\n=== Custom Exceptions ===")
    
    def validate_age(age):
        """Validate age with custom exception."""
        if not isinstance(age, int):
            raise ValidationError("Age must be an integer", "age")
        
        if age < 0:
            raise ValidationError("Age cannot be negative", "age")
        
        if age > 150:
            raise ValidationError("Age seems unrealistic", "age")
        
        return True
    
    def process_user_registration(name, age, email):
        """Process user registration with validation."""
        try:
            # Validate inputs
            if not name or len(name) < 2:
                raise ValidationError("Name must be at least 2 characters", "name")
            
            validate_age(age)
            
            if "@" not in email:
                raise ValidationError("Invalid email format", "email")
            
            # Business logic check
            if age < 18:
                raise BusinessLogicError("User must be 18 or older to register", "AGE_RESTRICTION")
            
            return f"User {name} registered successfully!"
            
        except ValidationError as e:
            return f"Validation Error in {e.field_name}: {e}"
        except BusinessLogicError as e:
            return f"Business Logic Error ({e.error_code}): {e}"
    
    # Test cases
    test_users = [
        ("Alice", 25, "alice@email.com"),      # Valid
        ("", 25, "alice@email.com"),           # Invalid name
        ("Bob", -5, "bob@email.com"),          # Invalid age
        ("Charlie", 16, "charlie@email.com"),  # Business logic error
        ("Diana", "thirty", "diana@email.com") # Type error
    ]
    
    for name, age, email in test_users:
        result = process_user_registration(name, age, email)
        print(f"Registration attempt: {result}")

# =============================================================================
# EXCEPTION CHAINING
# =============================================================================

def demonstrate_exception_chaining():
    """Show exception chaining with 'raise from'."""
    print("\n=== Exception Chaining ===")
    
    def parse_config_file(filename):
        """Parse configuration file with exception chaining."""
        try:
            with open(filename, 'r') as file:
                content = file.read()
                # Simulate JSON parsing
                if "invalid" in content:
                    raise ValueError("Invalid JSON format")
                return {"config": "loaded"}
        except FileNotFoundError as e:
            raise CustomError(f"Configuration file not found: {filename}") from e
        except ValueError as e:
            raise CustomError(f"Configuration file is corrupted: {filename}") from e
    
    def initialize_application():
        """Initialize application with chained exceptions."""
        try:
            config = parse_config_file("nonexistent_config.json")
            return config
        except CustomError as e:
            print(f"Application initialization failed: {e}")
            print(f"Original cause: {e.__cause__}")
            return None
    
    initialize_application()

# =============================================================================
# CONTEXT MANAGERS FOR EXCEPTION HANDLING
# =============================================================================

class DatabaseConnection:
    """Simulate database connection with proper cleanup."""
    
    def __init__(self, connection_string):
        self.connection_string = connection_string
        self.connected = False
    
    def __enter__(self):
        print(f"Connecting to database: {self.connection_string}")
        self.connected = True
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        print("Closing database connection")
        self.connected = False
        
        if exc_type is not None:
            print(f"Exception occurred: {exc_type.__name__}: {exc_value}")
            # Return False to propagate the exception
            return False
    
    def execute_query(self, query):
        """Execute a database query."""
        if not self.connected:
            raise RuntimeError("Not connected to database")
        
        if "DROP" in query.upper():
            raise RuntimeError("DROP operations are not allowed")
        
        return f"Query executed: {query}"

def demonstrate_context_manager_exceptions():
    """Show exception handling with context managers."""
    print("\n=== Context Managers and Exceptions ===")
    
    # Successful operation
    try:
        with DatabaseConnection("localhost:5432") as db:
            result = db.execute_query("SELECT * FROM users")
            print(f"Success: {result}")
    except Exception as e:
        print(f"Error: {e}")
    
    print()
    
    # Operation with exception
    try:
        with DatabaseConnection("localhost:5432") as db:
            result = db.execute_query("DROP TABLE users")  # This will raise an exception
            print(f"Success: {result}")
    except Exception as e:
        print(f"Error caught: {e}")

# =============================================================================
# BEST PRACTICES
# =============================================================================

def demonstrate_best_practices():
    """Show best practices for exception handling."""
    print("\n=== Best Practices ===")
    
    # 1. Be specific with exception types
    def good_exception_handling(data):
        """Good: Catch specific exceptions."""
        try:
            return int(data)
        except ValueError:
            print(f"Cannot convert '{data}' to integer")
            return None
        except TypeError:
            print(f"Invalid data type: {type(data)}")
            return None
    
    # 2. Don't catch all exceptions unless necessary
    def avoid_bare_except():
        """Demonstrate why bare except is problematic."""
        try:
            # Some operation
            result = 10 / 2
            return result
        except Exception as e:  # Better than bare except:
            print(f"Unexpected error: {e}")
            raise  # Re-raise the exception
    
    # 3. Use logging instead of print for production code
    import logging
    
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    
    def production_error_handling(filename):
        """Production-ready error handling."""
        try:
            with open(filename, 'r') as file:
                return file.read()
        except FileNotFoundError:
            logger.error(f"File not found: {filename}")
            raise
        except PermissionError:
            logger.error(f"Permission denied: {filename}")
            raise
        except Exception as e:
            logger.error(f"Unexpected error reading {filename}: {e}")
            raise
    
    # 4. Fail fast principle
    def validate_input_early(age, name):
        """Validate inputs early to fail fast."""
        if not isinstance(age, int):
            raise TypeError("Age must be an integer")
        
        if age < 0:
            raise ValueError("Age cannot be negative")
        
        if not name or not isinstance(name, str):
            raise ValueError("Name must be a non-empty string")
        
        # Continue with processing...
        return f"Processing user: {name}, age: {age}"
    
    # Test best practices
    print("Testing best practices:")
    
    # Test specific exception handling
    test_values = ["123", "abc", None]
    for value in test_values:
        result = good_exception_handling(value)
        print(f"  Convert '{value}': {result}")
    
    # Test input validation
    try:
        result = validate_input_early(25, "Alice")
        print(f"  {result}")
    except (TypeError, ValueError) as e:
        print(f"  Validation error: {e}")

# =============================================================================
# DEBUGGING TECHNIQUES
# =============================================================================

def demonstrate_debugging_techniques():
    """Show debugging techniques for exception handling."""
    print("\n=== Debugging Techniques ===")
    
    import pdb
    import traceback
    
    def buggy_function(data):
        """Function with potential bugs."""
        result = []
        for item in data:
            # Potential bug: what if item is not a number?
            processed = item * 2 + 1
            result.append(processed)
        return result
    
    def debug_with_traceback():
        """Use traceback for debugging."""
        test_data = [1, 2, "three", 4]
        
        try:
            result = buggy_function(test_data)
            print(f"Result: {result}")
        except Exception:
            print("Exception occurred! Full traceback:")
            traceback.print_exc()
            
            # Get formatted traceback as string
            tb_str = traceback.format_exc()
            print(f"\nTraceback as string:\n{tb_str}")
    
    def debug_with_logging():
        """Use logging for debugging."""
        import logging
        
        # Configure logging
        logging.basicConfig(
            level=logging.DEBUG,
            format='%(levelname)s - %(message)s'
        )
        
        logger = logging.getLogger(__name__)
        
        test_data = [1, 2, "three", 4]
        logger.debug(f"Processing data: {test_data}")
        
        try:
            result = buggy_function(test_data)
            logger.info(f"Successfully processed data: {result}")
        except Exception as e:
            logger.error(f"Error processing data: {e}")
            logger.debug("Full traceback:", exc_info=True)
    
    print("Debugging with traceback:")
    debug_with_traceback()
    
    print("\nDebugging with logging:")
    debug_with_logging()

# =============================================================================
# MAIN EXECUTION
# =============================================================================

if __name__ == "__main__":
    """Run all demonstrations when script is executed directly."""
    print("Python Error Handling Tutorial")
    print("=" * 50)
    
    basic_exception_handling()
    demonstrate_exception_hierarchy()
    demonstrate_else_finally()
    demonstrate_exception_info()
    demonstrate_custom_exceptions()
    demonstrate_exception_chaining()
    demonstrate_context_manager_exceptions()
    demonstrate_best_practices()
    demonstrate_debugging_techniques()
    
    print("\n" + "=" * 50)
    print("Error handling tutorial completed!")