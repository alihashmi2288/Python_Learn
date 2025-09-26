"""
Python File Operations
======================

This module demonstrates file handling in Python - reading, writing, and manipulating files.
Learn about file modes, context managers, and best practices for file operations.
"""

import os
import json
import csv
from pathlib import Path

# =============================================================================
# BASIC FILE OPERATIONS
# =============================================================================

def demonstrate_basic_file_operations():
    """Show basic file reading and writing."""
    print("=== Basic File Operations ===")
    
    # Writing to a file
    filename = "sample.txt"
    content = """Hello, World!
This is a sample file.
It contains multiple lines.
Python file operations are powerful!"""
    
    # Write file
    with open(filename, 'w') as file:
        file.write(content)
    print(f"✓ Created file: {filename}")
    
    # Read entire file
    with open(filename, 'r') as file:
        file_content = file.read()
    print(f"File content:\n{file_content}")
    
    # Read file line by line
    print("\nReading line by line:")
    with open(filename, 'r') as file:
        for line_num, line in enumerate(file, 1):
            print(f"  Line {line_num}: {line.strip()}")
    
    # Clean up
    os.remove(filename)
    print(f"✓ Cleaned up: {filename}")

# =============================================================================
# FILE MODES
# =============================================================================

def demonstrate_file_modes():
    """Show different file opening modes."""
    print("\n=== File Modes ===")
    
    filename = "modes_demo.txt"
    
    # Write mode ('w') - creates new file or overwrites existing
    with open(filename, 'w') as file:
        file.write("Original content\n")
    print("✓ Written with 'w' mode")
    
    # Append mode ('a') - adds to end of file
    with open(filename, 'a') as file:
        file.write("Appended content\n")
    print("✓ Appended with 'a' mode")
    
    # Read mode ('r') - default mode
    with open(filename, 'r') as file:
        content = file.read()
    print(f"Content after append:\n{content}")
    
    # Read and write mode ('r+')
    with open(filename, 'r+') as file:
        file.seek(0)  # Go to beginning
        original = file.read()
        file.seek(0)  # Go back to beginning
        file.write("Modified: " + original)
    
    with open(filename, 'r') as file:
        print(f"After r+ modification:\n{file.read()}")
    
    # Binary mode
    binary_filename = "binary_demo.bin"
    data = b"Binary data: \x00\x01\x02\x03"
    
    with open(binary_filename, 'wb') as file:
        file.write(data)
    
    with open(binary_filename, 'rb') as file:
        binary_content = file.read()
    print(f"Binary content: {binary_content}")
    
    # Clean up
    os.remove(filename)
    os.remove(binary_filename)

# =============================================================================
# CONTEXT MANAGERS AND ERROR HANDLING
# =============================================================================

def demonstrate_context_managers():
    """Show proper file handling with context managers."""
    print("\n=== Context Managers ===")
    
    filename = "context_demo.txt"
    
    # Good practice: using 'with' statement
    try:
        with open(filename, 'w') as file:
            file.write("Content written safely\n")
            file.write("File will be closed automatically\n")
        print("✓ File written and closed automatically")
        
        # File is automatically closed here, even if an error occurs
        with open(filename, 'r') as file:
            content = file.read()
        print(f"Content: {content.strip()}")
        
    except FileNotFoundError:
        print("File not found!")
    except PermissionError:
        print("Permission denied!")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Clean up
        if os.path.exists(filename):
            os.remove(filename)
    
    # Handling non-existent files
    try:
        with open("nonexistent.txt", 'r') as file:
            content = file.read()
    except FileNotFoundError:
        print("✓ Handled FileNotFoundError gracefully")

# =============================================================================
# WORKING WITH DIFFERENT FILE FORMATS
# =============================================================================

def demonstrate_text_files():
    """Work with text files and encoding."""
    print("\n=== Text Files and Encoding ===")
    
    filename = "text_demo.txt"
    
    # Writing with specific encoding
    text_content = "Hello, 世界! Café résumé naïve"
    
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(text_content)
    print("✓ Written with UTF-8 encoding")
    
    # Reading with specific encoding
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
    print(f"Content: {content}")
    
    # Working with lines
    lines = ["Line 1: Introduction", "Line 2: Body", "Line 3: Conclusion"]
    
    with open(filename, 'w') as file:
        for line in lines:
            file.write(line + '\n')
    
    # Reading lines into a list
    with open(filename, 'r') as file:
        read_lines = file.readlines()
    
    print("Lines read:")
    for i, line in enumerate(read_lines):
        print(f"  {i}: {line.strip()}")
    
    os.remove(filename)

def demonstrate_json_files():
    """Work with JSON files."""
    print("\n=== JSON Files ===")
    
    filename = "data.json"
    
    # Python data to save
    data = {
        "name": "Alice",
        "age": 30,
        "skills": ["Python", "JavaScript", "SQL"],
        "is_active": True,
        "projects": {
            "web_app": {"status": "completed", "rating": 4.5},
            "mobile_app": {"status": "in_progress", "rating": None}
        }
    }
    
    # Write JSON file
    with open(filename, 'w') as file:
        json.dump(data, file, indent=2)
    print("✓ JSON data written")
    
    # Read JSON file
    with open(filename, 'r') as file:
        loaded_data = json.load(file)
    
    print("Loaded JSON data:")
    print(f"  Name: {loaded_data['name']}")
    print(f"  Skills: {loaded_data['skills']}")
    print(f"  Projects: {len(loaded_data['projects'])}")
    
    # Pretty print JSON
    print("\nFormatted JSON:")
    print(json.dumps(loaded_data, indent=2))
    
    os.remove(filename)

def demonstrate_csv_files():
    """Work with CSV files."""
    print("\n=== CSV Files ===")
    
    filename = "data.csv"
    
    # Sample data
    students = [
        ["Name", "Age", "Grade", "Subject"],
        ["Alice", 20, "A", "Math"],
        ["Bob", 19, "B", "Physics"],
        ["Charlie", 21, "A", "Chemistry"],
        ["Diana", 20, "B+", "Biology"]
    ]
    
    # Write CSV file
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(students)
    print("✓ CSV data written")
    
    # Read CSV file
    print("CSV content:")
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row_num, row in enumerate(reader):
            if row_num == 0:
                print(f"  Headers: {row}")
            else:
                print(f"  Row {row_num}: {row}")
    
    # Using DictReader for named access
    print("\nUsing DictReader:")
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(f"  {row['Name']} (Age {row['Age']}): Grade {row['Grade']} in {row['Subject']}")
    
    os.remove(filename)

# =============================================================================
# FILE SYSTEM OPERATIONS
# =============================================================================

def demonstrate_file_system_operations():
    """Show file system operations."""
    print("\n=== File System Operations ===")
    
    # Check if file exists
    filename = "test_file.txt"
    print(f"File '{filename}' exists: {os.path.exists(filename)}")
    
    # Create file
    with open(filename, 'w') as file:
        file.write("Test content")
    
    print(f"File '{filename}' exists after creation: {os.path.exists(filename)}")
    
    # Get file information
    file_stats = os.stat(filename)
    print(f"File size: {file_stats.st_size} bytes")
    print(f"Last modified: {file_stats.st_mtime}")
    
    # Get file extension and name
    name, ext = os.path.splitext(filename)
    print(f"Name: '{name}', Extension: '{ext}'")
    
    # Directory operations
    directory = "test_directory"
    
    if not os.path.exists(directory):
        os.makedirs(directory)
        print(f"✓ Created directory: {directory}")
    
    # List directory contents
    print(f"Current directory contents:")
    for item in os.listdir('.'):
        if os.path.isfile(item):
            print(f"  File: {item}")
        elif os.path.isdir(item):
            print(f"  Directory: {item}")
    
    # Clean up
    os.remove(filename)
    os.rmdir(directory)
    print("✓ Cleaned up test files and directories")

# =============================================================================
# PATHLIB - MODERN PATH HANDLING
# =============================================================================

def demonstrate_pathlib():
    """Show modern path handling with pathlib."""
    print("\n=== Pathlib (Modern Path Handling) ===")
    
    # Create Path objects
    current_dir = Path('.')
    file_path = Path('example.txt')
    
    print(f"Current directory: {current_dir.absolute()}")
    print(f"File path: {file_path}")
    
    # Create file using pathlib
    file_path.write_text("Content written using pathlib")
    print("✓ File created using pathlib")
    
    # Read file using pathlib
    content = file_path.read_text()
    print(f"Content: {content}")
    
    # Path operations
    print(f"File name: {file_path.name}")
    print(f"File stem: {file_path.stem}")
    print(f"File suffix: {file_path.suffix}")
    print(f"Parent directory: {file_path.parent}")
    print(f"Is file: {file_path.is_file()}")
    print(f"Exists: {file_path.exists()}")
    
    # Working with directories
    test_dir = Path('test_pathlib')
    test_dir.mkdir(exist_ok=True)
    
    # Create nested file
    nested_file = test_dir / 'nested' / 'file.txt'
    nested_file.parent.mkdir(parents=True, exist_ok=True)
    nested_file.write_text("Nested file content")
    
    print(f"✓ Created nested file: {nested_file}")
    
    # Iterate through directory
    print("Directory contents:")
    for item in test_dir.rglob('*'):
        print(f"  {item}")
    
    # Clean up
    file_path.unlink()
    nested_file.unlink()
    nested_file.parent.rmdir()
    test_dir.rmdir()
    print("✓ Cleaned up pathlib examples")

# =============================================================================
# PRACTICAL FILE OPERATIONS
# =============================================================================

def demonstrate_practical_examples():
    """Show practical file operation examples."""
    print("\n=== Practical Examples ===")
    
    # Log file processing
    log_filename = "app.log"
    log_entries = [
        "2024-01-01 10:00:00 INFO Application started",
        "2024-01-01 10:01:00 DEBUG User login attempt",
        "2024-01-01 10:01:05 INFO User logged in successfully",
        "2024-01-01 10:05:00 ERROR Database connection failed",
        "2024-01-01 10:05:30 INFO Database connection restored",
        "2024-01-01 10:10:00 WARNING High memory usage detected"
    ]
    
    # Create log file
    with open(log_filename, 'w') as file:
        for entry in log_entries:
            file.write(entry + '\n')
    
    # Process log file - count log levels
    log_counts = {"INFO": 0, "DEBUG": 0, "ERROR": 0, "WARNING": 0}
    
    with open(log_filename, 'r') as file:
        for line in file:
            for level in log_counts:
                if level in line:
                    log_counts[level] += 1
                    break
    
    print("Log level counts:")
    for level, count in log_counts.items():
        print(f"  {level}: {count}")
    
    # Configuration file example
    config_filename = "config.txt"
    config_data = {
        "database_host": "localhost",
        "database_port": "5432",
        "debug_mode": "True",
        "max_connections": "100"
    }
    
    # Write configuration
    with open(config_filename, 'w') as file:
        for key, value in config_data.items():
            file.write(f"{key}={value}\n")
    
    # Read configuration
    config = {}
    with open(config_filename, 'r') as file:
        for line in file:
            if '=' in line:
                key, value = line.strip().split('=', 1)
                config[key] = value
    
    print("\nConfiguration loaded:")
    for key, value in config.items():
        print(f"  {key}: {value}")
    
    # File backup example
    backup_filename = log_filename + ".backup"
    
    # Copy file content
    with open(log_filename, 'r') as source:
        with open(backup_filename, 'w') as backup:
            backup.write(source.read())
    
    print(f"✓ Created backup: {backup_filename}")
    
    # Clean up
    os.remove(log_filename)
    os.remove(config_filename)
    os.remove(backup_filename)
    print("✓ Cleaned up practical examples")

# =============================================================================
# MAIN EXECUTION
# =============================================================================

if __name__ == "__main__":
    """Run all demonstrations when script is executed directly."""
    print("Python File Operations Tutorial")
    print("=" * 50)
    
    demonstrate_basic_file_operations()
    demonstrate_file_modes()
    demonstrate_context_managers()
    demonstrate_text_files()
    demonstrate_json_files()
    demonstrate_csv_files()
    demonstrate_file_system_operations()
    demonstrate_pathlib()
    demonstrate_practical_examples()
    
    print("\n" + "=" * 50)
    print("File operations tutorial completed!")