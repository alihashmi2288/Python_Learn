"""
Python Generators and Iterators
===============================

Created by: Syed Ali Hashmi
LinkedIn: https://www.linkedin.com/in/hashmiali2288

This module demonstrates generators and iterators for memory-efficient data processing.
Learn about yield, generator expressions, and the iterator protocol.
"""

import sys
import time
from itertools import islice, count, cycle, chain

# =============================================================================
# BASIC GENERATORS
# =============================================================================

def simple_generator():
    """A simple generator function."""
    print("Generator started")
    yield 1
    print("Between yields")
    yield 2
    print("Generator ending")
    yield 3

def demonstrate_basic_generator():
    """Show basic generator usage."""
    print("=== Basic Generator ===")
    
    gen = simple_generator()
    print(f"Generator object: {gen}")
    
    print("Getting values:")
    print(f"First: {next(gen)}")
    print(f"Second: {next(gen)}")
    print(f"Third: {next(gen)}")
    
    try:
        print(f"Fourth: {next(gen)}")
    except StopIteration:
        print("Generator exhausted")

# =============================================================================
# PRACTICAL GENERATORS
# =============================================================================

def fibonacci_generator(limit=None):
    """Generate Fibonacci numbers."""
    a, b = 0, 1
    count = 0
    
    while limit is None or count < limit:
        yield a
        a, b = b, a + b
        count += 1

def countdown(start):
    """Countdown generator."""
    while start > 0:
        yield start
        start -= 1
    yield "Blast off!"

def read_file_lines(filename):
    """Generator to read file lines one at a time."""
    try:
        with open(filename, 'r') as file:
            for line in file:
                yield line.strip()
    except FileNotFoundError:
        print(f"File {filename} not found")

def demonstrate_practical_generators():
    """Show practical generator examples."""
    print("\n=== Practical Generators ===")
    
    # Fibonacci generator
    print("First 10 Fibonacci numbers:")
    fib_gen = fibonacci_generator(10)
    for num in fib_gen:
        print(num, end=" ")
    print()
    
    # Countdown generator
    print("\nCountdown:")
    for value in countdown(5):
        print(value)
    
    # Create a sample file for demonstration
    sample_content = "Line 1\nLine 2\nLine 3\nLine 4\nLine 5"
    with open("sample.txt", "w") as f:
        f.write(sample_content)
    
    # File reading generator
    print("\nReading file lines:")
    for line in read_file_lines("sample.txt"):
        print(f"  {line}")
    
    # Clean up
    import os
    os.remove("sample.txt")

# =============================================================================
# GENERATOR EXPRESSIONS
# =============================================================================

def demonstrate_generator_expressions():
    """Show generator expressions."""
    print("\n=== Generator Expressions ===")
    
    # Basic generator expression
    squares_gen = (x**2 for x in range(10))
    print("Squares generator:", squares_gen)
    
    print("First 5 squares:")
    for i, square in enumerate(squares_gen):
        if i >= 5:
            break
        print(square, end=" ")
    print()
    
    # Generator with condition
    even_squares = (x**2 for x in range(20) if x % 2 == 0)
    print("Even squares:", list(even_squares))
    
    # Memory efficiency demonstration
    print("\nMemory usage comparison:")
    
    # List comprehension (creates all items in memory)
    large_list = [x**2 for x in range(1000000)]
    list_size = sys.getsizeof(large_list)
    print(f"List size: {list_size:,} bytes")
    
    # Generator expression (creates items on demand)
    large_gen = (x**2 for x in range(1000000))
    gen_size = sys.getsizeof(large_gen)
    print(f"Generator size: {gen_size:,} bytes")
    
    print(f"Memory savings: {list_size / gen_size:.1f}x")

# =============================================================================
# ITERATOR PROTOCOL
# =============================================================================

class CountDown:
    """Custom iterator implementing the iterator protocol."""
    
    def __init__(self, start):
        self.start = start
        self.current = start
    
    def __iter__(self):
        """Return the iterator object (self)."""
        return self
    
    def __next__(self):
        """Return the next item in the sequence."""
        if self.current <= 0:
            raise StopIteration
        
        self.current -= 1
        return self.current + 1

class NumberRange:
    """Iterable class that returns an iterator."""
    
    def __init__(self, start, end, step=1):
        self.start = start
        self.end = end
        self.step = step
    
    def __iter__(self):
        """Return a new iterator instance."""
        return NumberRangeIterator(self.start, self.end, self.step)

class NumberRangeIterator:
    """Iterator for NumberRange."""
    
    def __init__(self, start, end, step):
        self.current = start
        self.end = end
        self.step = step
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current >= self.end:
            raise StopIteration
        
        value = self.current
        self.current += self.step
        return value

def demonstrate_iterator_protocol():
    """Show custom iterators."""
    print("\n=== Iterator Protocol ===")
    
    # Custom iterator
    print("CountDown iterator:")
    countdown = CountDown(5)
    for num in countdown:
        print(num, end=" ")
    print()
    
    # Iterable class
    print("\nNumberRange iterable:")
    number_range = NumberRange(0, 10, 2)
    for num in number_range:
        print(num, end=" ")
    print()
    
    # Multiple iterations
    print("\nMultiple iterations:")
    for i, num in enumerate(NumberRange(1, 4)):
        print(f"Iteration {i+1}: {num}")

# =============================================================================
# ADVANCED GENERATOR TECHNIQUES
# =============================================================================

def generator_with_send():
    """Generator that can receive values via send()."""
    print("Generator started")
    value = yield "Ready"
    
    while True:
        if value is None:
            break
        
        result = f"Received: {value}"
        print(result)
        value = yield result

def coroutine_example():
    """Simple coroutine using generators."""
    def accumulator():
        total = 0
        while True:
            value = yield total
            if value is not None:
                total += value
    
    acc = accumulator()
    next(acc)  # Prime the generator
    
    print("Accumulator coroutine:")
    print(f"Initial: {acc.send(None)}")
    print(f"Add 10: {acc.send(10)}")
    print(f"Add 5: {acc.send(5)}")
    print(f"Add 3: {acc.send(3)}")

def demonstrate_advanced_generators():
    """Show advanced generator techniques."""
    print("\n=== Advanced Generator Techniques ===")
    
    # Generator with send
    print("Generator with send():")
    gen = generator_with_send()
    
    print(next(gen))  # Start generator
    print(gen.send("Hello"))
    print(gen.send("World"))
    gen.send(None)  # Stop generator
    
    # Coroutine example
    coroutine_example()

# =============================================================================
# GENERATOR PIPELINES
# =============================================================================

def numbers(start, end):
    """Generate numbers in range."""
    for i in range(start, end):
        yield i

def squares(numbers_gen):
    """Square each number from generator."""
    for num in numbers_gen:
        yield num ** 2

def filter_even(numbers_gen):
    """Filter even numbers from generator."""
    for num in numbers_gen:
        if num % 2 == 0:
            yield num

def take(n, generator):
    """Take first n items from generator."""
    for i, item in enumerate(generator):
        if i >= n:
            break
        yield item

def demonstrate_generator_pipelines():
    """Show generator pipelines for data processing."""
    print("\n=== Generator Pipelines ===")
    
    # Create a pipeline
    pipeline = take(5, filter_even(squares(numbers(1, 20))))
    
    print("Pipeline: numbers -> squares -> filter_even -> take(5)")
    result = list(pipeline)
    print(f"Result: {result}")
    
    # Another pipeline example
    def process_data():
        """Simulate data processing pipeline."""
        # Generate data
        data = (x for x in range(100))
        
        # Transform data
        transformed = (x * 2 for x in data)
        
        # Filter data
        filtered = (x for x in transformed if x % 3 == 0)
        
        # Take first 10
        return list(islice(filtered, 10))
    
    print("\nData processing pipeline:")
    processed = process_data()
    print(f"Processed data: {processed}")

# =============================================================================
# ITERTOOLS MODULE
# =============================================================================

def demonstrate_itertools():
    """Show useful itertools functions."""
    print("\n=== Itertools Module ===")
    
    # count - infinite arithmetic sequence
    print("count(10, 2) - first 5:")
    counter = count(10, 2)
    for i, num in enumerate(counter):
        if i >= 5:
            break
        print(num, end=" ")
    print()
    
    # cycle - infinite repetition
    print("\ncycle(['A', 'B', 'C']) - first 8:")
    cycler = cycle(['A', 'B', 'C'])
    for i, item in enumerate(cycler):
        if i >= 8:
            break
        print(item, end=" ")
    print()
    
    # chain - concatenate iterables
    print("\nchain([1,2], [3,4], [5,6]):")
    chained = chain([1, 2], [3, 4], [5, 6])
    print(list(chained))
    
    # islice - slice an iterator
    print("\nislice(range(20), 5, 15, 2):")
    sliced = islice(range(20), 5, 15, 2)
    print(list(sliced))

# =============================================================================
# PERFORMANCE COMPARISON
# =============================================================================

def demonstrate_performance():
    """Compare performance of different approaches."""
    print("\n=== Performance Comparison ===")
    
    def list_approach(n):
        """Create list of squares."""
        return [x**2 for x in range(n)]
    
    def generator_approach(n):
        """Create generator of squares."""
        return (x**2 for x in range(n))
    
    n = 1000000
    
    # Time list creation
    start_time = time.time()
    squares_list = list_approach(n)
    list_time = time.time() - start_time
    
    # Time generator creation
    start_time = time.time()
    squares_gen = generator_approach(n)
    gen_time = time.time() - start_time
    
    print(f"List creation time: {list_time:.6f} seconds")
    print(f"Generator creation time: {gen_time:.6f} seconds")
    
    # Memory usage
    list_memory = sys.getsizeof(squares_list)
    gen_memory = sys.getsizeof(squares_gen)
    
    print(f"List memory: {list_memory:,} bytes")
    print(f"Generator memory: {gen_memory:,} bytes")
    print(f"Memory ratio: {list_memory / gen_memory:.1f}x")

# =============================================================================
# PRACTICAL APPLICATIONS
# =============================================================================

def file_processor(directory_path="."):
    """Generator to process files in directory."""
    import os
    
    for filename in os.listdir(directory_path):
        if filename.endswith('.py'):
            filepath = os.path.join(directory_path, filename)
            try:
                with open(filepath, 'r') as file:
                    line_count = sum(1 for line in file)
                    yield filename, line_count
            except Exception as e:
                yield filename, f"Error: {e}"

def batch_processor(items, batch_size):
    """Process items in batches."""
    batch = []
    for item in items:
        batch.append(item)
        if len(batch) == batch_size:
            yield batch
            batch = []
    
    if batch:  # Yield remaining items
        yield batch

def demonstrate_practical_applications():
    """Show practical generator applications."""
    print("\n=== Practical Applications ===")
    
    # File processing
    print("Python files in current directory:")
    for filename, line_count in file_processor():
        print(f"  {filename}: {line_count} lines")
    
    # Batch processing
    print("\nBatch processing:")
    data = range(23)  # 23 items
    
    for i, batch in enumerate(batch_processor(data, 5)):
        print(f"  Batch {i+1}: {list(batch)}")

# =============================================================================
# MAIN EXECUTION
# =============================================================================

if __name__ == "__main__":
    """Run all demonstrations when script is executed directly."""
    print("Python Generators and Iterators Tutorial")
    print("=" * 50)
    
    demonstrate_basic_generator()
    demonstrate_practical_generators()
    demonstrate_generator_expressions()
    demonstrate_iterator_protocol()
    demonstrate_advanced_generators()
    demonstrate_generator_pipelines()
    demonstrate_itertools()
    demonstrate_performance()
    demonstrate_practical_applications()
    
    print("\n" + "=" * 50)
    print("Generators and iterators tutorial completed!")