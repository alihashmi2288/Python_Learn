"""
Python Context Managers
=======================

Created by: Syed Ali Hashmi
LinkedIn: https://www.linkedin.com/in/hashmiali2288

This module demonstrates context managers for resource management and cleanup.
Learn about the 'with' statement, __enter__/__exit__ methods, and contextlib.
"""

import os
import time
import contextlib
from contextlib import contextmanager

# =============================================================================
# BASIC CONTEXT MANAGER CLASS
# =============================================================================

class FileManager:
    """A simple file context manager."""
    
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None
    
    def __enter__(self):
        """Enter the context - open the file."""
        print(f"Opening file: {self.filename}")
        self.file = open(self.filename, self.mode)
        return self.file
    
    def __exit__(self, exc_type, exc_value, traceback):
        """Exit the context - close the file."""
        print(f"Closing file: {self.filename}")
        if self.file:
            self.file.close()
        
        # Handle exceptions
        if exc_type is not None:
            print(f"Exception occurred: {exc_type.__name__}: {exc_value}")
            return False  # Don't suppress the exception
        
        return True

def demonstrate_basic_context_manager():
    """Show basic context manager usage."""
    print("=== Basic Context Manager ===")
    
    # Using our custom context manager
    with FileManager("test.txt", "w") as f:
        f.write("Hello from context manager!")
        f.write("\nThis file will be automatically closed.")
    
    # File is automatically closed here
    print("File operations completed")
    
    # Clean up
    if os.path.exists("test.txt"):
        os.remove("test.txt")

# =============================================================================
# DATABASE CONNECTION CONTEXT MANAGER
# =============================================================================

class DatabaseConnection:
    """Simulate a database connection context manager."""
    
    def __init__(self, connection_string):
        self.connection_string = connection_string
        self.connection = None
        self.transaction_active = False
    
    def __enter__(self):
        """Establish database connection and start transaction."""
        print(f"Connecting to database: {self.connection_string}")
        self.connection = f"Connection to {self.connection_string}"
        
        print("Starting transaction")
        self.transaction_active = True
        
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        """Clean up database connection."""
        if self.transaction_active:
            if exc_type is None:
                print("Committing transaction")
            else:
                print(f"Rolling back transaction due to: {exc_type.__name__}")
            
            self.transaction_active = False
        
        if self.connection:
            print("Closing database connection")
            self.connection = None
        
        # Don't suppress exceptions
        return False
    
    def execute(self, query):
        """Execute a database query."""
        if not self.connection:
            raise RuntimeError("Not connected to database")
        
        print(f"Executing query: {query}")
        return f"Result of: {query}"

def demonstrate_database_context_manager():
    """Show database context manager."""
    print("\n=== Database Context Manager ===")
    
    # Successful operation
    try:
        with DatabaseConnection("postgresql://localhost:5432/mydb") as db:
            result1 = db.execute("SELECT * FROM users")
            result2 = db.execute("UPDATE users SET active = true")
            print("All operations successful")
    except Exception as e:
        print(f"Database error: {e}")
    
    print()
    
    # Operation with exception
    try:
        with DatabaseConnection("postgresql://localhost:5432/mydb") as db:
            result1 = db.execute("SELECT * FROM users")
            raise ValueError("Simulated error")  # This will trigger rollback
            result2 = db.execute("UPDATE users SET active = true")
    except ValueError as e:
        print(f"Caught exception: {e}")

# =============================================================================
# TIMING CONTEXT MANAGER
# =============================================================================

class Timer:
    """Context manager for timing code execution."""
    
    def __init__(self, description="Operation"):
        self.description = description
        self.start_time = None
        self.end_time = None
    
    def __enter__(self):
        """Start timing."""
        print(f"Starting: {self.description}")
        self.start_time = time.time()
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        """Stop timing and report duration."""
        self.end_time = time.time()
        duration = self.end_time - self.start_time
        
        if exc_type is None:
            print(f"Completed: {self.description} in {duration:.4f} seconds")
        else:
            print(f"Failed: {self.description} after {duration:.4f} seconds")
        
        return False
    
    @property
    def elapsed_time(self):
        """Get elapsed time."""
        if self.start_time and self.end_time:
            return self.end_time - self.start_time
        return None

def demonstrate_timing_context_manager():
    """Show timing context manager."""
    print("\n=== Timing Context Manager ===")
    
    # Time a simple operation
    with Timer("Simple calculation") as timer:
        result = sum(range(1000000))
        print(f"Sum calculated: {result}")
    
    # Time a sleep operation
    with Timer("Sleep operation"):
        time.sleep(0.1)
    
    # Time an operation that fails
    try:
        with Timer("Failing operation"):
            time.sleep(0.05)
            raise ValueError("Simulated failure")
    except ValueError:
        print("Exception handled outside context manager")

# =============================================================================
# CONTEXTLIB DECORATORS
# =============================================================================

@contextmanager
def temporary_file(filename, content=""):
    """Context manager using @contextmanager decorator."""
    print(f"Creating temporary file: {filename}")
    
    try:
        # Setup
        with open(filename, 'w') as f:
            f.write(content)
        
        # Yield the filename to the with block
        yield filename
        
    finally:
        # Cleanup
        if os.path.exists(filename):
            os.remove(filename)
            print(f"Removed temporary file: {filename}")

@contextmanager
def change_directory(path):
    """Context manager to temporarily change directory."""
    original_path = os.getcwd()
    print(f"Changing directory from {original_path} to {path}")
    
    try:
        os.chdir(path)
        yield path
    finally:
        os.chdir(original_path)
        print(f"Restored directory to {original_path}")

def demonstrate_contextlib_decorators():
    """Show contextlib @contextmanager decorator."""
    print("\n=== Contextlib Decorators ===")
    
    # Temporary file context manager
    with temporary_file("temp_data.txt", "Temporary content\nLine 2\nLine 3") as filename:
        print(f"Working with file: {filename}")
        
        # Read the file
        with open(filename, 'r') as f:
            content = f.read()
            print(f"File content:\n{content}")
    
    print("Temporary file automatically cleaned up")
    
    # Directory change context manager
    current_dir = os.getcwd()
    parent_dir = os.path.dirname(current_dir)
    
    print(f"\nCurrent directory: {current_dir}")
    
    with change_directory(parent_dir):
        print(f"Inside context: {os.getcwd()}")
        # Do some work in the different directory
    
    print(f"Back to original: {os.getcwd()}")

# =============================================================================
# MULTIPLE CONTEXT MANAGERS
# =============================================================================

class ResourceManager:
    """Simulate a resource that needs cleanup."""
    
    def __init__(self, name):
        self.name = name
        self.acquired = False
    
    def __enter__(self):
        print(f"Acquiring resource: {self.name}")
        self.acquired = True
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        print(f"Releasing resource: {self.name}")
        self.acquired = False
        return False
    
    def use(self):
        if not self.acquired:
            raise RuntimeError(f"Resource {self.name} not acquired")
        print(f"Using resource: {self.name}")

def demonstrate_multiple_context_managers():
    """Show multiple context managers."""
    print("\n=== Multiple Context Managers ===")
    
    # Multiple context managers in one with statement
    with ResourceManager("Database") as db, \
         ResourceManager("Cache") as cache, \
         ResourceManager("Logger") as logger:
        
        db.use()
        cache.use()
        logger.use()
        print("All resources used successfully")
    
    print("All resources automatically released")

# =============================================================================
# EXCEPTION HANDLING IN CONTEXT MANAGERS
# =============================================================================

class SafeResource:
    """Context manager with sophisticated exception handling."""
    
    def __init__(self, name, suppress_exceptions=False):
        self.name = name
        self.suppress_exceptions = suppress_exceptions
        self.resource = None
    
    def __enter__(self):
        print(f"Acquiring safe resource: {self.name}")
        self.resource = f"Resource-{self.name}"
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        print(f"Cleaning up safe resource: {self.name}")
        
        if exc_type is not None:
            print(f"Exception in context: {exc_type.__name__}: {exc_value}")
            
            # Log the exception or perform cleanup based on exception type
            if exc_type == ValueError:
                print("Handling ValueError specifically")
            elif exc_type == RuntimeError:
                print("Handling RuntimeError specifically")
            
            # Return True to suppress the exception, False to propagate it
            return self.suppress_exceptions
        
        return False
    
    def work(self):
        print(f"Working with {self.resource}")

def demonstrate_exception_handling():
    """Show exception handling in context managers."""
    print("\n=== Exception Handling in Context Managers ===")
    
    # Context manager that propagates exceptions
    print("1. Exception propagation:")
    try:
        with SafeResource("PropagateExceptions", suppress_exceptions=False):
            raise ValueError("Something went wrong")
    except ValueError as e:
        print(f"Caught propagated exception: {e}")
    
    print("\n2. Exception suppression:")
    with SafeResource("SuppressExceptions", suppress_exceptions=True):
        raise RuntimeError("This will be suppressed")
    
    print("Execution continued after suppressed exception")

# =============================================================================
# CONTEXTLIB UTILITIES
# =============================================================================

def demonstrate_contextlib_utilities():
    """Show useful contextlib utilities."""
    print("\n=== Contextlib Utilities ===")
    
    # contextlib.suppress - suppress specific exceptions
    print("1. contextlib.suppress:")
    
    with contextlib.suppress(FileNotFoundError):
        os.remove("nonexistent_file.txt")
        print("This won't print because file doesn't exist")
    
    print("File removal attempted, exception suppressed")
    
    # contextlib.closing - ensure close() is called
    print("\n2. contextlib.closing:")
    
    class CustomResource:
        def __init__(self, name):
            self.name = name
            print(f"Created resource: {name}")
        
        def close(self):
            print(f"Closed resource: {self.name}")
        
        def work(self):
            print(f"Working with: {self.name}")
    
    with contextlib.closing(CustomResource("TestResource")) as resource:
        resource.work()
    
    # contextlib.redirect_stdout
    print("\n3. contextlib.redirect_stdout:")
    
    import io
    
    output_buffer = io.StringIO()
    with contextlib.redirect_stdout(output_buffer):
        print("This goes to the buffer")
        print("So does this")
    
    captured_output = output_buffer.getvalue()
    print(f"Captured output: {repr(captured_output)}")

# =============================================================================
# NESTED CONTEXT MANAGERS
# =============================================================================

@contextmanager
def nested_operation(level, max_level=3):
    """Demonstrate nested context managers."""
    print("  " * level + f"Entering level {level}")
    
    try:
        if level < max_level:
            with nested_operation(level + 1, max_level):
                yield f"Level {level}"
        else:
            yield f"Level {level} (deepest)"
    finally:
        print("  " * level + f"Exiting level {level}")

def demonstrate_nested_context_managers():
    """Show nested context managers."""
    print("\n=== Nested Context Managers ===")
    
    with nested_operation(0) as result:
        print(f"Working at: {result}")

# =============================================================================
# PRACTICAL EXAMPLES
# =============================================================================

@contextmanager
def atomic_write(filename):
    """Atomic file writing - write to temp file, then rename."""
    temp_filename = filename + ".tmp"
    
    try:
        with open(temp_filename, 'w') as f:
            yield f
        
        # If we get here, writing succeeded
        if os.path.exists(filename):
            os.remove(filename)
        os.rename(temp_filename, filename)
        print(f"Atomically wrote to {filename}")
        
    except Exception:
        # Clean up temp file on error
        if os.path.exists(temp_filename):
            os.remove(temp_filename)
        raise

@contextmanager
def environment_variable(key, value):
    """Temporarily set an environment variable."""
    old_value = os.environ.get(key)
    os.environ[key] = value
    
    try:
        yield
    finally:
        if old_value is None:
            os.environ.pop(key, None)
        else:
            os.environ[key] = old_value

def demonstrate_practical_examples():
    """Show practical context manager examples."""
    print("\n=== Practical Examples ===")
    
    # Atomic file writing
    print("1. Atomic file writing:")
    try:
        with atomic_write("important_data.txt") as f:
            f.write("Critical data\n")
            f.write("More critical data\n")
            # If an exception occurs here, the original file is preserved
    except Exception as e:
        print(f"Write failed: {e}")
    
    # Check if file was created
    if os.path.exists("important_data.txt"):
        with open("important_data.txt", 'r') as f:
            print(f"File contents: {f.read().strip()}")
        os.remove("important_data.txt")
    
    # Environment variable management
    print("\n2. Environment variable management:")
    print(f"Before: TEST_VAR = {os.environ.get('TEST_VAR', 'Not set')}")
    
    with environment_variable("TEST_VAR", "temporary_value"):
        print(f"Inside: TEST_VAR = {os.environ.get('TEST_VAR')}")
    
    print(f"After: TEST_VAR = {os.environ.get('TEST_VAR', 'Not set')}")

# =============================================================================
# MAIN EXECUTION
# =============================================================================

if __name__ == "__main__":
    """Run all demonstrations when script is executed directly."""
    print("Python Context Managers Tutorial")
    print("=" * 50)
    
    demonstrate_basic_context_manager()
    demonstrate_database_context_manager()
    demonstrate_timing_context_manager()
    demonstrate_contextlib_decorators()
    demonstrate_multiple_context_managers()
    demonstrate_exception_handling()
    demonstrate_contextlib_utilities()
    demonstrate_nested_context_managers()
    demonstrate_practical_examples()
    
    print("\n" + "=" * 50)
    print("Context managers tutorial completed!")