from abc import ABC, abstractmethod

class Serializable(ABC):
    @abstractmethod
    def to_dict(self) -> dict: ...

    def to_json(self) -> str:
        import json
        return json.dumps(self.to_dict())

class User(Serializable):
    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email

    def to_dict(self) -> dict:
        return {"name": self.name, "email": self.email}

print(User("Alice", "alice@example.com").to_json())

###
class DataProcessor(ABC):
    def process(self, data):
        return self.save(self.transform(self.load(data)))

    @abstractmethod
    def load(self, data): ...

    @abstractmethod
    def transform(self, data): ...

    def save(self, data):
        return data

class UpperCaseProcessor(DataProcessor):
    def load(self, data): return data.strip()
    def transform(self, data): return data.upper()

class ReverseProcessor(DataProcessor):
    def load(self, data): return list(data)
    def transform(self, data): return data[::-1]

print(UpperCaseProcessor().process("  hello  "))   # HELLO
print(ReverseProcessor().process([1, 2, 3]))       # [3, 2, 1]

#Interface-like ABCs
class Readable(ABC):
    @abstractmethod
    def read(self) -> str: ...

class Writable(ABC):
    @abstractmethod
    def write(self, data: str) -> None: ...

class ReadWriteStream(Readable, Writable):
    def __init__(self):
        self._buffer = ""

    def read(self) -> str:
        return self._buffer

    def write(self, data: str) -> None:
        self._buffer += data

stream = ReadWriteStream()
stream.write("Hello, ")
stream.write("World!")
print(stream.read())
