#!/usr/bin/env python3
"""
Demonstrates threading performance for I/O-bound vs CPU-bound tasks.
"""

import time
import threading
from concurrent.futures import ThreadPoolExecutor
import urllib.request
import urllib.error

# URLs to download (using httpbin for reliable testing)
URLS = [
    "https://httpbin.org/delay/0.5",
    "https://httpbin.org/uuid",
    "https://httpbin.org/user-agent",
    "https://httpbin.org/headers",
    "https://httpbin.org/ip",
] * 4  # 20 URLs total

def download_url(url):
    """Download a single URL and return its length."""
    try:
        with urllib.request.urlopen(url, timeout=10) as response:
            data = response.read()
            return len(data)
    except urllib.error.URLError as e:
        print(f"Error downloading {url}: {e}")
        return 0

def download_sequential(urls):
    """Download URLs one at a time."""
    results = []
    for url in urls:
        results.append(download_url(url))
    return results

def download_threaded(urls):
    """Download URLs using a thread pool."""
    with ThreadPoolExecutor(max_workers=10) as executor:
        results = list(executor.map(download_url, urls))
    return results

def heavy_math(n):
    """CPU-intensive calculation."""
    total = 0
    for i in range(n):
        total += i ** 2
    return total

def math_sequential(iterations, count=20):
    """Run math calculations sequentially."""
    results = []
    for _ in range(count):
        results.append(heavy_math(iterations))
    return results

def math_threaded(iterations, count=20):
    """Run math calculations with threads."""
    with ThreadPoolExecutor(max_workers=10) as executor:
        results = list(executor.map(heavy_math, [iterations] * count))
    return results

def main():
    print("=" * 60)
    print("Threading Performance Demo")
    print("=" * 60)

    # I/O-bound task: downloading URLs
    print("\n📥 I/O-BOUND TASK: Downloading 20 URLs")
    print("-" * 60)

    print("Sequential downloads...")
    start = time.time()
    seq_results = download_sequential(URLS)
    seq_time = time.time() - start
    print(f"  Time: {seq_time:.2f}s")
    print(f"  Downloaded: {sum(seq_results)} bytes")

    print("\nThreaded downloads...")
    start = time.time()
    thread_results = download_threaded(URLS)
    thread_time = time.time() - start
    print(f"  Time: {thread_time:.2f}s")
    print(f"  Downloaded: {sum(thread_results)} bytes")

    speedup = seq_time / thread_time if thread_time > 0 else 0
    print(f"\n✨ Speedup: {speedup:.2f}x faster with threads")

    # CPU-bound task: heavy math
    print("\n" + "=" * 60)
    print("🧮 CPU-BOUND TASK: Heavy math (20 iterations)")
    print("-" * 60)

    iterations = 1_000_000

    print("Sequential math...")
    start = time.time()
    seq_math = math_sequential(iterations)
    seq_math_time = time.time() - start
    print(f"  Time: {seq_math_time:.2f}s")

    print("\nThreaded math...")
    start = time.time()
    thread_math = math_threaded(iterations)
    thread_math_time = time.time() - start
    print(f"  Time: {thread_math_time:.2f}s")

    if thread_math_time < seq_math_time:
        speedup = seq_math_time / thread_math_time
        print(f"\n✨ Speedup: {speedup:.2f}x faster with threads")
    else:
        slowdown = thread_math_time / seq_math_time
        print(f"\n⚠️  Slowdown: {slowdown:.2f}x SLOWER with threads")
        print("   (Expected: Python's GIL prevents true parallel CPU work)")

    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print("• I/O-bound tasks benefit from threading (waiting on network)")
    print("• CPU-bound tasks don't benefit (Python GIL limits parallelism)")
    print("• For CPU tasks, use multiprocessing instead of threading")
    print("=" * 60)

if __name__ == "__main__":
    main()
