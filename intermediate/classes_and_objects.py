"""
Python Classes and Objects (Object-Oriented Programming)
========================================================

This module demonstrates Python's object-oriented programming features.
Learn about classes, objects, inheritance, encapsulation, and polymorphism.
"""

# =============================================================================
# BASIC CLASS DEFINITION
# =============================================================================

class Person:
    """A simple Person class demonstrating basic OOP concepts."""
    
    # Class variable (shared by all instances)
    species = "Homo sapiens"
    
    def __init__(self, name, age):
        """Initialize a Person instance."""
        # Instance variables (unique to each instance)
        self.name = name
        self.age = age
    
    def introduce(self):
        """Method to introduce the person."""
        return f"Hi, I'm {self.name} and I'm {self.age} years old."
    
    def have_birthday(self):
        """Method to increment age."""
        self.age += 1
        return f"Happy birthday! {self.name} is now {self.age} years old."
    
    def __str__(self):
        """String representation of the object."""
        return f"Person(name='{self.name}', age={self.age})"
    
    def __repr__(self):
        """Developer-friendly representation."""
        return f"Person('{self.name}', {self.age})"

# =============================================================================
# CLASS WITH PROPERTIES AND METHODS
# =============================================================================

class BankAccount:
    """A BankAccount class demonstrating encapsulation and validation."""
    
    def __init__(self, account_number, initial_balance=0):
        """Initialize a bank account."""
        self.account_number = account_number
        self._balance = initial_balance  # Protected attribute
        self._transaction_history = []
    
    @property
    def balance(self):
        """Get the current balance (read-only property)."""
        return self._balance
    
    def deposit(self, amount):
        """Deposit money into the account."""
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        
        self._balance += amount
        self._transaction_history.append(f"Deposited ${amount:.2f}")
        return f"Deposited ${amount:.2f}. New balance: ${self._balance:.2f}"
    
    def withdraw(self, amount):
        """Withdraw money from the account."""
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        
        if amount > self._balance:
            raise ValueError("Insufficient funds")
        
        self._balance -= amount
        self._transaction_history.append(f"Withdrew ${amount:.2f}")
        return f"Withdrew ${amount:.2f}. New balance: ${self._balance:.2f}"
    
    def get_transaction_history(self):
        """Get a copy of transaction history."""
        return self._transaction_history.copy()
    
    def __str__(self):
        return f"Account {self.account_number}: ${self._balance:.2f}"

# =============================================================================
# INHERITANCE
# =============================================================================

class Animal:
    """Base class for all animals."""
    
    def __init__(self, name, species):
        self.name = name
        self.species = species
    
    def make_sound(self):
        """Base method for making sound."""
        return f"{self.name} makes a sound"
    
    def info(self):
        """Get animal information."""
        return f"{self.name} is a {self.species}"

class Dog(Animal):
    """Dog class inheriting from Animal."""
    
    def __init__(self, name, breed):
        # Call parent constructor
        super().__init__(name, "Dog")
        self.breed = breed
    
    def make_sound(self):
        """Override parent method."""
        return f"{self.name} barks: Woof!"
    
    def fetch(self):
        """Dog-specific method."""
        return f"{self.name} fetches the ball"
    
    def info(self):
        """Override parent method with additional info."""
        base_info = super().info()
        return f"{base_info} ({self.breed} breed)"

class Cat(Animal):
    """Cat class inheriting from Animal."""
    
    def __init__(self, name, indoor=True):
        super().__init__(name, "Cat")
        self.indoor = indoor
    
    def make_sound(self):
        """Override parent method."""
        return f"{self.name} meows: Meow!"
    
    def climb(self):
        """Cat-specific method."""
        return f"{self.name} climbs up high"

# =============================================================================
# MULTIPLE INHERITANCE
# =============================================================================

class Flyable:
    """Mixin class for flying ability."""
    
    def fly(self):
        return f"{self.name} is flying"

class Swimmable:
    """Mixin class for swimming ability."""
    
    def swim(self):
        return f"{self.name} is swimming"

class Duck(Animal, Flyable, Swimmable):
    """Duck class with multiple inheritance."""
    
    def __init__(self, name):
        super().__init__(name, "Duck")
    
    def make_sound(self):
        return f"{self.name} quacks: Quack!"

# =============================================================================
# CLASS METHODS AND STATIC METHODS
# =============================================================================

class MathUtils:
    """Utility class demonstrating class and static methods."""
    
    pi = 3.14159
    
    def __init__(self, precision=2):
        self.precision = precision
    
    @classmethod
    def create_high_precision(cls):
        """Class method to create high-precision instance."""
        return cls(precision=6)
    
    @staticmethod
    def add(a, b):
        """Static method for addition."""
        return a + b
    
    @staticmethod
    def circle_area(radius):
        """Static method to calculate circle area."""
        return MathUtils.pi * radius ** 2
    
    def format_number(self, number):
        """Instance method using precision."""
        return round(number, self.precision)

# =============================================================================
# PROPERTY DECORATORS
# =============================================================================

class Temperature:
    """Class demonstrating property decorators."""
    
    def __init__(self, celsius=0):
        self._celsius = celsius
    
    @property
    def celsius(self):
        """Get temperature in Celsius."""
        return self._celsius
    
    @celsius.setter
    def celsius(self, value):
        """Set temperature in Celsius with validation."""
        if value < -273.15:
            raise ValueError("Temperature cannot be below absolute zero")
        self._celsius = value
    
    @property
    def fahrenheit(self):
        """Get temperature in Fahrenheit."""
        return (self._celsius * 9/5) + 32
    
    @fahrenheit.setter
    def fahrenheit(self, value):
        """Set temperature using Fahrenheit."""
        self.celsius = (value - 32) * 5/9
    
    @property
    def kelvin(self):
        """Get temperature in Kelvin."""
        return self._celsius + 273.15
    
    def __str__(self):
        return f"{self._celsius}°C ({self.fahrenheit}°F, {self.kelvin}K)"

# =============================================================================
# SPECIAL METHODS (MAGIC METHODS)
# =============================================================================

class Vector:
    """Vector class demonstrating special methods."""
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        """String representation for users."""
        return f"Vector({self.x}, {self.y})"
    
    def __repr__(self):
        """String representation for developers."""
        return f"Vector({self.x}, {self.y})"
    
    def __add__(self, other):
        """Addition operator overloading."""
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        return NotImplemented
    
    def __sub__(self, other):
        """Subtraction operator overloading."""
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)
        return NotImplemented
    
    def __mul__(self, scalar):
        """Multiplication by scalar."""
        if isinstance(scalar, (int, float)):
            return Vector(self.x * scalar, self.y * scalar)
        return NotImplemented
    
    def __eq__(self, other):
        """Equality comparison."""
        if isinstance(other, Vector):
            return self.x == other.x and self.y == other.y
        return False
    
    def __len__(self):
        """Length of vector (magnitude)."""
        return int((self.x ** 2 + self.y ** 2) ** 0.5)
    
    def __getitem__(self, index):
        """Index access."""
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        else:
            raise IndexError("Vector index out of range")
    
    def __setitem__(self, index, value):
        """Index assignment."""
        if index == 0:
            self.x = value
        elif index == 1:
            self.y = value
        else:
            raise IndexError("Vector index out of range")

# =============================================================================
# ABSTRACT BASE CLASSES
# =============================================================================

from abc import ABC, abstractmethod

class Shape(ABC):
    """Abstract base class for shapes."""
    
    def __init__(self, name):
        self.name = name
    
    @abstractmethod
    def area(self):
        """Calculate area - must be implemented by subclasses."""
        pass
    
    @abstractmethod
    def perimeter(self):
        """Calculate perimeter - must be implemented by subclasses."""
        pass
    
    def describe(self):
        """Concrete method available to all subclasses."""
        return f"This is a {self.name}"

class Rectangle(Shape):
    """Rectangle implementation of Shape."""
    
    def __init__(self, width, height):
        super().__init__("Rectangle")
        self.width = width
        self.height = height
    
    def area(self):
        """Calculate rectangle area."""
        return self.width * self.height
    
    def perimeter(self):
        """Calculate rectangle perimeter."""
        return 2 * (self.width + self.height)
    
    def __str__(self):
        return f"Rectangle({self.width}x{self.height})"

class Circle(Shape):
    """Circle implementation of Shape."""
    
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius
    
    def area(self):
        """Calculate circle area."""
        return 3.14159 * self.radius ** 2
    
    def perimeter(self):
        """Calculate circle circumference."""
        return 2 * 3.14159 * self.radius
    
    def __str__(self):
        return f"Circle(radius={self.radius})"

# =============================================================================
# DEMONSTRATION FUNCTIONS
# =============================================================================

def demonstrate_basic_classes():
    """Demonstrate basic class usage."""
    print("=== Basic Classes ===")
    
    # Create instances
    person1 = Person("Alice", 30)
    person2 = Person("Bob", 25)
    
    print(f"Person 1: {person1}")
    print(f"Person 2: {person2}")
    print(f"Species: {Person.species}")
    
    # Call methods
    print(person1.introduce())
    print(person1.have_birthday())
    print(f"Updated: {person1}")

def demonstrate_encapsulation():
    """Demonstrate encapsulation with BankAccount."""
    print("\n=== Encapsulation ===")
    
    account = BankAccount("12345", 1000)
    print(f"Initial: {account}")
    print(f"Balance: ${account.balance}")
    
    # Perform transactions
    print(account.deposit(500))
    print(account.withdraw(200))
    
    # Show transaction history
    print("Transaction History:")
    for transaction in account.get_transaction_history():
        print(f"  - {transaction}")
    
    # Try invalid operations
    try:
        account.withdraw(2000)
    except ValueError as e:
        print(f"Error: {e}")

def demonstrate_inheritance():
    """Demonstrate inheritance and polymorphism."""
    print("\n=== Inheritance ===")
    
    # Create different animals
    animals = [
        Dog("Buddy", "Golden Retriever"),
        Cat("Whiskers", indoor=True),
        Duck("Donald")
    ]
    
    # Polymorphism in action
    for animal in animals:
        print(f"{animal.info()}")
        print(f"  {animal.make_sound()}")
        
        # Call specific methods if available
        if hasattr(animal, 'fetch'):
            print(f"  {animal.fetch()}")
        if hasattr(animal, 'climb'):
            print(f"  {animal.climb()}")
        if hasattr(animal, 'fly'):
            print(f"  {animal.fly()}")
        if hasattr(animal, 'swim'):
            print(f"  {animal.swim()}")
        print()

def demonstrate_class_methods():
    """Demonstrate class and static methods."""
    print("=== Class and Static Methods ===")
    
    # Static methods
    print(f"Add 5 + 3 = {MathUtils.add(5, 3)}")
    print(f"Circle area (r=5): {MathUtils.circle_area(5)}")
    
    # Instance methods
    math1 = MathUtils(precision=2)
    math2 = MathUtils.create_high_precision()
    
    number = 3.14159265
    print(f"Number with 2 decimals: {math1.format_number(number)}")
    print(f"Number with 6 decimals: {math2.format_number(number)}")

def demonstrate_properties():
    """Demonstrate property decorators."""
    print("\n=== Properties ===")
    
    temp = Temperature(25)
    print(f"Initial: {temp}")
    
    # Set using different units
    temp.fahrenheit = 86
    print(f"After setting to 86°F: {temp}")
    
    temp.celsius = 0
    print(f"After setting to 0°C: {temp}")
    
    # Try invalid temperature
    try:
        temp.celsius = -300
    except ValueError as e:
        print(f"Error: {e}")

def demonstrate_special_methods():
    """Demonstrate special methods (operator overloading)."""
    print("\n=== Special Methods ===")
    
    v1 = Vector(3, 4)
    v2 = Vector(1, 2)
    
    print(f"Vector 1: {v1}")
    print(f"Vector 2: {v2}")
    
    # Arithmetic operations
    v3 = v1 + v2
    print(f"v1 + v2 = {v3}")
    
    v4 = v1 - v2
    print(f"v1 - v2 = {v4}")
    
    v5 = v1 * 2
    print(f"v1 * 2 = {v5}")
    
    # Comparison
    print(f"v1 == v2: {v1 == v2}")
    print(f"v1 == Vector(3, 4): {v1 == Vector(3, 4)}")
    
    # Length and indexing
    print(f"Length of v1: {len(v1)}")
    print(f"v1[0] = {v1[0]}, v1[1] = {v1[1]}")
    
    v1[0] = 5
    print(f"After v1[0] = 5: {v1}")

def demonstrate_abstract_classes():
    """Demonstrate abstract base classes."""
    print("\n=== Abstract Classes ===")
    
    shapes = [
        Rectangle(5, 3),
        Circle(4)
    ]
    
    for shape in shapes:
        print(f"{shape}")
        print(f"  {shape.describe()}")
        print(f"  Area: {shape.area():.2f}")
        print(f"  Perimeter: {shape.perimeter():.2f}")
        print()
    
    # Try to create abstract class (will fail)
    try:
        # shape = Shape("Generic")  # This would raise TypeError
        pass
    except TypeError as e:
        print(f"Cannot instantiate abstract class: {e}")

# =============================================================================
# MAIN EXECUTION
# =============================================================================

if __name__ == "__main__":
    """Run all demonstrations when script is executed directly."""
    print("Python Classes and Objects Tutorial")
    print("=" * 50)
    
    demonstrate_basic_classes()
    demonstrate_encapsulation()
    demonstrate_inheritance()
    demonstrate_class_methods()
    demonstrate_properties()
    demonstrate_special_methods()
    demonstrate_abstract_classes()
    
    print("=" * 50)
    print("Classes and Objects tutorial completed!")