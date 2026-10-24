- What is an Interface?
    - An interface is a `blueprint of a class.`
    - It is a `contract between the interface and the class.`
    - It is a `set of methods that the class must implement.`
    - It is a `way to achieve abstraction.`
    

# 1. Interfaces in python

- Python `does not have a dedicated interface keyword` like Java, C#, or Go.
- Instead, Python relies on `its dynamic nature and specific standard library tools to implement the interface pattern.`
- You can implement interfaces in Python using three main approaches:

    1. `Duck Typing` (informal)
    2. `Abstract Base Classes` (nominal/runtime)
    3. `Protocols` (structural/static)

## 1. Duck Typing (Informal Interfaces)
- Python's native philosophy is based on the idea: "If it walks like a duck and quacks like a duck, it's a duck."
- You do not need to explicitly declare that a class implements an interface; you just need to make sure the class has the required methods. [1, 4] 
```python
class PDFReader:
    def extract_text(self) -> str:
        return "Text from PDF"
class EmailReader:
    def extract_text(self) -> str:
        return "Text from Email"
# This function accepts any object as long as it has an `extract_text` methoddef print_content(reader):
    print(reader.extract_text())

print_content(PDFReader())   # Works
print_content(EmailReader()) # Works
```

* Pros: Extremely flexible, zero boilerplate code.
* Cons: Errors only happen at runtime if a method is missing or misspelled. [1, 4] 

------------------------------
## 2. Abstract Base Classes (ABCs)
- If you want strict enforcement at runtime, you can use the built-in abc module.
- By inheriting from ABC and using the @abstractmethod decorator, you create a formal contract.
- Any subclass must implement these methods, or Python will raise a TypeError when you try to instantiate it. [1, 5] 

```python
from abc import ABC, abstractmethod
class FileReader(ABC):
    @abstractmethod
    def extract_text(self) -> str:
        pass
class PDFReader(FileReader):
    def extract_text(self) -> str:
        return "Text from PDF"
# This will fail at runtime because it didn't implement `extract_text`:class FaultyReader(FileReader):
    pass
# reader = FaultyReader() # Raises TypeError: Can't instantiate abstract class...
```

* Pros: Fails early at instantiation time if a class is missing required methods.
* Cons: Requires explicit inheritance, forcing tight coupling between your classes. [1, 6] 

------------------------------
## 3. Protocols (Structural Subtyping)
- Introduced via [PEP 544](https://peps.python.org/pep-0544/), typing.Protocol gives you the best of both worlds.
- It acts like an interface for static type checkers (like Mypy or your IDE) without requiring explicit inheritance. [1, 6, 7] 

```python
from typing import Protocol
class Reader(Protocol):
    def extract_text(self) -> str:
        ...
# No explicit inheritance needed!class PDFReader: 
    def extract_text(self) -> str:
        return "Text from PDF"
# Your IDE or Mypy can statically check if `reader` adheres to the `Reader` protocoldef print_content(reader: Reader):
    print(reader.extract_text())

print_content(PDFReader()) # Passes type checking perfectly
```

* Pros: Combines the flexibility of duck typing with the safety of static type checking.
* Cons: Does not block object creation at runtime by default (unless paired with @runtime_checkable). [1] 

------------------------------
## Summary: Which should you use?

| Method | Enforced At | Requires Inheritance? | Best For |
|---|---|---|---|
| Duck Typing | Runtime (when called) | No | Small scripts, rapid prototyping |
| Abstract Base Classes (ABCs) | Runtime (on instantiation) | Yes | Strict framework architectures, plug-in designs |
| Protocols | Static analysis (IDE / Mypy) | No | Modern Python codebases prioritizing type hints |

On community platforms like [Reddit](https://www.reddit.com/r/Python/comments/1lvrkpg/using_oop_interfaces_in_python/), users generally agree that modern Python design favors Protocols when you want clean structural contracts without messy inheritance hierarchies, falling back to ABCs if runtime enforcement is strictly mandatory. [6] 
If you are working on a specific use case, tell me:
