#!/usr/bin/env python3
"""
Benchmark: Sequential vs Threaded CPU-intensive math
"""

import time
from concurrent.futures import ThreadPoolExecutor

def heavy_computation(n):
    """CPU-intensive calculation."""
    result = 0
    for i in range(n):
        result += i ** 2 + i ** 0.5
    return result

ITERATIONS = 2_000_000
TASKS = 20

# Sequential execution
print("Sequential math computation...")
start = time.time()
sequential_results = [heavy_computation(ITERATIONS) for _ in range(TASKS)]
sequential_time = time.time() - start

print(f"Time: {sequential_time:.2f}s")
print(f"Completed {TASKS} tasks")

# Threaded execution
print("\nThreaded math computation...")
start = time.time()
with ThreadPoolExecutor(max_workers=10) as executor:
    threaded_results = list(executor.map(heavy_computation, [ITERATIONS] * TASKS))
threaded_time = time.time() - start

print(f"Time: {threaded_time:.2f}s")
print(f"Completed {TASKS} tasks")

# Results
print(f"\n{'='*40}")
if threaded_time < sequential_time:
    print(f"Speedup: {sequential_time / threaded_time:.2f}x")
else:
    print(f"Slowdown: {threaded_time / sequential_time:.2f}x")
    print("(Python GIL prevents parallel CPU work)")
print(f"{'='*40}")
