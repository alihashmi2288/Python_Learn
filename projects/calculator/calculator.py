"""
Simple Calculator Project
========================

Created by: Syed Ali Hashmi
LinkedIn: https://www.linkedin.com/in/hashmiali2288

A command-line calculator demonstrating functions, error handling, and user interaction.
Features: basic operations, memory functions, and history tracking.
"""

import math
import json
from datetime import datetime

class Calculator:
    """A simple calculator with memory and history features."""
    
    def __init__(self):
        self.memory = 0
        self.history = []
    
    def add(self, a, b):
        """Add two numbers."""
        result = a + b
        self._add_to_history(f"{a} + {b} = {result}")
        return result
    
    def subtract(self, a, b):
        """Subtract b from a."""
        result = a - b
        self._add_to_history(f"{a} - {b} = {result}")
        return result
    
    def multiply(self, a, b):
        """Multiply two numbers."""
        result = a * b
        self._add_to_history(f"{a} × {b} = {result}")
        return result
    
    def divide(self, a, b):
        """Divide a by b."""
        if b == 0:
            raise ValueError("Cannot divide by zero")
        result = a / b
        self._add_to_history(f"{a} ÷ {b} = {result}")
        return result
    
    def power(self, base, exponent):
        """Calculate base raised to exponent."""
        result = base ** exponent
        self._add_to_history(f"{base} ^ {exponent} = {result}")
        return result
    
    def square_root(self, number):
        """Calculate square root."""
        if number < 0:
            raise ValueError("Cannot calculate square root of negative number")
        result = math.sqrt(number)
        self._add_to_history(f"√{number} = {result}")
        return result
    
    def memory_store(self, value):
        """Store value in memory."""
        self.memory = value
        self._add_to_history(f"Stored {value} in memory")
    
    def memory_recall(self):
        """Recall value from memory."""
        self._add_to_history(f"Recalled {self.memory} from memory")
        return self.memory
    
    def memory_clear(self):
        """Clear memory."""
        self.memory = 0
        self._add_to_history("Memory cleared")
    
    def _add_to_history(self, operation):
        """Add operation to history."""
        timestamp = datetime.now().strftime("%H:%M:%S")
        self.history.append(f"[{timestamp}] {operation}")
    
    def show_history(self):
        """Display calculation history."""
        if not self.history:
            print("No calculations in history")
            return
        
        print("\nCalculation History:")
        print("-" * 40)
        for entry in self.history[-10:]:  # Show last 10 entries
            print(entry)
    
    def clear_history(self):
        """Clear calculation history."""
        self.history.clear()
        print("History cleared")

def get_number_input(prompt):
    """Get a valid number from user input."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")

def display_menu():
    """Display the calculator menu."""
    print("\n" + "=" * 40)
    print("         CALCULATOR MENU")
    print("=" * 40)
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (×)")
    print("4. Division (÷)")
    print("5. Power (^)")
    print("6. Square Root (√)")
    print("7. Memory Store (MS)")
    print("8. Memory Recall (MR)")
    print("9. Memory Clear (MC)")
    print("10. Show History")
    print("11. Clear History")
    print("0. Exit")
    print("=" * 40)

def main():
    """Main calculator program."""
    calculator = Calculator()
    
    print("Welcome to the Python Calculator!")
    
    while True:
        display_menu()
        
        try:
            choice = input("\nEnter your choice (0-11): ").strip()
            
            if choice == "0":
                print("Thank you for using the calculator!")
                break
            
            elif choice == "1":  # Addition
                a = get_number_input("Enter first number: ")
                b = get_number_input("Enter second number: ")
                result = calculator.add(a, b)
                print(f"Result: {result}")
            
            elif choice == "2":  # Subtraction
                a = get_number_input("Enter first number: ")
                b = get_number_input("Enter second number: ")
                result = calculator.subtract(a, b)
                print(f"Result: {result}")
            
            elif choice == "3":  # Multiplication
                a = get_number_input("Enter first number: ")
                b = get_number_input("Enter second number: ")
                result = calculator.multiply(a, b)
                print(f"Result: {result}")
            
            elif choice == "4":  # Division
                a = get_number_input("Enter dividend: ")
                b = get_number_input("Enter divisor: ")
                try:
                    result = calculator.divide(a, b)
                    print(f"Result: {result}")
                except ValueError as e:
                    print(f"Error: {e}")
            
            elif choice == "5":  # Power
                base = get_number_input("Enter base: ")
                exponent = get_number_input("Enter exponent: ")
                result = calculator.power(base, exponent)
                print(f"Result: {result}")
            
            elif choice == "6":  # Square Root
                number = get_number_input("Enter number: ")
                try:
                    result = calculator.square_root(number)
                    print(f"Result: {result}")
                except ValueError as e:
                    print(f"Error: {e}")
            
            elif choice == "7":  # Memory Store
                value = get_number_input("Enter value to store: ")
                calculator.memory_store(value)
                print(f"Stored {value} in memory")
            
            elif choice == "8":  # Memory Recall
                value = calculator.memory_recall()
                print(f"Memory contains: {value}")
            
            elif choice == "9":  # Memory Clear
                calculator.memory_clear()
                print("Memory cleared")
            
            elif choice == "10":  # Show History
                calculator.show_history()
            
            elif choice == "11":  # Clear History
                calculator.clear_history()
            
            else:
                print("Invalid choice. Please try again.")
        
        except KeyboardInterrupt:
            print("\n\nCalculator interrupted. Goodbye!")
            break
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()