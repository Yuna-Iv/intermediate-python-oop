import sys
import itertools

# custom iterator
class CountUp:
    def __init__(self, start: int, end: int):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.end:
            raise StopIteration
        value = self.current
        self.current += 1
        return value

for n in CountUp(1, 5):
    print(n, end=" ")   # 1 2 3 4 5
print()

# inf generator
def infinite_counter(start: int = 0):
    n = start
    while True:
        yield n
        n += 1

gen = infinite_counter(5)
for _ in range(5):
    print(next(gen), end=" ")   # 5 6 7 8 9
print()

#Fibonacci generator
def fibonacci_gen():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib = fibonacci_gen()
print([next(fib) for _ in range(10)])   # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

# --- File reader (memory-efficient) ---
def read_large_file(filepath: str):
    with open(filepath, encoding="utf-8") as f:
        for line in f:
            yield line.strip()

#Generator expression vs list comprehension
sq_gen  = (x ** 2 for x in range(1_000_000))   # lazy
sq_list = [x ** 2 for x in range(1_000_000)]   # all in memory

print(f"List:      {sys.getsizeof(sq_list):,} bytes")
print(f"Generator: {sys.getsizeof(sq_gen):,} bytes")

#Two-way communication with send()
def accumulator():
    total = 0
    while True:
        value = yield total
        if value is None:
            break
        total += value

acc = accumulator()
next(acc)           # prime the generator
print(acc.send(10)) # 10
print(acc.send(20)) # 30
print(acc.send(5))  # 35

gen = infinite_counter()
print(list(itertools.islice(gen, 5)))                           # [0, 1, 2, 3, 4]
print(list(itertools.chain([1, 2], [3, 4], [5])))              # [1, 2, 3, 4, 5]
print(list(itertools.takewhile(lambda x: x < 5, infinite_counter())))  # [0..4]
