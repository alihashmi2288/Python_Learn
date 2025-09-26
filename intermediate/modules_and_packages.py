"""
Python Modules and Packages
============================

This module demonstrates Python's module system for organizing and reusing code.
Learn about imports, creating modules, packages, and distribution.
"""

import os
import sys
import math
from datetime import datetime, timedelta
from collections import Counter, defaultdict
import json

# =============================================================================
# BASIC IMPORTS
# =============================================================================

def demonstrate_basic_imports():
    """Show different ways to import modules."""
    print("=== Basic Imports ===")
    
    # Standard library imports
    import random
    import string
    
    # Generate random data
    random_number = random.randint(1, 100)
    random_string = ''.join(random.choices(string.ascii_letters, k=5))
    
    print(f"Random number: {random_number}")
    print(f"Random string: {random_string}")
    
    # From imports
    from math import pi, sqrt, factorial
    
    print(f"Pi: {pi}")
    print(f"Square root of 16: {sqrt(16)}")
    print(f"Factorial of 5: {factorial(5)}")
    
    # Import with alias
    import datetime as dt
    
    now = dt.datetime.now()
    print(f"Current time: {now}")

# =============================================================================
# CREATING A SIMPLE MODULE
# =============================================================================

def create_sample_module():
    """Create a sample module file."""
    print("\n=== Creating Sample Module ===")
    
    module_content = '''"""
Sample utility module for demonstration.
"""

def greet(name):
    """Greet a person."""
    return f"Hello, {name}!"

def calculate_area(length, width):
    """Calculate rectangle area."""
    return length * width

class Calculator:
    """Simple calculator class."""
    
    @staticmethod
    def add(a, b):
        return a + b
    
    @staticmethod
    def multiply(a, b):
        return a * b

# Module-level variable
VERSION = "1.0.0"

# Code that runs when module is imported
print(f"Sample module loaded, version {VERSION}")
'''
    
    # Write the module file
    with open("sample_module.py", "w") as f:
        f.write(module_content)
    
    print("✓ Created sample_module.py")
    
    # Import and use the module
    import sample_module
    
    print(f"Module version: {sample_module.VERSION}")
    print(sample_module.greet("Alice"))
    
    calc = sample_module.Calculator()
    print(f"5 + 3 = {calc.add(5, 3)}")
    
    # Clean up
    os.remove("sample_module.py")
    if "sample_module" in sys.modules:
        del sys.modules["sample_module"]

# =============================================================================
# MODULE SEARCH PATH
# =============================================================================

def demonstrate_module_path():
    """Show how Python finds modules."""
    print("\n=== Module Search Path ===")
    
    print("Python searches for modules in this order:")
    for i, path in enumerate(sys.path, 1):
        print(f"  {i}. {path}")
    
    # Add custom path
    custom_path = os.path.join(os.getcwd(), "custom_modules")
    if custom_path not in sys.path:
        sys.path.insert(0, custom_path)
        print(f"\n✓ Added custom path: {custom_path}")

# =============================================================================
# CREATING PACKAGES
# =============================================================================

def create_sample_package():
    """Create a sample package structure."""
    print("\n=== Creating Sample Package ===")
    
    # Create package directory
    package_dir = "mypackage"
    os.makedirs(package_dir, exist_ok=True)
    
    # Create __init__.py
    init_content = '''"""
My sample package for demonstration.
"""

from .math_utils import add, multiply
from .string_utils import reverse_string, capitalize_words

__version__ = "1.0.0"
__all__ = ["add", "multiply", "reverse_string", "capitalize_words"]

print(f"MyPackage v{__version__} loaded")
'''
    
    with open(f"{package_dir}/__init__.py", "w") as f:
        f.write(init_content)
    
    # Create math_utils.py
    math_utils_content = '''"""
Mathematical utility functions.
"""

def add(a, b):
    """Add two numbers."""
    return a + b

def multiply(a, b):
    """Multiply two numbers."""
    return a * b

def power(base, exponent):
    """Calculate power."""
    return base ** exponent
'''
    
    with open(f"{package_dir}/math_utils.py", "w") as f:
        f.write(math_utils_content)
    
    # Create string_utils.py
    string_utils_content = '''"""
String utility functions.
"""

def reverse_string(text):
    """Reverse a string."""
    return text[::-1]

def capitalize_words(text):
    """Capitalize each word."""
    return ' '.join(word.capitalize() for word in text.split())

def count_vowels(text):
    """Count vowels in text."""
    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char in vowels)
'''
    
    with open(f"{package_dir}/string_utils.py", "w") as f:
        f.write(string_utils_content)
    
    print("✓ Created package structure:")
    print(f"  {package_dir}/")
    print(f"    __init__.py")
    print(f"    math_utils.py")
    print(f"    string_utils.py")
    
    # Import and use the package
    sys.path.insert(0, os.getcwd())
    
    try:
        import mypackage
        
        print(f"\nUsing package:")
        print(f"  Add: {mypackage.add(5, 3)}")
        print(f"  Multiply: {mypackage.multiply(4, 7)}")
        print(f"  Reverse: {mypackage.reverse_string('hello')}")
        print(f"  Capitalize: {mypackage.capitalize_words('hello world')}")
        
        # Import specific submodule
        from mypackage import string_utils
        print(f"  Vowel count: {string_utils.count_vowels('hello world')}")
        
    except ImportError as e:
        print(f"Import error: {e}")
    
    # Clean up
    import shutil
    shutil.rmtree(package_dir)
    
    # Remove from sys.modules
    modules_to_remove = [name for name in sys.modules if name.startswith('mypackage')]
    for module in modules_to_remove:
        del sys.modules[module]

# =============================================================================
# STANDARD LIBRARY MODULES
# =============================================================================

def demonstrate_standard_library():
    """Show useful standard library modules."""
    print("\n=== Standard Library Modules ===")
    
    # os module
    print("OS Module:")
    print(f"  Current directory: {os.getcwd()}")
    print(f"  Platform: {os.name}")
    print(f"  Environment PATH: {len(os.environ.get('PATH', '').split(os.pathsep))} entries")
    
    # sys module
    print(f"\nSys Module:")
    print(f"  Python version: {sys.version}")
    print(f"  Platform: {sys.platform}")
    print(f"  Module search paths: {len(sys.path)} paths")
    
    # datetime module
    print(f"\nDateTime Module:")
    now = datetime.now()
    tomorrow = now + timedelta(days=1)
    print(f"  Now: {now.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"  Tomorrow: {tomorrow.strftime('%Y-%m-%d %H:%M:%S')}")
    
    # collections module
    print(f"\nCollections Module:")
    
    # Counter
    text = "hello world"
    char_count = Counter(text)
    print(f"  Character count in '{text}': {dict(char_count.most_common(3))}")
    
    # defaultdict
    word_groups = defaultdict(list)
    words = ["apple", "banana", "apricot", "blueberry", "cherry"]
    for word in words:
        word_groups[word[0]].append(word)
    
    print(f"  Words grouped by first letter: {dict(word_groups)}")
    
    # json module
    print(f"\nJSON Module:")
    data = {"name": "Alice", "age": 30, "skills": ["Python", "JavaScript"]}
    json_string = json.dumps(data)
    parsed_data = json.loads(json_string)
    print(f"  JSON serialization: {json_string}")
    print(f"  Parsed back: {parsed_data}")

# =============================================================================
# THIRD-PARTY PACKAGES
# =============================================================================

def demonstrate_third_party_packages():
    """Show how to work with third-party packages."""
    print("\n=== Third-Party Packages ===")
    
    # Simulate package installation info
    print("Popular third-party packages:")
    
    packages = [
        ("requests", "HTTP library for humans"),
        ("numpy", "Numerical computing"),
        ("pandas", "Data analysis and manipulation"),
        ("matplotlib", "Plotting library"),
        ("flask", "Lightweight web framework"),
        ("django", "Full-featured web framework"),
        ("pytest", "Testing framework"),
        ("pillow", "Image processing"),
    ]
    
    for package, description in packages:
        print(f"  {package}: {description}")
        print(f"    Install: pip install {package}")
    
    print("\nPackage management commands:")
    print("  pip list                 # List installed packages")
    print("  pip show package_name    # Show package info")
    print("  pip freeze > requirements.txt  # Save dependencies")
    print("  pip install -r requirements.txt  # Install from file")

# =============================================================================
# MODULE ATTRIBUTES AND INTROSPECTION
# =============================================================================

def demonstrate_module_introspection():
    """Show how to inspect modules."""
    print("\n=== Module Introspection ===")
    
    # Inspect math module
    print("Math module attributes:")
    math_attrs = [attr for attr in dir(math) if not attr.startswith('_')]
    print(f"  Public attributes: {len(math_attrs)}")
    print(f"  Sample functions: {math_attrs[:5]}")
    
    # Module information
    print(f"\nModule information:")
    print(f"  Math module file: {math.__file__ if hasattr(math, '__file__') else 'Built-in'}")
    print(f"  Math module name: {math.__name__}")
    
    # Function inspection
    import inspect
    
    print(f"\nFunction inspection (math.pow):")
    signature = inspect.signature(math.pow)
    print(f"  Signature: {signature}")
    print(f"  Docstring: {math.pow.__doc__}")
    
    # Get all functions in a module
    math_functions = [name for name, obj in inspect.getmembers(math, inspect.isfunction)]
    print(f"  Functions in math: {len(math_functions)}")

# =============================================================================
# RELATIVE IMPORTS
# =============================================================================

def demonstrate_relative_imports():
    """Show relative import concepts."""
    print("\n=== Relative Imports ===")
    
    print("Relative import syntax:")
    print("  from . import module          # Same package")
    print("  from .subpackage import mod   # Subpackage")
    print("  from ..parent import mod      # Parent package")
    print("  from ...grandparent import mod # Grandparent package")
    
    print("\nPackage structure example:")
    print("  myproject/")
    print("    __init__.py")
    print("    main.py")
    print("    utils/")
    print("      __init__.py")
    print("      helpers.py")
    print("      data/")
    print("        __init__.py")
    print("        processors.py")
    
    print("\nIn processors.py:")
    print("  from ..helpers import some_function    # Import from utils")
    print("  from ...main import main_function      # Import from root")

# =============================================================================
# NAMESPACE PACKAGES
# =============================================================================

def demonstrate_namespace_packages():
    """Show namespace package concepts."""
    print("\n=== Namespace Packages ===")
    
    print("Namespace packages allow splitting a package across directories:")
    print("\nDirectory structure:")
    print("  site-packages/")
    print("    mynamespace/")
    print("      subpackage1/")
    print("        __init__.py")
    print("        module1.py")
    print("    another-location/")
    print("      mynamespace/")
    print("        subpackage2/")
    print("          __init__.py")
    print("          module2.py")
    
    print("\nUsage:")
    print("  from mynamespace.subpackage1 import module1")
    print("  from mynamespace.subpackage2 import module2")
    
    print("\nBenefits:")
    print("  - Distribute parts of a package separately")
    print("  - Plugin architectures")
    print("  - Large projects with multiple teams")

# =============================================================================
# BEST PRACTICES
# =============================================================================

def demonstrate_best_practices():
    """Show best practices for modules and packages."""
    print("\n=== Best Practices ===")
    
    print("1. Module Organization:")
    print("  - One class per module (for large classes)")
    print("  - Group related functions in modules")
    print("  - Use clear, descriptive names")
    
    print("\n2. Import Guidelines:")
    print("  - Standard library imports first")
    print("  - Third-party imports second")
    print("  - Local imports last")
    print("  - Use absolute imports when possible")
    
    print("\n3. Package Structure:")
    print("  - Always include __init__.py")
    print("  - Use __all__ to control public API")
    print("  - Document your packages")
    
    print("\n4. Example import order:")
    print("  import os")
    print("  import sys")
    print("  ")
    print("  import requests")
    print("  import numpy as np")
    print("  ")
    print("  from mypackage import mymodule")
    print("  from . import local_module")
    
    # Create example requirements.txt
    requirements_content = """# Production dependencies
requests>=2.25.0
numpy>=1.20.0
pandas>=1.3.0

# Development dependencies
pytest>=6.0.0
black>=21.0.0
flake8>=3.8.0
"""
    
    with open("requirements.txt", "w") as f:
        f.write(requirements_content)
    
    print("\n5. Created requirements.txt example")
    
    # Clean up
    os.remove("requirements.txt")

# =============================================================================
# MAIN EXECUTION
# =============================================================================

if __name__ == "__main__":
    """Run all demonstrations when script is executed directly."""
    print("Python Modules and Packages Tutorial")
    print("=" * 50)
    
    demonstrate_basic_imports()
    create_sample_module()
    demonstrate_module_path()
    create_sample_package()
    demonstrate_standard_library()
    demonstrate_third_party_packages()
    demonstrate_module_introspection()
    demonstrate_relative_imports()
    demonstrate_namespace_packages()
    demonstrate_best_practices()
    
    print("\n" + "=" * 50)
    print("Modules and packages tutorial completed!")