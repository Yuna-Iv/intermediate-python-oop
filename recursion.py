import sys
from functools import lru_cache

#Factorial
def factorial(n: int) -> int:
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n <= 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))   # 120

#Fibonacci with memoization
@lru_cache(maxsize=None)
def fibonacci(n: int) -> int:
    if n in (1, 2):
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(50))  # fast — results are cached

# Flatten nested list
def flatten(data):
    result = []
    for item in data:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result

print(flatten([1, [2, [3, 4], 5], [6, 7], 8]))  # [1, 2, 3, 4, 5, 6, 7, 8]

# Binary search
def binary_search(arr: list, target: int, low: int = 0, high: int = None) -> int:
    if high is None:
        high = len(arr) - 1
    if low > high:
        return -1
    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search(arr, target, mid + 1, high)
    else:
        return binary_search(arr, target, low, mid - 1)

print(binary_search([1, 3, 5, 7, 9, 11], 7))   # 3
print(binary_search([1, 3, 5, 7, 9, 11], 6))   # -1

# Python's recursion limit (default 1000)
print(sys.getrecursionlimit())

# Iterative fallback so no RecursionError risk
def factorial_iterative(n: int) -> int:
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
