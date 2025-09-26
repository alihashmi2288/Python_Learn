"""
Python Metaclasses
==================

Created by: Syed Ali Hashmi
LinkedIn: https://www.linkedin.com/in/hashmiali2288

This module demonstrates metaclasses - classes that create classes.
Learn about class creation, __new__, __init__, and metaprogramming.
"""

# =============================================================================
# BASIC METACLASS CONCEPTS
# =============================================================================

def demonstrate_class_creation():
    """Show how classes are created in Python."""
    print("=== Class Creation Basics ===")
    
    # Classes are objects too
    class MyClass:
        def method(self):
            return "Hello from MyClass"
    
    print(f"MyClass type: {type(MyClass)}")
    print(f"MyClass is instance of type: {isinstance(MyClass, type)}")
    
    # Create class dynamically using type()
    def dynamic_method(self):
        return "Hello from DynamicClass"
    
    DynamicClass = type('DynamicClass', (), {'method': dynamic_method})
    
    # Both classes work the same way
    obj1 = MyClass()
    obj2 = DynamicClass()
    
    print(f"MyClass instance: {obj1.method()}")
    print(f"DynamicClass instance: {obj2.method()}")

# =============================================================================
# SIMPLE METACLASS
# =============================================================================

class SimpleMeta(type):
    """A simple metaclass that modifies class creation."""
    
    def __new__(mcs, name, bases, attrs):
        """Create a new class."""
        print(f"Creating class: {name}")
        
        # Modify class attributes
        attrs['class_id'] = f"ID_{name.upper()}"
        attrs['created_by'] = 'SimpleMeta'
        
        # Create the class
        return super().__new__(mcs, name, bases, attrs)
    
    def __init__(cls, name, bases, attrs):
        """Initialize the created class."""
        print(f"Initializing class: {name}")
        super().__init__(name, bases, attrs)

class MyMetaClass(metaclass=SimpleMeta):
    """Class using SimpleMeta metaclass."""
    
    def __init__(self, value):
        self.value = value
    
    def get_info(self):
        return f"Value: {self.value}, ID: {self.class_id}"

def demonstrate_simple_metaclass():
    """Show simple metaclass usage."""
    print("\n=== Simple Metaclass ===")
    
    # Create instance
    obj = MyMetaClass("test")
    print(f"Instance info: {obj.get_info()}")
    print(f"Created by: {obj.created_by}")

# =============================================================================
# ATTRIBUTE VALIDATION METACLASS
# =============================================================================

class ValidatedMeta(type):
    """Metaclass that adds attribute validation."""
    
    def __new__(mcs, name, bases, attrs):
        # Find validation rules
        validators = {}
        for key, value in list(attrs.items()):
            if key.startswith('validate_'):
                field_name = key[9:]  # Remove 'validate_' prefix
                validators[field_name] = value
                del attrs[key]  # Remove validator from class attributes
        
        # Store validators
        attrs['_validators'] = validators
        
        # Add validation method
        def __setattr__(self, name, value):
            if name in self._validators:
                self._validators[name](value)
            super(type(self), self).__setattr__(name, value)
        
        attrs['__setattr__'] = __setattr__
        
        return super().__new__(mcs, name, bases, attrs)

class Person(metaclass=ValidatedMeta):
    """Person class with automatic validation."""
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    @staticmethod
    def validate_name(value):
        if not isinstance(value, str) or len(value) < 2:
            raise ValueError("Name must be a string with at least 2 characters")
    
    @staticmethod
    def validate_age(value):
        if not isinstance(value, int) or value < 0 or value > 150:
            raise ValueError("Age must be an integer between 0 and 150")

def demonstrate_validation_metaclass():
    """Show validation metaclass."""
    print("\n=== Validation Metaclass ===")
    
    # Valid person
    person = Person("Alice", 30)
    print(f"Created person: {person.name}, {person.age}")
    
    # Try invalid values
    try:
        person.name = "A"  # Too short
    except ValueError as e:
        print(f"Validation error: {e}")
    
    try:
        person.age = -5  # Invalid age
    except ValueError as e:
        print(f"Validation error: {e}")

# =============================================================================
# SINGLETON METACLASS
# =============================================================================

class SingletonMeta(type):
    """Metaclass that implements singleton pattern."""
    
    _instances = {}
    
    def __call__(cls, *args, **kwargs):
        """Control instance creation."""
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class DatabaseConnection(metaclass=SingletonMeta):
    """Database connection using singleton pattern."""
    
    def __init__(self):
        self.connection_id = id(self)
        print(f"Creating database connection: {self.connection_id}")
    
    def query(self, sql):
        return f"Executing: {sql} on connection {self.connection_id}"

def demonstrate_singleton_metaclass():
    """Show singleton metaclass."""
    print("\n=== Singleton Metaclass ===")
    
    # Create multiple instances
    db1 = DatabaseConnection()
    db2 = DatabaseConnection()
    db3 = DatabaseConnection()
    
    print(f"db1 ID: {db1.connection_id}")
    print(f"db2 ID: {db2.connection_id}")
    print(f"db3 ID: {db3.connection_id}")
    print(f"All same instance: {db1 is db2 is db3}")

# =============================================================================
# ORM-STYLE METACLASS
# =============================================================================

class ORMMeta(type):
    """Metaclass for creating ORM-like classes."""
    
    def __new__(mcs, name, bases, attrs):
        # Skip for base Model class
        if name == 'Model':
            return super().__new__(mcs, name, bases, attrs)
        
        # Find field definitions
        fields = {}
        for key, value in list(attrs.items()):
            if isinstance(value, Field):
                fields[key] = value
                value.name = key
        
        # Store fields metadata
        attrs['_fields'] = fields
        attrs['_table_name'] = name.lower()
        
        # Add methods
        def __init__(self, **kwargs):
            for field_name, field in self._fields.items():
                value = kwargs.get(field_name, field.default)
                setattr(self, field_name, value)
        
        def save(self):
            field_values = []
            for field_name in self._fields:
                value = getattr(self, field_name)
                field_values.append(f"{field_name}={value}")
            return f"INSERT INTO {self._table_name} SET {', '.join(field_values)}"
        
        attrs['__init__'] = __init__
        attrs['save'] = save
        
        return super().__new__(mcs, name, bases, attrs)

class Field:
    """Field descriptor for ORM."""
    
    def __init__(self, field_type, default=None):
        self.field_type = field_type
        self.default = default
        self.name = None

class Model(metaclass=ORMMeta):
    """Base model class."""
    pass

class User(Model):
    """User model with fields."""
    
    id = Field(int, 0)
    name = Field(str, "")
    email = Field(str, "")
    age = Field(int, 18)

def demonstrate_orm_metaclass():
    """Show ORM-style metaclass."""
    print("\n=== ORM Metaclass ===")
    
    # Create user
    user = User(name="Alice", email="alice@example.com", age=30)
    
    print(f"User: {user.name}, {user.email}, {user.age}")
    print(f"Table name: {user._table_name}")
    print(f"Fields: {list(user._fields.keys())}")
    print(f"Save SQL: {user.save()}")

# =============================================================================
# REGISTRY METACLASS
# =============================================================================

class RegistryMeta(type):
    """Metaclass that maintains a registry of all classes."""
    
    registry = {}
    
    def __new__(mcs, name, bases, attrs):
        cls = super().__new__(mcs, name, bases, attrs)
        
        # Register the class
        mcs.registry[name] = cls
        
        return cls
    
    @classmethod
    def get_class(mcs, name):
        """Get class by name from registry."""
        return mcs.registry.get(name)
    
    @classmethod
    def list_classes(mcs):
        """List all registered classes."""
        return list(mcs.registry.keys())

class Animal(metaclass=RegistryMeta):
    """Base animal class."""
    
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    """Dog class."""
    
    def bark(self):
        return f"{self.name} says Woof!"

class Cat(Animal):
    """Cat class."""
    
    def meow(self):
        return f"{self.name} says Meow!"

def demonstrate_registry_metaclass():
    """Show registry metaclass."""
    print("\n=== Registry Metaclass ===")
    
    # List registered classes
    print(f"Registered classes: {RegistryMeta.list_classes()}")
    
    # Get class by name and create instance
    DogClass = RegistryMeta.get_class('Dog')
    if DogClass:
        dog = DogClass("Buddy")
        print(f"Created dog: {dog.bark()}")
    
    CatClass = RegistryMeta.get_class('Cat')
    if CatClass:
        cat = CatClass("Whiskers")
        print(f"Created cat: {cat.meow()}")

# =============================================================================
# PROPERTY INJECTION METACLASS
# =============================================================================

class PropertyMeta(type):
    """Metaclass that automatically creates properties."""
    
    def __new__(mcs, name, bases, attrs):
        # Find attributes that should become properties
        for key, value in list(attrs.items()):
            if key.startswith('_') and not key.startswith('__'):
                # Create property for private attribute
                prop_name = key[1:]  # Remove leading underscore
                
                def make_property(attr_name):
                    def getter(self):
                        return getattr(self, attr_name)
                    
                    def setter(self, value):
                        print(f"Setting {attr_name} to {value}")
                        setattr(self, attr_name, value)
                    
                    return property(getter, setter)
                
                if prop_name not in attrs:
                    attrs[prop_name] = make_property(key)
        
        return super().__new__(mcs, name, bases, attrs)

class Circle(metaclass=PropertyMeta):
    """Circle class with automatic properties."""
    
    def __init__(self, radius):
        self._radius = radius
    
    @property
    def area(self):
        return 3.14159 * self._radius ** 2

def demonstrate_property_metaclass():
    """Show property injection metaclass."""
    print("\n=== Property Metaclass ===")
    
    circle = Circle(5)
    print(f"Initial radius: {circle.radius}")
    print(f"Area: {circle.area}")
    
    # Setting radius will trigger the setter
    circle.radius = 10
    print(f"New area: {circle.area}")

# =============================================================================
# METACLASS WITH __CALL__
# =============================================================================

class CallableMeta(type):
    """Metaclass that makes classes callable in special ways."""
    
    def __call__(cls, *args, **kwargs):
        """Custom instance creation."""
        print(f"Creating instance of {cls.__name__} with args: {args}")
        
        # Create instance normally
        instance = super().__call__(*args, **kwargs)
        
        # Add some post-processing
        instance._created_at = "2024-01-01"
        
        return instance

class Product(metaclass=CallableMeta):
    """Product class with custom creation."""
    
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def __str__(self):
        return f"{self.name}: ${self.price} (created: {self._created_at})"

def demonstrate_callable_metaclass():
    """Show callable metaclass."""
    print("\n=== Callable Metaclass ===")
    
    product = Product("Laptop", 999.99)
    print(f"Product: {product}")

# =============================================================================
# ADVANCED METACLASS TECHNIQUES
# =============================================================================

class AdvancedMeta(type):
    """Advanced metaclass with multiple features."""
    
    def __new__(mcs, name, bases, attrs):
        # Add automatic string representation
        if '__str__' not in attrs:
            def __str__(self):
                class_name = self.__class__.__name__
                attr_strs = []
                for key, value in self.__dict__.items():
                    if not key.startswith('_'):
                        attr_strs.append(f"{key}={value}")
                return f"{class_name}({', '.join(attr_strs)})"
            
            attrs['__str__'] = __str__
        
        # Add method counting
        method_count = sum(1 for v in attrs.values() if callable(v))
        attrs['_method_count'] = method_count
        
        return super().__new__(mcs, name, bases, attrs)
    
    def __init__(cls, name, bases, attrs):
        super().__init__(name, bases, attrs)
        print(f"Class {name} created with {cls._method_count} methods")

class AdvancedClass(metaclass=AdvancedMeta):
    """Class using advanced metaclass."""
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def method1(self):
        pass
    
    def method2(self):
        pass

def demonstrate_advanced_metaclass():
    """Show advanced metaclass features."""
    print("\n=== Advanced Metaclass ===")
    
    obj = AdvancedClass(10, 20)
    print(f"Object: {obj}")  # Uses auto-generated __str__
    print(f"Method count: {obj._method_count}")

# =============================================================================
# MAIN EXECUTION
# =============================================================================

if __name__ == "__main__":
    """Run all demonstrations when script is executed directly."""
    print("Python Metaclasses Tutorial")
    print("=" * 50)
    
    demonstrate_class_creation()
    demonstrate_simple_metaclass()
    demonstrate_validation_metaclass()
    demonstrate_singleton_metaclass()
    demonstrate_orm_metaclass()
    demonstrate_registry_metaclass()
    demonstrate_property_metaclass()
    demonstrate_callable_metaclass()
    demonstrate_advanced_metaclass()
    
    print("\n" + "=" * 50)
    print("Metaclasses tutorial completed!")