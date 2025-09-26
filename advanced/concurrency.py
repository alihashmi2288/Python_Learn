"""
Python Concurrency
==================

Created by: Syed Ali Hashmi
LinkedIn: https://www.linkedin.com/in/hashmiali2288

This module demonstrates concurrent programming in Python using threading,
multiprocessing, and asyncio for parallel and asynchronous execution.
"""

import threading
import multiprocessing
import asyncio
import time
import concurrent.futures
from queue import Queue
import requests

# =============================================================================
# THREADING BASICS
# =============================================================================

def worker_function(name, duration):
    """Simple worker function for threading examples."""
    print(f"Worker {name} starting")
    time.sleep(duration)
    print(f"Worker {name} finished after {duration} seconds")
    return f"Result from {name}"

def demonstrate_basic_threading():
    """Show basic threading concepts."""
    print("=== Basic Threading ===")
    
    # Create and start threads
    thread1 = threading.Thread(target=worker_function, args=("A", 2))
    thread2 = threading.Thread(target=worker_function, args=("B", 1))
    
    start_time = time.time()
    
    # Start threads
    thread1.start()
    thread2.start()
    
    # Wait for threads to complete
    thread1.join()
    thread2.join()
    
    end_time = time.time()
    print(f"Total time with threading: {end_time - start_time:.2f} seconds")
    
    # Compare with sequential execution
    start_time = time.time()
    worker_function("Sequential-1", 2)
    worker_function("Sequential-2", 1)
    end_time = time.time()
    print(f"Total time sequential: {end_time - start_time:.2f} seconds")

# =============================================================================
# THREAD SYNCHRONIZATION
# =============================================================================

class Counter:
    """Thread-safe counter using locks."""
    
    def __init__(self):
        self.value = 0
        self.lock = threading.Lock()
    
    def increment(self):
        """Thread-safe increment."""
        with self.lock:
            current = self.value
            time.sleep(0.001)  # Simulate some work
            self.value = current + 1
    
    def get_value(self):
        """Get current value."""
        with self.lock:
            return self.value

def increment_worker(counter, iterations):
    """Worker that increments counter."""
    for _ in range(iterations):
        counter.increment()

def demonstrate_thread_synchronization():
    """Show thread synchronization with locks."""
    print("\n=== Thread Synchronization ===")
    
    # Without synchronization (unsafe)
    unsafe_counter = 0
    
    def unsafe_increment():
        nonlocal unsafe_counter
        for _ in range(1000):
            current = unsafe_counter
            time.sleep(0.0001)
            unsafe_counter = current + 1
    
    threads = []
    for _ in range(3):
        thread = threading.Thread(target=unsafe_increment)
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()
    
    print(f"Unsafe counter result: {unsafe_counter} (should be 3000)")
    
    # With synchronization (safe)
    safe_counter = Counter()
    
    threads = []
    for _ in range(3):
        thread = threading.Thread(target=increment_worker, args=(safe_counter, 1000))
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()
    
    print(f"Safe counter result: {safe_counter.get_value()} (should be 3000)")

# =============================================================================
# PRODUCER-CONSUMER PATTERN
# =============================================================================

def producer(queue, items):
    """Producer function that adds items to queue."""
    for item in items:
        print(f"Producing: {item}")
        queue.put(item)
        time.sleep(0.1)
    
    # Signal completion
    queue.put(None)

def consumer(queue, name):
    """Consumer function that processes items from queue."""
    while True:
        item = queue.get()
        if item is None:
            queue.task_done()
            break
        
        print(f"Consumer {name} processing: {item}")
        time.sleep(0.2)  # Simulate processing time
        queue.task_done()

def demonstrate_producer_consumer():
    """Show producer-consumer pattern with queues."""
    print("\n=== Producer-Consumer Pattern ===")
    
    # Create queue
    queue = Queue()
    
    # Create producer thread
    items = [f"Item-{i}" for i in range(5)]
    producer_thread = threading.Thread(target=producer, args=(queue, items))
    
    # Create consumer threads
    consumer_threads = []
    for i in range(2):
        thread = threading.Thread(target=consumer, args=(queue, f"C{i+1}"))
        consumer_threads.append(thread)
    
    # Start all threads
    producer_thread.start()
    for thread in consumer_threads:
        thread.start()
    
    # Wait for producer to finish
    producer_thread.join()
    
    # Wait for all items to be processed
    queue.join()
    
    # Stop consumers
    for _ in consumer_threads:
        queue.put(None)
    
    for thread in consumer_threads:
        thread.join()
    
    print("Producer-Consumer completed")

# =============================================================================
# THREAD POOL EXECUTOR
# =============================================================================

def cpu_bound_task(n):
    """CPU-intensive task for demonstration."""
    total = 0
    for i in range(n):
        total += i ** 2
    return total

def io_bound_task(url):
    """Simulate I/O-bound task."""
    time.sleep(1)  # Simulate network delay
    return f"Response from {url}"

def demonstrate_thread_pool():
    """Show ThreadPoolExecutor for concurrent execution."""
    print("\n=== Thread Pool Executor ===")
    
    # I/O-bound tasks with ThreadPoolExecutor
    urls = [f"http://example{i}.com" for i in range(5)]
    
    start_time = time.time()
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        # Submit tasks
        future_to_url = {executor.submit(io_bound_task, url): url for url in urls}
        
        # Collect results
        for future in concurrent.futures.as_completed(future_to_url):
            url = future_to_url[future]
            try:
                result = future.result()
                print(f"Completed: {result}")
            except Exception as e:
                print(f"Error with {url}: {e}")
    
    end_time = time.time()
    print(f"ThreadPool time: {end_time - start_time:.2f} seconds")

# =============================================================================
# MULTIPROCESSING BASICS
# =============================================================================

def cpu_intensive_work(n):
    """CPU-intensive function for multiprocessing."""
    result = sum(i * i for i in range(n))
    return result

def demonstrate_multiprocessing():
    """Show multiprocessing for CPU-bound tasks."""
    print("\n=== Multiprocessing ===")
    
    numbers = [1000000, 1000000, 1000000, 1000000]
    
    # Sequential execution
    start_time = time.time()
    sequential_results = [cpu_intensive_work(n) for n in numbers]
    sequential_time = time.time() - start_time
    
    # Multiprocessing execution
    start_time = time.time()
    with multiprocessing.Pool() as pool:
        parallel_results = pool.map(cpu_intensive_work, numbers)
    parallel_time = time.time() - start_time
    
    print(f"Sequential time: {sequential_time:.2f} seconds")
    print(f"Parallel time: {parallel_time:.2f} seconds")
    print(f"Speedup: {sequential_time / parallel_time:.2f}x")
    print(f"Results match: {sequential_results == parallel_results}")

# =============================================================================
# ASYNCIO BASICS
# =============================================================================

async def async_task(name, duration):
    """Asynchronous task."""
    print(f"Task {name} starting")
    await asyncio.sleep(duration)  # Non-blocking sleep
    print(f"Task {name} completed after {duration} seconds")
    return f"Result from {name}"

async def demonstrate_asyncio_basics():
    """Show basic asyncio concepts."""
    print("\n=== Asyncio Basics ===")
    
    # Run tasks concurrently
    start_time = time.time()
    
    tasks = [
        async_task("Alpha", 2),
        async_task("Beta", 1),
        async_task("Gamma", 1.5)
    ]
    
    results = await asyncio.gather(*tasks)
    
    end_time = time.time()
    print(f"Asyncio time: {end_time - start_time:.2f} seconds")
    print(f"Results: {results}")

# =============================================================================
# ASYNC HTTP REQUESTS
# =============================================================================

async def fetch_url(session, url):
    """Fetch URL asynchronously (simulated)."""
    print(f"Fetching: {url}")
    await asyncio.sleep(1)  # Simulate network request
    return f"Content from {url}"

async def demonstrate_async_http():
    """Show asynchronous HTTP requests pattern."""
    print("\n=== Async HTTP Requests ===")
    
    urls = [
        "http://example1.com",
        "http://example2.com", 
        "http://example3.com",
        "http://example4.com"
    ]
    
    start_time = time.time()
    
    # Create session (simulated)
    session = "mock_session"
    
    # Fetch all URLs concurrently
    tasks = [fetch_url(session, url) for url in urls]
    results = await asyncio.gather(*tasks)
    
    end_time = time.time()
    
    print(f"Fetched {len(results)} URLs in {end_time - start_time:.2f} seconds")
    for result in results:
        print(f"  {result}")

# =============================================================================
# ASYNC CONTEXT MANAGERS
# =============================================================================

class AsyncResource:
    """Async context manager example."""
    
    def __init__(self, name):
        self.name = name
    
    async def __aenter__(self):
        print(f"Acquiring async resource: {self.name}")
        await asyncio.sleep(0.1)  # Simulate async setup
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        print(f"Releasing async resource: {self.name}")
        await asyncio.sleep(0.1)  # Simulate async cleanup
    
    async def work(self):
        print(f"Working with {self.name}")
        await asyncio.sleep(0.5)

async def demonstrate_async_context_manager():
    """Show async context managers."""
    print("\n=== Async Context Managers ===")
    
    async with AsyncResource("Database") as db:
        await db.work()
    
    async with AsyncResource("Cache") as cache:
        await cache.work()

# =============================================================================
# ASYNC GENERATORS
# =============================================================================

async def async_number_generator(start, end, delay=0.1):
    """Async generator that yields numbers with delay."""
    for i in range(start, end):
        await asyncio.sleep(delay)
        yield i

async def demonstrate_async_generators():
    """Show async generators."""
    print("\n=== Async Generators ===")
    
    print("Async generator output:")
    async for number in async_number_generator(1, 6, 0.2):
        print(f"  Generated: {number}")

# =============================================================================
# CHOOSING THE RIGHT CONCURRENCY MODEL
# =============================================================================

def demonstrate_concurrency_comparison():
    """Compare different concurrency models."""
    print("\n=== Concurrency Model Comparison ===")
    
    print("When to use each model:")
    print("\n1. Threading:")
    print("   - I/O-bound tasks (file operations, network requests)")
    print("   - Tasks that spend time waiting")
    print("   - Limited by GIL for CPU-bound tasks")
    
    print("\n2. Multiprocessing:")
    print("   - CPU-bound tasks (calculations, data processing)")
    print("   - Tasks that can be parallelized")
    print("   - Bypasses GIL limitations")
    
    print("\n3. Asyncio:")
    print("   - I/O-bound tasks with many concurrent operations")
    print("   - Network programming (web servers, clients)")
    print("   - Single-threaded but highly concurrent")
    
    print("\n4. Guidelines:")
    print("   - CPU-bound + multicore → Multiprocessing")
    print("   - I/O-bound + limited concurrency → Threading")
    print("   - I/O-bound + high concurrency → Asyncio")

# =============================================================================
# PRACTICAL EXAMPLES
# =============================================================================

def download_file(url):
    """Simulate file download."""
    print(f"Downloading {url}")
    time.sleep(1)  # Simulate download time
    return f"Content from {url}"

def demonstrate_practical_threading():
    """Practical threading example: concurrent downloads."""
    print("\n=== Practical Example: Concurrent Downloads ===")
    
    urls = [
        "http://example.com/file1.txt",
        "http://example.com/file2.txt",
        "http://example.com/file3.txt",
        "http://example.com/file4.txt"
    ]
    
    # Sequential downloads
    start_time = time.time()
    sequential_results = [download_file(url) for url in urls]
    sequential_time = time.time() - start_time
    
    # Concurrent downloads using ThreadPoolExecutor
    start_time = time.time()
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        concurrent_results = list(executor.map(download_file, urls))
    concurrent_time = time.time() - start_time
    
    print(f"Sequential downloads: {sequential_time:.2f} seconds")
    print(f"Concurrent downloads: {concurrent_time:.2f} seconds")
    print(f"Speedup: {sequential_time / concurrent_time:.2f}x")

# =============================================================================
# MAIN EXECUTION
# =============================================================================

async def run_async_demos():
    """Run all async demonstrations."""
    await demonstrate_asyncio_basics()
    await demonstrate_async_http()
    await demonstrate_async_context_manager()
    await demonstrate_async_generators()

def main():
    """Run all demonstrations."""
    print("Python Concurrency Tutorial")
    print("=" * 50)
    
    demonstrate_basic_threading()
    demonstrate_thread_synchronization()
    demonstrate_producer_consumer()
    demonstrate_thread_pool()
    demonstrate_multiprocessing()
    demonstrate_practical_threading()
    demonstrate_concurrency_comparison()
    
    # Run async demonstrations
    print("\n" + "=" * 30)
    print("ASYNC DEMONSTRATIONS")
    print("=" * 30)
    asyncio.run(run_async_demos())
    
    print("\n" + "=" * 50)
    print("Concurrency tutorial completed!")

if __name__ == "__main__":
    main()