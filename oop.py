from abc import ABC, abstractmethod

class Animal:
    species_count = 0   # class-level attribute

    def __init__(self, name: str, age: int):
        self._name = name    # protected (convention)
        self.__age = age     # private (name mangling)
        Animal.species_count += 1

    @property
    def name(self) -> str:
        return self._name

    @property
    def age(self) -> int:
        return self.__age

    @age.setter
    def age(self, value: int):
        if value < 0:
            raise ValueError("Age cannot be negative")
        self.__age = value

    def speak(self) -> str:
        raise NotImplementedError

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self._name!r}, age={self.__age})"

    def __str__(self) -> str:
        return f"{self._name} ({self.__class__.__name__})"

    @classmethod
    def total_count(cls) -> int:
        return cls.species_count

    @staticmethod
    def is_valid_name(name: str) -> bool:
        return name.isalpha()

###
class Dog(Animal):
    def __init__(self, name: str, age: int, breed: str):
        super().__init__(name, age)
        self.breed = breed

    def speak(self) -> str:
        return f"{self._name} says: Woof!"

    def fetch(self, item: str) -> str:
        return f"{self._name} fetched {item}"

class Cat(Animal):
    def __init__(self, name: str, age: int, indoor: bool = True):
        super().__init__(name, age)
        self.indoor = indoor

    def speak(self) -> str:
        return f"{self._name} says: Meow!"

# Polymorphism
animals: list[Animal] = [Dog("Rex", 3, "Labrador"), Cat("Luna", 5)]
for a in animals:
    print(a.speak())

#MRO
class Flyable:
    def fly(self) -> str: return "I can fly!"

class Swimmable:
    def swim(self) -> str: return "I can swim!"

class Duck(Animal, Flyable, Swimmable):
    def speak(self) -> str: return f"{self._name} says: Quack!"

donald = Duck("Donald", 2)
print(donald.fly(), donald.swim())
print(Duck.__mro__)     # Method Resolution Order

#ABC
class Shape(ABC):
    @abstractmethod
    def area(self) -> float: ...

    @abstractmethod
    def perimeter(self) -> float: ...

    def describe(self) -> str:
        return f"{self.__class__.__name__}: area={self.area():.2f}, perimeter={self.perimeter():.2f}"

class Rectangle(Shape):
    def __init__(self, w: float, h: float):
        self.w, self.h = w, h
    def area(self) -> float: return self.w * self.h
    def perimeter(self) -> float: return 2 * (self.w + self.h)

class Circle(Shape):
    import math
    def __init__(self, r: float): self.r = r
    def area(self) -> float:
        import math; return math.pi * self.r ** 2
    def perimeter(self) -> float:
        import math; return 2 * math.pi * self.r

for shape in [Rectangle(4, 5), Circle(3)]:
    print(shape.describe())
