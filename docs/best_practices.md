# Python Best Practices

**Created by: Syed Ali Hashmi**  
**LinkedIn: [https://www.linkedin.com/in/hashmiali2288](https://www.linkedin.com/in/hashmiali2288)**

## Code Style and Formatting

### PEP 8 Guidelines
- Use 4 spaces for indentation (not tabs)
- Limit lines to 79 characters for code, 72 for comments
- Use blank lines to separate functions and classes
- Put imports at the top of the file

```python
# Good
def calculate_area(length, width):
    """Calculate the area of a rectangle."""
    return length * width

# Avoid
def calculateArea(length,width):
    return length*width
```

### Naming Conventions
```python
# Variables and functions: snake_case
user_name = "alice"
def get_user_data():
    pass

# Classes: PascalCase
class UserAccount:
    pass

# Constants: UPPER_CASE
MAX_CONNECTIONS = 100
API_KEY = "your-key-here"

# Private attributes: leading underscore
class MyClass:
    def __init__(self):
        self._internal_value = 42
        self.__private_value = 24
```

## Documentation

### Docstrings
```python
def calculate_bmi(weight, height):
    """
    Calculate Body Mass Index.
    
    Args:
        weight (float): Weight in kilograms
        height (float): Height in meters
    
    Returns:
        float: BMI value
    
    Raises:
        ValueError: If height is zero or negative
    
    Example:
        >>> calculate_bmi(70, 1.75)
        22.86
    """
    if height <= 0:
        raise ValueError("Height must be positive")
    return weight / (height ** 2)
```

### Comments
```python
# Good: Explain why, not what
def process_payment(amount):
    # Apply discount for bulk orders to encourage larger purchases
    if amount > 1000:
        amount *= 0.95
    return amount

# Avoid: Stating the obvious
def process_payment(amount):
    # Check if amount is greater than 1000
    if amount > 1000:
        amount *= 0.95  # Multiply amount by 0.95
    return amount
```

## Error Handling

### Be Specific with Exceptions
```python
# Good
try:
    value = int(user_input)
except ValueError:
    print("Please enter a valid number")
except KeyboardInterrupt:
    print("Operation cancelled")

# Avoid
try:
    value = int(user_input)
except:  # Too broad
    print("Something went wrong")
```

### Use Custom Exceptions
```python
class ValidationError(Exception):
    """Raised when input validation fails."""
    pass

class DatabaseError(Exception):
    """Raised when database operations fail."""
    pass

def validate_email(email):
    if "@" not in email:
        raise ValidationError("Invalid email format")
```

## Function Design

### Single Responsibility Principle
```python
# Good: Each function has one responsibility
def read_config_file(filename):
    with open(filename, 'r') as f:
        return json.load(f)

def validate_config(config):
    required_keys = ['database_url', 'api_key']
    for key in required_keys:
        if key not in config:
            raise ValueError(f"Missing required key: {key}")

# Avoid: Function doing too much
def setup_application(config_file):
    # Reading file
    with open(config_file, 'r') as f:
        config = json.load(f)
    
    # Validating
    if 'database_url' not in config:
        raise ValueError("Missing database_url")
    
    # Setting up database
    database.connect(config['database_url'])
    
    # Setting up logging
    logging.basicConfig(level=config.get('log_level', 'INFO'))
```

### Use Type Hints
```python
from typing import List, Dict, Optional, Union

def process_users(users: List[Dict[str, str]]) -> List[str]:
    """Process a list of user dictionaries and return usernames."""
    return [user['username'] for user in users]

def find_user(user_id: int) -> Optional[Dict[str, str]]:
    """Find user by ID, return None if not found."""
    # Implementation here
    pass
```

### Avoid Mutable Default Arguments
```python
# Wrong
def add_item(item, my_list=[]):
    my_list.append(item)
    return my_list

# Correct
def add_item(item, my_list=None):
    if my_list is None:
        my_list = []
    my_list.append(item)
    return my_list
```

## Class Design

### Use Properties for Computed Values
```python
class Circle:
    def __init__(self, radius):
        self._radius = radius
    
    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = value
    
    @property
    def area(self):
        return 3.14159 * self._radius ** 2
```

### Prefer Composition Over Inheritance
```python
# Good: Composition
class Engine:
    def start(self):
        return "Engine started"

class Car:
    def __init__(self):
        self.engine = Engine()
    
    def start(self):
        return self.engine.start()

# Sometimes inheritance is appropriate
class ElectricCar(Car):  # Clear is-a relationship
    def __init__(self):
        super().__init__()
        self.battery_level = 100
```

## File and Resource Management

### Always Use Context Managers
```python
# Good
with open('file.txt', 'r') as f:
    content = f.read()

# Avoid
f = open('file.txt', 'r')
content = f.read()
f.close()  # Easy to forget!
```

### Handle Large Files Efficiently
```python
# Good: Process line by line
def process_large_file(filename):
    with open(filename, 'r') as f:
        for line in f:
            process_line(line.strip())

# Avoid: Loading entire file into memory
def process_large_file(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()  # Could use lots of memory
        for line in lines:
            process_line(line.strip())
```

## Performance Best Practices

### Use List Comprehensions Appropriately
```python
# Good for simple transformations
squares = [x**2 for x in range(10)]
evens = [x for x in numbers if x % 2 == 0]

# Use generator expressions for large datasets
sum_of_squares = sum(x**2 for x in range(1000000))

# Use regular loops for complex logic
processed_items = []
for item in items:
    if complex_condition(item):
        result = complex_processing(item)
        if result is not None:
            processed_items.append(result)
```

### Choose Appropriate Data Structures
```python
# Use sets for membership testing
valid_ids = {1, 2, 3, 4, 5}
if user_id in valid_ids:  # O(1) lookup
    process_user()

# Use dictionaries for key-value relationships
user_data = {'name': 'Alice', 'age': 30}

# Use deque for frequent insertions/deletions at both ends
from collections import deque
queue = deque()
queue.appendleft(item)  # Efficient
```

## Security Best Practices

### Input Validation
```python
def process_user_input(user_input):
    # Validate input
    if not isinstance(user_input, str):
        raise TypeError("Input must be a string")
    
    if len(user_input) > 1000:
        raise ValueError("Input too long")
    
    # Sanitize input
    sanitized = user_input.strip()
    
    return sanitized
```

### Avoid Hardcoded Secrets
```python
# Wrong
API_KEY = "sk-1234567890abcdef"

# Better: Use environment variables
import os
API_KEY = os.getenv('API_KEY')
if not API_KEY:
    raise ValueError("API_KEY environment variable not set")
```

## Testing Best Practices

### Write Testable Code
```python
# Good: Easy to test
def calculate_discount(price, discount_rate):
    return price * (1 - discount_rate)

# Harder to test: External dependencies
def calculate_discount_with_tax():
    price = get_price_from_database()
    discount = get_discount_from_api()
    tax_rate = get_tax_rate_from_config()
    return price * (1 - discount) * (1 + tax_rate)
```

### Use Descriptive Test Names
```python
def test_calculate_discount_with_valid_inputs():
    result = calculate_discount(100, 0.1)
    assert result == 90

def test_calculate_discount_raises_error_for_negative_price():
    with pytest.raises(ValueError):
        calculate_discount(-100, 0.1)
```

## Import Organization

### Import Order
```python
# 1. Standard library imports
import os
import sys
from datetime import datetime

# 2. Third-party imports
import requests
import numpy as np
from flask import Flask

# 3. Local application imports
from myapp.models import User
from myapp.utils import helper_function
```

### Avoid Wildcard Imports
```python
# Good
from math import pi, sqrt

# Avoid
from math import *  # Pollutes namespace
```

## Configuration Management

### Use Configuration Files
```python
# config.py
import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev-key')
    DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///app.db')
    DEBUG = os.getenv('DEBUG', 'False').lower() == 'true'

# app.py
from config import Config

app.config.from_object(Config)
```

## Logging Best Practices

### Use Logging Instead of Print
```python
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)

def process_data(data):
    logger.info(f"Processing {len(data)} items")
    
    try:
        result = expensive_operation(data)
        logger.info("Processing completed successfully")
        return result
    except Exception as e:
        logger.error(f"Processing failed: {e}")
        raise
```

## Code Organization

### Package Structure
```
myproject/
├── myproject/
│   ├── __init__.py
│   ├── models/
│   │   ├── __init__.py
│   │   └── user.py
│   ├── utils/
│   │   ├── __init__.py
│   │   └── helpers.py
│   └── main.py
├── tests/
│   ├── __init__.py
│   └── test_models.py
├── requirements.txt
├── setup.py
└── README.md
```

### Use __all__ in Modules
```python
# mymodule.py
def public_function():
    pass

def _private_function():
    pass

__all__ = ['public_function']  # Only this will be imported with "from mymodule import *"
```

## Version Control Best Practices

### .gitignore for Python
```gitignore
# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# Virtual environments
venv/
env/
.env

# IDE files
.vscode/
.idea/

# OS files
.DS_Store
Thumbs.db

# Project specific
config.ini
*.log
```

### Requirements Management
```bash
# Create requirements.txt
pip freeze > requirements.txt

# Install from requirements.txt
pip install -r requirements.txt

# Use virtual environments
python -m venv myenv
source myenv/bin/activate  # On Windows: myenv\Scripts\activate
```

## Common Anti-Patterns to Avoid

### 1. God Objects
```python
# Avoid: Class that does everything
class ApplicationManager:
    def connect_database(self): pass
    def send_email(self): pass
    def process_payments(self): pass
    def generate_reports(self): pass
    def manage_users(self): pass

# Better: Separate responsibilities
class DatabaseManager: pass
class EmailService: pass
class PaymentProcessor: pass
```

### 2. Magic Numbers
```python
# Avoid
if user.age > 18:
    grant_access()

# Better
LEGAL_AGE = 18
if user.age > LEGAL_AGE:
    grant_access()
```

### 3. Premature Optimization
```python
# Don't optimize until you measure
# Write clear code first, optimize later if needed

# Clear and readable
def find_user(users, target_id):
    for user in users:
        if user.id == target_id:
            return user
    return None

# Optimize only if this becomes a bottleneck
```

Remember: "Premature optimization is the root of all evil" - Donald Knuth