class Vector:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f"Vector({self.x}, {self.y})"

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar: float):
        return Vector(self.x * scalar, self.y * scalar)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Vector):
            return NotImplemented
        return self.x == other.x and self.y == other.y

    def __abs__(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def __bool__(self) -> bool:
        return self.x != 0 or self.y != 0

    def __len__(self) -> int:
        return 2

v1, v2 = Vector(1, 2), Vector(3, 4)
print(v1 + v2)              # (4, 6)
print(abs(v2))              # 5.0
print(bool(Vector(0, 0)))   # False

# context manager
class ManagedFile:
    def __init__(self, path: str, mode: str = "r"):
        self.path, self.mode = path, mode

    def __enter__(self):
        self.file = open(self.path, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
        return False    # do not suppress exceptions

with ManagedFile("test.txt", "w") as f:
    f.write("hello")

#Comparable objects with total_ordering
from functools import total_ordering

@total_ordering
class Temperature:
    def __init__(self, celsius: float):
        self.celsius = celsius

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Temperature):
            return NotImplemented
        return self.celsius == other.celsius

    def __lt__(self, other) -> bool:
        return self.celsius < other.celsius

    def __repr__(self) -> str:
        return f"Temperature({self.celsius}C)"

print(sorted([Temperature(30), Temperature(15), Temperature(22)]))
