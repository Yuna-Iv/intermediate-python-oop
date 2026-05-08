import time
import functools

# Basic decoratoк
def my_decorator(func):
    @functools.wraps(func)  # preserves __name__, __doc__
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Done {func.__name__}")
        return result
    return wrapper

@my_decorator
def greet(name: str):
    print(f"Hello, {name}!")

greet("Alice")
print(greet.__name__)   # 'greet' thanks to functools.wraps

#Timer
def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        print(f"{func.__name__}: {time.perf_counter() - start:.6f}s")
        return result
    return wrapper

@timer
def slow_sum(n: int) -> int:
    return sum(range(n))

slow_sum(1_000_000)

#Decorator factory (with arguments)
def repeat(times: int):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = None
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(times=3)
def say_hi():
    print("Hi!")

say_hi()

#Manual memoization
def memoize(func):
    cache = {}
    @functools.wraps(func)
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    wrapper.cache = cache
    return wrapper

@memoize
def fib(n: int) -> int:
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

print(fib(40))

# Stacked decorators (order matters)
def bold(func):
    @functools.wraps(func)
    def wrapper(*a, **kw): return f"**{func(*a, **kw)}**"
    return wrapper

def italic(func):
    @functools.wraps(func)
    def wrapper(*a, **kw): return f"_{func(*a, **kw)}_"
    return wrapper

@bold    # applied second (outer)
@italic  # applied first (inner)
def text():
    return "Hello"

print(text())   # **_Hello_**

# property
class Circle:
    def __init__(self, radius: float):
        self._radius = radius

    @property
    def radius(self) -> float:
        return self._radius

    @radius.setter
    def radius(self, value: float):
        if value < 0:
            raise ValueError("Radius must be non-negative")
        self._radius = value

    @property
    def area(self) -> float:
        import math
        return math.pi * self._radius ** 2

c = Circle(5)
c.radius = 10
print(c.area)
