"""
Python Conditionals (if, elif, else)
====================================

This module demonstrates Python conditional statements for decision-making in programs.
Learn about if/elif/else, comparison operators, logical operators, and advanced patterns.
"""

# =============================================================================
# BASIC IF STATEMENTS
# =============================================================================

def basic_if_examples():
    """Demonstrate basic if statement usage."""
    print("=== Basic If Statements ===")
    
    # Simple if statement
    age = 18
    if age >= 18:
        print("You are an adult")
    
    # If with else
    temperature = 25
    if temperature > 30:
        print("It's hot outside")
    else:
        print("It's not too hot")
    
    # Multiple conditions
    score = 85
    if score >= 90:
        print("Grade: A")
    elif score >= 80:
        print("Grade: B")
    elif score >= 70:
        print("Grade: C")
    elif score >= 60:
        print("Grade: D")
    else:
        print("Grade: F")

# =============================================================================
# COMPARISON OPERATORS
# =============================================================================

def demonstrate_comparison_operators():
    """Show all comparison operators in Python."""
    print("\n=== Comparison Operators ===")
    
    a, b = 10, 5
    
    print(f"a = {a}, b = {b}")
    print(f"a == b: {a == b}")  # Equal to
    print(f"a != b: {a != b}")  # Not equal to
    print(f"a > b: {a > b}")    # Greater than
    print(f"a < b: {a < b}")    # Less than
    print(f"a >= b: {a >= b}")  # Greater than or equal to
    print(f"a <= b: {a <= b}")  # Less than or equal to
    
    # String comparisons
    name1, name2 = "Alice", "Bob"
    print(f"\nString comparison:")
    print(f"'{name1}' == '{name2}': {name1 == name2}")
    print(f"'{name1}' < '{name2}': {name1 < name2}")  # Lexicographic order
    
    # List comparisons
    list1, list2 = [1, 2, 3], [1, 2, 4]
    print(f"\nList comparison:")
    print(f"{list1} == {list2}: {list1 == list2}")
    print(f"{list1} < {list2}: {list1 < list2}")

# =============================================================================
# LOGICAL OPERATORS
# =============================================================================

def demonstrate_logical_operators():
    """Show logical operators: and, or, not."""
    print("\n=== Logical Operators ===")
    
    # AND operator
    age = 25
    has_license = True
    
    if age >= 18 and has_license:
        print("Can drive a car")
    
    # OR operator
    is_weekend = False
    is_holiday = True
    
    if is_weekend or is_holiday:
        print("No work today!")
    
    # NOT operator
    is_raining = False
    
    if not is_raining:
        print("Good weather for a walk")
    
    # Complex logical expressions
    temperature = 22
    is_sunny = True
    has_umbrella = False
    
    if (temperature > 20 and is_sunny) or (temperature > 15 and has_umbrella):
        print("Good conditions to go outside")
    
    # Short-circuit evaluation
    print(f"\nShort-circuit evaluation:")
    print(f"True or (1/0): {True or print('This won\'t execute')}")
    print(f"False and (1/0): {False and print('This won\'t execute either')}")

# =============================================================================
# MEMBERSHIP OPERATORS
# =============================================================================

def demonstrate_membership_operators():
    """Show 'in' and 'not in' operators."""
    print("\n=== Membership Operators ===")
    
    # List membership
    fruits = ["apple", "banana", "cherry"]
    
    if "apple" in fruits:
        print("Apple is in the fruit list")
    
    if "orange" not in fruits:
        print("Orange is not in the fruit list")
    
    # String membership
    text = "Python programming"
    
    if "Python" in text:
        print("Found 'Python' in the text")
    
    if "Java" not in text:
        print("'Java' is not in the text")
    
    # Dictionary membership (checks keys by default)
    person = {"name": "Alice", "age": 30}
    
    if "name" in person:
        print("Person has a name")
    
    if "Alice" in person.values():
        print("Alice is one of the values")

# =============================================================================
# IDENTITY OPERATORS
# =============================================================================

def demonstrate_identity_operators():
    """Show 'is' and 'is not' operators."""
    print("\n=== Identity Operators ===")
    
    # None checks
    value = None
    
    if value is None:
        print("Value is None")
    
    if value is not None:
        print("Value is not None")
    else:
        print("Confirmed: value is None")
    
    # Object identity
    list1 = [1, 2, 3]
    list2 = [1, 2, 3]
    list3 = list1
    
    print(f"list1 == list2: {list1 == list2}")  # True (same content)
    print(f"list1 is list2: {list1 is list2}")  # False (different objects)
    print(f"list1 is list3: {list1 is list3}")  # True (same object)
    
    # Boolean and small integer caching
    a = 256
    b = 256
    print(f"a is b (256): {a is b}")  # True (cached)
    
    a = 257
    b = 257
    print(f"a is b (257): {a is b}")  # May be False (not cached)

# =============================================================================
# TRUTHINESS AND FALSY VALUES
# =============================================================================

def demonstrate_truthiness():
    """Show how Python evaluates truthiness."""
    print("\n=== Truthiness in Python ===")
    
    # Falsy values
    falsy_values = [False, 0, 0.0, "", [], {}, set(), None]
    
    print("Falsy values:")
    for value in falsy_values:
        if not value:
            print(f"  {repr(value)} is falsy")
    
    # Truthy values
    truthy_values = [True, 1, -1, "hello", [1], {"a": 1}, {1, 2}]
    
    print("\nTruthy values:")
    for value in truthy_values:
        if value:
            print(f"  {repr(value)} is truthy")
    
    # Practical usage
    user_input = ""
    if user_input:
        print(f"User entered: {user_input}")
    else:
        print("No input provided")
    
    # Checking for empty collections
    shopping_list = []
    if shopping_list:
        print("You have items to buy")
    else:
        print("Your shopping list is empty")

# =============================================================================
# NESTED CONDITIONS
# =============================================================================

def demonstrate_nested_conditions():
    """Show nested if statements and alternatives."""
    print("\n=== Nested Conditions ===")
    
    # Nested if statements
    weather = "sunny"
    temperature = 25
    
    if weather == "sunny":
        if temperature > 20:
            print("Perfect day for outdoor activities")
        else:
            print("Sunny but a bit cold")
    else:
        print("Not sunny today")
    
    # Alternative using logical operators
    if weather == "sunny" and temperature > 20:
        print("Great weather (using logical operators)")
    
    # Multiple nested conditions
    user_role = "admin"
    is_logged_in = True
    has_permission = True
    
    if is_logged_in:
        if user_role == "admin":
            if has_permission:
                print("Access granted to admin panel")
            else:
                print("Admin without permission")
        elif user_role == "user":
            print("Regular user access")
        else:
            print("Unknown user role")
    else:
        print("Please log in first")

# =============================================================================
# CONDITIONAL EXPRESSIONS (TERNARY OPERATOR)
# =============================================================================

def demonstrate_conditional_expressions():
    """Show conditional expressions (ternary operator)."""
    print("\n=== Conditional Expressions ===")
    
    # Basic ternary operator
    age = 20
    status = "adult" if age >= 18 else "minor"
    print(f"Age {age}: {status}")
    
    # Multiple conditions
    score = 85
    grade = "A" if score >= 90 else "B" if score >= 80 else "C"
    print(f"Score {score}: Grade {grade}")
    
    # With function calls
    def get_discount(is_member):
        return 0.1 if is_member else 0.0
    
    is_member = True
    discount = get_discount(is_member)
    print(f"Member discount: {discount * 100}%")
    
    # In list comprehensions
    numbers = [-2, -1, 0, 1, 2]
    abs_numbers = [x if x >= 0 else -x for x in numbers]
    print(f"Absolute values: {abs_numbers}")

# =============================================================================
# MATCH STATEMENTS (PYTHON 3.10+)
# =============================================================================

def demonstrate_match_statements():
    """Show match statements (structural pattern matching)."""
    print("\n=== Match Statements (Python 3.10+) ===")
    
    try:
        # Basic match
        def handle_http_status(status):
            match status:
                case 200:
                    return "OK"
                case 404:
                    return "Not Found"
                case 500:
                    return "Internal Server Error"
                case _:  # Default case
                    return "Unknown Status"
        
        print(f"Status 200: {handle_http_status(200)}")
        print(f"Status 404: {handle_http_status(404)}")
        print(f"Status 999: {handle_http_status(999)}")
        
        # Match with conditions
        def categorize_number(x):
            match x:
                case n if n < 0:
                    return "negative"
                case 0:
                    return "zero"
                case n if n > 0 and n <= 10:
                    return "small positive"
                case _:
                    return "large positive"
        
        test_numbers = [-5, 0, 3, 15]
        for num in test_numbers:
            print(f"{num}: {categorize_number(num)}")
        
        # Match with data structures
        def process_data(data):
            match data:
                case {"type": "user", "name": str(name)}:
                    return f"User: {name}"
                case {"type": "product", "id": int(product_id), "price": float(price)}:
                    return f"Product {product_id}: ${price}"
                case [first, *rest]:
                    return f"List starting with {first}, {len(rest)} more items"
                case _:
                    return "Unknown data format"
        
        test_data = [
            {"type": "user", "name": "Alice"},
            {"type": "product", "id": 123, "price": 29.99},
            [1, 2, 3, 4, 5],
            "unknown"
        ]
        
        for data in test_data:
            print(f"{data} -> {process_data(data)}")
    
    except SyntaxError:
        print("Match statements require Python 3.10 or later")

# =============================================================================
# PRACTICAL EXAMPLES
# =============================================================================

def practical_examples():
    """Show practical conditional statement examples."""
    print("\n=== Practical Examples ===")
    
    # Input validation
    def validate_email(email):
        if not email:
            return False, "Email cannot be empty"
        elif "@" not in email:
            return False, "Email must contain @"
        elif "." not in email.split("@")[1]:
            return False, "Email domain must contain a dot"
        else:
            return True, "Valid email"
    
    test_emails = ["", "invalid", "user@domain", "user@domain.com"]
    for email in test_emails:
        is_valid, message = validate_email(email)
        print(f"'{email}': {message}")
    
    # Grade calculator
    def calculate_grade(scores):
        if not scores:
            return "No scores provided"
        
        average = sum(scores) / len(scores)
        
        if average >= 90:
            return f"A ({average:.1f}%)"
        elif average >= 80:
            return f"B ({average:.1f}%)"
        elif average >= 70:
            return f"C ({average:.1f}%)"
        elif average >= 60:
            return f"D ({average:.1f}%)"
        else:
            return f"F ({average:.1f}%)"
    
    student_scores = [85, 92, 78, 96, 88]
    print(f"\nStudent grade: {calculate_grade(student_scores)}")
    
    # Access control
    def check_access(user_role, resource, action):
        permissions = {
            "admin": ["read", "write", "delete"],
            "editor": ["read", "write"],
            "viewer": ["read"]
        }
        
        if user_role not in permissions:
            return False, "Invalid user role"
        
        if action in permissions[user_role]:
            return True, f"Access granted for {action} on {resource}"
        else:
            return False, f"Access denied for {action} on {resource}"
    
    # Test access control
    test_cases = [
        ("admin", "document", "delete"),
        ("editor", "document", "write"),
        ("viewer", "document", "delete"),
        ("guest", "document", "read")
    ]
    
    print("\nAccess control tests:")
    for role, resource, action in test_cases:
        allowed, message = check_access(role, resource, action)
        print(f"  {role} -> {action} {resource}: {message}")

# =============================================================================
# COMMON PATTERNS AND BEST PRACTICES
# =============================================================================

def demonstrate_best_practices():
    """Show best practices for conditional statements."""
    print("\n=== Best Practices ===")
    
    # 1. Use early returns to reduce nesting
    def process_user_good(user_data):
        """Good: Early returns reduce nesting."""
        if not user_data:
            return "No user data"
        
        if "name" not in user_data:
            return "Name is required"
        
        if len(user_data["name"]) < 2:
            return "Name too short"
        
        return f"Welcome, {user_data['name']}!"
    
    # 2. Use guard clauses
    def calculate_discount_good(price, is_member, coupon_code):
        """Good: Guard clauses handle edge cases first."""
        if price <= 0:
            return 0
        
        if not is_member and not coupon_code:
            return 0
        
        discount = 0
        if is_member:
            discount += 0.1
        if coupon_code == "SAVE20":
            discount += 0.2
        
        return min(discount, 0.3) * price  # Max 30% discount
    
    # 3. Use constants for magic numbers
    MIN_AGE = 18
    MAX_AGE = 65
    
    def is_eligible_age(age):
        """Good: Use named constants instead of magic numbers."""
        return MIN_AGE <= age <= MAX_AGE
    
    # Test the functions
    print("Testing best practices:")
    
    user_tests = [
        None,
        {},
        {"name": "A"},
        {"name": "Alice"}
    ]
    
    for user in user_tests:
        result = process_user_good(user)
        print(f"  User {user}: {result}")
    
    print(f"\nAge eligibility:")
    for age in [17, 25, 66]:
        eligible = is_eligible_age(age)
        print(f"  Age {age}: {'Eligible' if eligible else 'Not eligible'}")

# =============================================================================
# MAIN EXECUTION
# =============================================================================

if __name__ == "__main__":
    """Run all demonstrations when script is executed directly."""
    print("Python Conditionals Tutorial")
    print("=" * 50)
    
    basic_if_examples()
    demonstrate_comparison_operators()
    demonstrate_logical_operators()
    demonstrate_membership_operators()
    demonstrate_identity_operators()
    demonstrate_truthiness()
    demonstrate_nested_conditions()
    demonstrate_conditional_expressions()
    demonstrate_match_statements()
    practical_examples()
    demonstrate_best_practices()
    
    print("\n" + "=" * 50)
    print("Conditionals tutorial completed!")