"""
Python Performance Optimization
===============================

Created by: Syed Ali Hashmi
LinkedIn: https://www.linkedin.com/in/hashmiali2288

This module demonstrates performance optimization techniques, profiling,
and best practices for writing efficient Python code.
"""

import time
import sys
import cProfile
import timeit
from functools import lru_cache
from collections import defaultdict, deque
import gc

# =============================================================================
# TIMING AND PROFILING
# =============================================================================

def time_function(func, *args, **kwargs):
    """Time a function execution."""
    start_time = time.time()
    result = func(*args, **kwargs)
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"{func.__name__} took {execution_time:.6f} seconds")
    return result, execution_time

def demonstrate_timing():
    """Show different timing techniques."""
    print("=== Timing Techniques ===")
    
    def slow_function():
        """Simulate slow function."""
        total = 0
        for i in range(1000000):
            total += i ** 2
        return total
    
    # Method 1: Manual timing
    result, exec_time = time_function(slow_function)
    
    # Method 2: timeit module
    exec_time_timeit = timeit.timeit(slow_function, number=1)
    print(f"timeit result: {exec_time_timeit:.6f} seconds")
    
    # Method 3: Multiple runs for accuracy
    times = timeit.repeat(lambda: sum(x**2 for x in range(1000)), repeat=5, number=100)
    avg_time = sum(times) / len(times)
    print(f"Average time over 5 runs: {avg_time:.6f} seconds")

# =============================================================================
# ALGORITHM OPTIMIZATION
# =============================================================================

def fibonacci_naive(n):
    """Naive recursive Fibonacci (inefficient)."""
    if n <= 1:
        return n
    return fibonacci_naive(n - 1) + fibonacci_naive(n - 2)

@lru_cache(maxsize=None)
def fibonacci_cached(n):
    """Fibonacci with memoization using lru_cache."""
    if n <= 1:
        return n
    return fibonacci_cached(n - 1) + fibonacci_cached(n - 2)

def fibonacci_iterative(n):
    """Iterative Fibonacci (most efficient)."""
    if n <= 1:
        return n
    
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

def demonstrate_algorithm_optimization():
    """Compare different algorithm implementations."""
    print("\n=== Algorithm Optimization ===")
    
    n = 30
    
    # Time naive approach (warning: slow!)
    print(f"Computing Fibonacci({n}):")
    
    start = time.time()
    result_naive = fibonacci_naive(n)
    time_naive = time.time() - start
    print(f"Naive recursive: {result_naive} in {time_naive:.6f}s")
    
    start = time.time()
    result_cached = fibonacci_cached(n)
    time_cached = time.time() - start
    print(f"Cached recursive: {result_cached} in {time_cached:.6f}s")
    
    start = time.time()
    result_iterative = fibonacci_iterative(n)
    time_iterative = time.time() - start
    print(f"Iterative: {result_iterative} in {time_iterative:.6f}s")
    
    print(f"Speedup (cached vs naive): {time_naive / time_cached:.1f}x")
    print(f"Speedup (iterative vs naive): {time_naive / time_iterative:.1f}x")

# =============================================================================
# DATA STRUCTURE OPTIMIZATION
# =============================================================================

def demonstrate_data_structure_performance():
    """Compare performance of different data structures."""
    print("\n=== Data Structure Performance ===")
    
    # List vs Set for membership testing
    data_list = list(range(10000))
    data_set = set(range(10000))
    
    target = 9999
    
    # List membership (O(n))
    start = time.time()
    for _ in range(1000):
        result = target in data_list
    list_time = time.time() - start
    
    # Set membership (O(1))
    start = time.time()
    for _ in range(1000):
        result = target in data_set
    set_time = time.time() - start
    
    print(f"List membership (1000 lookups): {list_time:.6f}s")
    print(f"Set membership (1000 lookups): {set_time:.6f}s")
    print(f"Set is {list_time / set_time:.1f}x faster")
    
    # Dictionary vs List for key-value storage
    print("\nDictionary vs List for key-value pairs:")
    
    # Using list of tuples
    data_list_kv = [(i, f"value_{i}") for i in range(1000)]
    
    # Using dictionary
    data_dict = {i: f"value_{i}" for i in range(1000)}
    
    target_key = 999
    
    # List search (O(n))
    start = time.time()
    for _ in range(1000):
        for key, value in data_list_kv:
            if key == target_key:
                result = value
                break
    list_kv_time = time.time() - start
    
    # Dictionary lookup (O(1))
    start = time.time()
    for _ in range(1000):
        result = data_dict[target_key]
    dict_time = time.time() - start
    
    print(f"List search (1000 lookups): {list_kv_time:.6f}s")
    print(f"Dict lookup (1000 lookups): {dict_time:.6f}s")
    print(f"Dict is {list_kv_time / dict_time:.1f}x faster")

# =============================================================================
# LOOP OPTIMIZATION
# =============================================================================

def demonstrate_loop_optimization():
    """Show loop optimization techniques."""
    print("\n=== Loop Optimization ===")
    
    data = list(range(100000))
    
    # Inefficient: Function call in loop condition
    def inefficient_loop():
        result = []
        for i in range(len(data)):  # len() called every iteration
            if data[i] % 2 == 0:
                result.append(data[i] ** 2)
        return result
    
    # Better: Store length
    def better_loop():
        result = []
        data_len = len(data)  # Store length once
        for i in range(data_len):
            if data[i] % 2 == 0:
                result.append(data[i] ** 2)
        return result
    
    # Best: List comprehension
    def best_loop():
        return [x ** 2 for x in data if x % 2 == 0]
    
    # Time each approach
    time_inefficient = timeit.timeit(inefficient_loop, number=10)
    time_better = timeit.timeit(better_loop, number=10)
    time_best = timeit.timeit(best_loop, number=10)
    
    print(f"Inefficient loop: {time_inefficient:.6f}s")
    print(f"Better loop: {time_better:.6f}s")
    print(f"List comprehension: {time_best:.6f}s")
    print(f"List comprehension is {time_inefficient / time_best:.1f}x faster")

# =============================================================================
# STRING OPTIMIZATION
# =============================================================================

def demonstrate_string_optimization():
    """Show string operation optimizations."""
    print("\n=== String Optimization ===")
    
    words = ["hello", "world", "python", "performance"] * 1000
    
    # Inefficient: String concatenation in loop
    def inefficient_concat():
        result = ""
        for word in words:
            result += word + " "
        return result
    
    # Better: Using join
    def efficient_concat():
        return " ".join(words)
    
    # Time both approaches
    time_inefficient = timeit.timeit(inefficient_concat, number=100)
    time_efficient = timeit.timeit(efficient_concat, number=100)
    
    print(f"String concatenation in loop: {time_inefficient:.6f}s")
    print(f"Using join(): {time_efficient:.6f}s")
    print(f"join() is {time_inefficient / time_efficient:.1f}x faster")
    
    # String formatting comparison
    name = "Alice"
    age = 30
    
    def old_formatting():
        return "Name: %s, Age: %d" % (name, age)
    
    def format_method():
        return "Name: {}, Age: {}".format(name, age)
    
    def f_string():
        return f"Name: {name}, Age: {age}"
    
    time_old = timeit.timeit(old_formatting, number=100000)
    time_format = timeit.timeit(format_method, number=100000)
    time_f_string = timeit.timeit(f_string, number=100000)
    
    print(f"\nString formatting (100k iterations):")
    print(f"% formatting: {time_old:.6f}s")
    print(f".format(): {time_format:.6f}s")
    print(f"f-strings: {time_f_string:.6f}s")

# =============================================================================
# MEMORY OPTIMIZATION
# =============================================================================

def demonstrate_memory_optimization():
    """Show memory optimization techniques."""
    print("\n=== Memory Optimization ===")
    
    # Generator vs List for large datasets
    def create_large_list():
        return [x ** 2 for x in range(1000000)]
    
    def create_large_generator():
        return (x ** 2 for x in range(1000000))
    
    # Measure memory usage
    import tracemalloc
    
    # List approach
    tracemalloc.start()
    large_list = create_large_list()
    list_memory = tracemalloc.get_traced_memory()[0]
    tracemalloc.stop()
    
    # Generator approach
    tracemalloc.start()
    large_gen = create_large_generator()
    gen_memory = tracemalloc.get_traced_memory()[0]
    tracemalloc.stop()
    
    print(f"List memory usage: {list_memory / 1024 / 1024:.2f} MB")
    print(f"Generator memory usage: {gen_memory / 1024:.2f} KB")
    print(f"Memory savings: {list_memory / gen_memory:.1f}x")
    
    # __slots__ for memory-efficient classes
    class RegularClass:
        def __init__(self, x, y):
            self.x = x
            self.y = y
    
    class SlottedClass:
        __slots__ = ['x', 'y']
        
        def __init__(self, x, y):
            self.x = x
            self.y = y
    
    # Compare memory usage
    regular_objects = [RegularClass(i, i+1) for i in range(1000)]
    slotted_objects = [SlottedClass(i, i+1) for i in range(1000)]
    
    regular_size = sys.getsizeof(regular_objects) + sum(sys.getsizeof(obj.__dict__) for obj in regular_objects)
    slotted_size = sys.getsizeof(slotted_objects) + sum(sys.getsizeof(obj) for obj in slotted_objects)
    
    print(f"\nClass memory comparison (1000 objects):")
    print(f"Regular class: {regular_size / 1024:.2f} KB")
    print(f"Slotted class: {slotted_size / 1024:.2f} KB")
    print(f"Memory savings with __slots__: {regular_size / slotted_size:.1f}x")

# =============================================================================
# CACHING AND MEMOIZATION
# =============================================================================

def expensive_computation(n):
    """Simulate expensive computation."""
    time.sleep(0.1)  # Simulate work
    return n ** 2 + n + 1

@lru_cache(maxsize=128)
def cached_computation(n):
    """Cached version of expensive computation."""
    time.sleep(0.1)  # Simulate work
    return n ** 2 + n + 1

def demonstrate_caching():
    """Show caching benefits."""
    print("\n=== Caching and Memoization ===")
    
    test_values = [1, 2, 3, 1, 2, 4, 1, 5, 2, 3]
    
    # Without caching
    start = time.time()
    results_uncached = [expensive_computation(x) for x in test_values]
    time_uncached = time.time() - start
    
    # With caching
    start = time.time()
    results_cached = [cached_computation(x) for x in test_values]
    time_cached = time.time() - start
    
    print(f"Without caching: {time_uncached:.3f}s")
    print(f"With caching: {time_cached:.3f}s")
    print(f"Speedup: {time_uncached / time_cached:.1f}x")
    
    # Show cache info
    print(f"Cache info: {cached_computation.cache_info()}")

# =============================================================================
# BUILT-IN FUNCTION OPTIMIZATION
# =============================================================================

def demonstrate_builtin_optimization():
    """Show benefits of using built-in functions."""
    print("\n=== Built-in Function Optimization ===")
    
    numbers = list(range(100000))
    
    # Manual sum
    def manual_sum(nums):
        total = 0
        for num in nums:
            total += num
        return total
    
    # Built-in sum
    def builtin_sum(nums):
        return sum(nums)
    
    # Time both approaches
    time_manual = timeit.timeit(lambda: manual_sum(numbers), number=100)
    time_builtin = timeit.timeit(lambda: builtin_sum(numbers), number=100)
    
    print(f"Manual sum: {time_manual:.6f}s")
    print(f"Built-in sum(): {time_builtin:.6f}s")
    print(f"Built-in is {time_manual / time_builtin:.1f}x faster")
    
    # Map vs list comprehension
    def using_map():
        return list(map(lambda x: x ** 2, numbers))
    
    def using_comprehension():
        return [x ** 2 for x in numbers]
    
    time_map = timeit.timeit(using_map, number=10)
    time_comp = timeit.timeit(using_comprehension, number=10)
    
    print(f"\nSquaring numbers:")
    print(f"Using map(): {time_map:.6f}s")
    print(f"List comprehension: {time_comp:.6f}s")

# =============================================================================
# PROFILING TOOLS
# =============================================================================

def profile_example():
    """Function to profile."""
    # Some computations
    data = []
    for i in range(10000):
        data.append(i ** 2)
    
    # Some string operations
    text = ""
    for i in range(1000):
        text += str(i)
    
    # Some dictionary operations
    d = {}
    for i in range(5000):
        d[i] = i ** 2
    
    return len(data), len(text), len(d)

def demonstrate_profiling():
    """Show profiling techniques."""
    print("\n=== Profiling ===")
    
    # Profile with cProfile
    print("Running cProfile...")
    
    profiler = cProfile.Profile()
    profiler.enable()
    
    result = profile_example()
    
    profiler.disable()
    
    print(f"Function result: {result}")
    print("\nTop function calls:")
    
    # Print top 5 time-consuming functions
    import pstats
    import io
    
    s = io.StringIO()
    ps = pstats.Stats(profiler, stream=s)
    ps.sort_stats('cumulative').print_stats(5)
    
    print(s.getvalue())

# =============================================================================
# PERFORMANCE BEST PRACTICES
# =============================================================================

def demonstrate_best_practices():
    """Show performance best practices."""
    print("\n=== Performance Best Practices ===")
    
    print("1. Use appropriate data structures:")
    print("   - Lists for ordered data with frequent appends")
    print("   - Sets for membership testing")
    print("   - Dictionaries for key-value lookups")
    print("   - Deques for frequent insertions/deletions at both ends")
    
    print("\n2. Avoid premature optimization:")
    print("   - Profile first, optimize second")
    print("   - Focus on algorithmic improvements")
    print("   - Use built-in functions when possible")
    
    print("\n3. Memory management:")
    print("   - Use generators for large datasets")
    print("   - Use __slots__ for memory-critical classes")
    print("   - Be aware of reference cycles")
    
    print("\n4. String operations:")
    print("   - Use join() instead of += for multiple concatenations")
    print("   - Use f-strings for formatting")
    print("   - Consider using string methods instead of regex for simple operations")
    
    print("\n5. Loop optimization:")
    print("   - Move invariant calculations outside loops")
    print("   - Use list comprehensions when appropriate")
    print("   - Consider using map() and filter() for functional operations")

# =============================================================================
# MAIN EXECUTION
# =============================================================================

if __name__ == "__main__":
    """Run all demonstrations when script is executed directly."""
    print("Python Performance Optimization Tutorial")
    print("=" * 50)
    
    demonstrate_timing()
    demonstrate_algorithm_optimization()
    demonstrate_data_structure_performance()
    demonstrate_loop_optimization()
    demonstrate_string_optimization()
    demonstrate_memory_optimization()
    demonstrate_caching()
    demonstrate_builtin_optimization()
    demonstrate_profiling()
    demonstrate_best_practices()
    
    print("\n" + "=" * 50)
    print("Performance optimization tutorial completed!")