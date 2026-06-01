#!/usr/bin/env python3
"""
Benchmark: Sequential vs Threaded URL downloads
"""

import time
import urllib.request
from concurrent.futures import ThreadPoolExecutor

# 20 URLs to download
URLS = [
    "https://httpbin.org/delay/0.3",
    "https://httpbin.org/uuid",
    "https://httpbin.org/user-agent",
    "https://httpbin.org/headers",
    "https://httpbin.org/ip",
    "https://httpbin.org/get",
    "https://httpbin.org/base64/SFRUUEJJTiBpcyBhd2Vzb21l",
    "https://httpbin.org/json",
    "https://httpbin.org/html",
    "https://httpbin.org/robots.txt",
    "https://httpbin.org/deny",
    "https://httpbin.org/cache",
    "https://httpbin.org/etag/test",
    "https://httpbin.org/bytes/1024",
    "https://httpbin.org/stream-bytes/512",
    "https://httpbin.org/links/5",
    "https://httpbin.org/image/png",
    "https://httpbin.org/xml",
    "https://httpbin.org/encoding/utf8",
    "https://httpbin.org/gzip",
]

def fetch(url):
    """Download a URL and return byte count."""
    try:
        with urllib.request.urlopen(url, timeout=10) as resp:
            return len(resp.read())
    except Exception as e:
        print(f"Error: {e}")
        return 0

# Sequential downloads
print("Sequential downloads...")
start = time.time()
sequential_results = [fetch(url) for url in URLS]
sequential_time = time.time() - start

print(f"Time: {sequential_time:.2f}s")
print(f"Total bytes: {sum(sequential_results)}")

# Threaded downloads
print("\nThreaded downloads...")
start = time.time()
with ThreadPoolExecutor(max_workers=10) as executor:
    threaded_results = list(executor.map(fetch, URLS))
threaded_time = time.time() - start

print(f"Time: {threaded_time:.2f}s")
print(f"Total bytes: {sum(threaded_results)}")

# Results
print(f"\n{'='*40}")
print(f"Speedup: {sequential_time / threaded_time:.2f}x")
print(f"{'='*40}")
