# Classes and Objects in Python

## Overview
Object-Oriented Programming (OOP) is a programming paradigm that organizes code into classes and objects. Python supports OOP with classes, inheritance, encapsulation, and polymorphism.

## Basic Class Syntax

```python
class ClassName:
    """Class docstring"""
    
    # Class variable (shared by all instances)
    class_variable = "shared"
    
    def __init__(self, parameter):
        """Constructor method"""
        self.instance_variable = parameter
    
    def method(self):
        """Instance method"""
        return f"Hello from {self.instance_variable}"
```

## Core OOP Concepts

### 1. Encapsulation
Bundling data and methods that operate on that data within a single unit (class).

```python
class BankAccount:
    def __init__(self, balance=0):
        self._balance = balance  # Protected attribute
    
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
    
    def get_balance(self):
        return self._balance
```

### 2. Inheritance
Creating new classes based on existing classes.

```python
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        pass

class Dog(Animal):  # Dog inherits from Animal
    def speak(self):
        return f"{self.name} says Woof!"

class Cat(Animal):  # Cat inherits from Animal
    def speak(self):
        return f"{self.name} says Meow!"
```

### 3. Polymorphism
Using a single interface to represent different types.

```python
def make_animal_speak(animal):
    return animal.speak()  # Works with any Animal subclass

dog = Dog("Buddy")
cat = Cat("Whiskers")

print(make_animal_speak(dog))  # "Buddy says Woof!"
print(make_animal_speak(cat))  # "Whiskers says Meow!"
```

## Instance vs Class Variables

```python
class Counter:
    # Class variable (shared by all instances)
    total_instances = 0
    
    def __init__(self, start_value=0):
        # Instance variable (unique to each instance)
        self.value = start_value
        Counter.total_instances += 1
    
    def increment(self):
        self.value += 1

# Usage
c1 = Counter(10)
c2 = Counter(20)
print(Counter.total_instances)  # 2
print(c1.value, c2.value)      # 10 20
```

## Methods Types

### Instance Methods
```python
class Person:
    def __init__(self, name):
        self.name = name
    
    def greet(self):  # Instance method
        return f"Hello, I'm {self.name}"
```

### Class Methods
```python
class Person:
    species = "Homo sapiens"
    
    @classmethod
    def get_species(cls):  # Class method
        return cls.species
    
    @classmethod
    def create_anonymous(cls):  # Alternative constructor
        return cls("Anonymous")
```

### Static Methods
```python
class MathUtils:
    @staticmethod
    def add(a, b):  # Static method
        return a + b
    
    @staticmethod
    def is_even(number):
        return number % 2 == 0
```

## Properties and Descriptors

### Property Decorator
```python
class Circle:
    def __init__(self, radius):
        self._radius = radius
    
    @property
    def radius(self):
        """Getter for radius"""
        return self._radius
    
    @radius.setter
    def radius(self, value):
        """Setter for radius with validation"""
        if value < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = value
    
    @property
    def area(self):
        """Read-only property"""
        return 3.14159 * self._radius ** 2
```

## Special Methods (Magic Methods)

### String Representation
```python
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    
    def __str__(self):
        """User-friendly string representation"""
        return f"{self.title} by {self.author}"
    
    def __repr__(self):
        """Developer-friendly representation"""
        return f"Book('{self.title}', '{self.author}')"
```

### Arithmetic Operations
```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
```

### Container Methods
```python
class Playlist:
    def __init__(self):
        self.songs = []
    
    def __len__(self):
        return len(self.songs)
    
    def __getitem__(self, index):
        return self.songs[index]
    
    def __setitem__(self, index, value):
        self.songs[index] = value
    
    def __contains__(self, song):
        return song in self.songs
```

## Inheritance Patterns

### Single Inheritance
```python
class Vehicle:
    def __init__(self, brand):
        self.brand = brand
    
    def start(self):
        return f"{self.brand} vehicle started"

class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)  # Call parent constructor
        self.model = model
    
    def start(self):
        return f"{self.brand} {self.model} car started"
```

### Multiple Inheritance
```python
class Flyable:
    def fly(self):
        return "Flying through the air"

class Swimmable:
    def swim(self):
        return "Swimming in water"

class Duck(Animal, Flyable, Swimmable):
    def __init__(self, name):
        super().__init__(name)
    
    def speak(self):
        return f"{self.name} says Quack!"
```

### Method Resolution Order (MRO)
```python
class A:
    def method(self):
        return "A"

class B(A):
    def method(self):
        return "B"

class C(A):
    def method(self):
        return "C"

class D(B, C):
    pass

# Check MRO
print(D.__mro__)  # Shows the order: D -> B -> C -> A -> object
```

## Abstract Base Classes

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass
    
    def description(self):  # Concrete method
        return f"This is a {self.__class__.__name__}"

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)
```

## Access Control

### Naming Conventions
```python
class MyClass:
    def __init__(self):
        self.public = "Everyone can access"
        self._protected = "Intended for internal use"
        self.__private = "Name mangled to _MyClass__private"
    
    def _internal_method(self):
        """Protected method"""
        pass
    
    def __private_method(self):
        """Private method (name mangled)"""
        pass
```

## Class Decorators

```python
def add_debug_info(cls):
    """Class decorator to add debugging information"""
    original_init = cls.__init__
    
    def new_init(self, *args, **kwargs):
        print(f"Creating instance of {cls.__name__}")
        original_init(self, *args, **kwargs)
    
    cls.__init__ = new_init
    return cls

@add_debug_info
class Person:
    def __init__(self, name):
        self.name = name
```

## Composition vs Inheritance

### Inheritance (is-a relationship)
```python
class Animal:
    def breathe(self):
        return "Breathing"

class Dog(Animal):  # Dog IS-A Animal
    def bark(self):
        return "Woof!"
```

### Composition (has-a relationship)
```python
class Engine:
    def start(self):
        return "Engine started"

class Car:
    def __init__(self):
        self.engine = Engine()  # Car HAS-A Engine
    
    def start(self):
        return self.engine.start()
```

## Design Patterns

### Singleton Pattern
```python
class Singleton:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
```

### Factory Pattern
```python
class AnimalFactory:
    @staticmethod
    def create_animal(animal_type, name):
        if animal_type == "dog":
            return Dog(name)
        elif animal_type == "cat":
            return Cat(name)
        else:
            raise ValueError(f"Unknown animal type: {animal_type}")
```

## Best Practices

### 1. Use Clear, Descriptive Names
```python
# Good
class BankAccount:
    def calculate_interest(self):
        pass

# Avoid
class BA:
    def calc_int(self):
        pass
```

### 2. Keep Classes Focused (Single Responsibility)
```python
# Good - focused responsibility
class EmailValidator:
    def is_valid_email(self, email):
        return "@" in email and "." in email

class EmailSender:
    def send_email(self, email, message):
        pass

# Avoid - too many responsibilities
class EmailManager:
    def is_valid_email(self, email):
        pass
    
    def send_email(self, email, message):
        pass
    
    def log_email(self, email):
        pass
    
    def format_email(self, email):
        pass
```

### 3. Use Properties for Computed Values
```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    @property
    def area(self):  # Computed property
        return self.width * self.height
```

### 4. Prefer Composition Over Inheritance
```python
# Good - composition
class Car:
    def __init__(self):
        self.engine = Engine()
        self.wheels = [Wheel() for _ in range(4)]

# Sometimes inheritance is appropriate
class SportsCar(Car):  # Clear is-a relationship
    def __init__(self):
        super().__init__()
        self.turbo = True
```

## Common Pitfalls

### 1. Mutable Default Arguments
```python
# Wrong
class ShoppingCart:
    def __init__(self, items=[]):  # Dangerous!
        self.items = items

# Correct
class ShoppingCart:
    def __init__(self, items=None):
        self.items = items if items is not None else []
```

### 2. Not Using super() in Inheritance
```python
# Wrong
class Child(Parent):
    def __init__(self, name, age):
        Parent.__init__(self, name)  # Fragile
        self.age = age

# Correct
class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)  # Flexible
        self.age = age
```

### 3. Overusing Inheritance
```python
# Often better to use composition
class FileLogger:
    def __init__(self, filename):
        self.file = open(filename, 'a')  # Composition
    
    def log(self, message):
        self.file.write(f"{message}\n")
```