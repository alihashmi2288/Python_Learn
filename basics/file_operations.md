# File Operations in Python

**Created by: Syed Ali Hashmi**  
**LinkedIn: [https://www.linkedin.com/in/hashmiali2288](https://www.linkedin.com/in/hashmiali2288)**

## Overview
File operations allow programs to read from and write to files, enabling data persistence and interaction with external data sources.

## Basic File Operations

### Opening Files
```python
# Basic syntax
file = open(filename, mode)

# Always close files when done
file.close()

# Better: Use context managers (recommended)
with open(filename, mode) as file:
    # File operations here
    pass  # File automatically closed
```

### File Modes

| Mode | Description | Creates File | Truncates |
|------|-------------|--------------|-----------|
| `'r'` | Read (default) | No | No |
| `'w'` | Write | Yes | Yes |
| `'a'` | Append | Yes | No |
| `'x'` | Exclusive creation | Yes | N/A |
| `'r+'` | Read and write | No | No |
| `'w+'` | Write and read | Yes | Yes |
| `'a+'` | Append and read | Yes | No |

Add `'b'` for binary mode: `'rb'`, `'wb'`, etc.

## Reading Files

### Read Entire File
```python
with open('file.txt', 'r') as f:
    content = f.read()
    print(content)
```

### Read Line by Line
```python
with open('file.txt', 'r') as f:
    for line in f:
        print(line.strip())  # strip() removes newline
```

### Read All Lines into List
```python
with open('file.txt', 'r') as f:
    lines = f.readlines()
    # lines is a list with newline characters
```

### Read One Line at a Time
```python
with open('file.txt', 'r') as f:
    first_line = f.readline()
    second_line = f.readline()
```

## Writing Files

### Write String to File
```python
with open('output.txt', 'w') as f:
    f.write("Hello, World!\n")
    f.write("Second line\n")
```

### Write Multiple Lines
```python
lines = ["Line 1\n", "Line 2\n", "Line 3\n"]
with open('output.txt', 'w') as f:
    f.writelines(lines)
```

### Append to File
```python
with open('log.txt', 'a') as f:
    f.write("New log entry\n")
```

## Working with Different File Formats

### JSON Files
```python
import json

# Write JSON
data = {"name": "Alice", "age": 30}
with open('data.json', 'w') as f:
    json.dump(data, f, indent=2)

# Read JSON
with open('data.json', 'r') as f:
    data = json.load(f)
```

### CSV Files
```python
import csv

# Write CSV
data = [
    ['Name', 'Age', 'City'],
    ['Alice', 30, 'New York'],
    ['Bob', 25, 'London']
]

with open('people.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(data)

# Read CSV
with open('people.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

# Read CSV with headers
with open('people.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(f"{row['Name']} is {row['Age']} years old")
```

## File System Operations

### Check if File Exists
```python
import os

if os.path.exists('file.txt'):
    print("File exists")
else:
    print("File not found")
```

### Get File Information
```python
import os

stats = os.stat('file.txt')
print(f"Size: {stats.st_size} bytes")
print(f"Modified: {stats.st_mtime}")
```

### Directory Operations
```python
import os

# Create directory
os.makedirs('new_folder', exist_ok=True)

# List directory contents
for item in os.listdir('.'):
    print(item)

# Remove directory
os.rmdir('empty_folder')  # Only works for empty directories
```

## Modern Path Handling with pathlib

```python
from pathlib import Path

# Create Path objects
file_path = Path('data/file.txt')
current_dir = Path('.')

# Path operations
print(file_path.name)        # 'file.txt'
print(file_path.stem)        # 'file'
print(file_path.suffix)      # '.txt'
print(file_path.parent)      # 'data'

# Check existence
if file_path.exists():
    print("File exists")

# Read/write with pathlib
content = file_path.read_text()
file_path.write_text("New content")

# Create directories
file_path.parent.mkdir(parents=True, exist_ok=True)
```

## Error Handling

### Common File Exceptions
```python
try:
    with open('file.txt', 'r') as f:
        content = f.read()
except FileNotFoundError:
    print("File not found")
except PermissionError:
    print("Permission denied")
except IOError:
    print("I/O error occurred")
```

### Safe File Operations
```python
def safe_read_file(filename):
    try:
        with open(filename, 'r') as f:
            return f.read()
    except FileNotFoundError:
        print(f"File {filename} not found")
        return None
    except Exception as e:
        print(f"Error reading file: {e}")
        return None
```

## Best Practices

### 1. Always Use Context Managers
```python
# Good
with open('file.txt', 'r') as f:
    content = f.read()

# Avoid
f = open('file.txt', 'r')
content = f.read()
f.close()  # Easy to forget!
```

### 2. Specify Encoding
```python
# Good - explicit encoding
with open('file.txt', 'r', encoding='utf-8') as f:
    content = f.read()

# Can cause issues with non-ASCII characters
with open('file.txt', 'r') as f:
    content = f.read()
```

### 3. Handle Large Files Efficiently
```python
# For large files, process line by line
def process_large_file(filename):
    with open(filename, 'r') as f:
        for line in f:
            # Process one line at a time
            process_line(line.strip())
```

### 4. Use Appropriate File Modes
```python
# Reading existing file
with open('data.txt', 'r') as f:
    pass

# Creating new file (overwrites existing)
with open('output.txt', 'w') as f:
    pass

# Adding to existing file
with open('log.txt', 'a') as f:
    pass
```

## Common Patterns

### Configuration Files
```python
def load_config(filename):
    config = {}
    try:
        with open(filename, 'r') as f:
            for line in f:
                if '=' in line:
                    key, value = line.strip().split('=', 1)
                    config[key] = value
    except FileNotFoundError:
        print("Config file not found, using defaults")
    return config
```

### Log Files
```python
import datetime

def log_message(message, log_file='app.log'):
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open(log_file, 'a') as f:
        f.write(f"[{timestamp}] {message}\n")
```

### File Backup
```python
def backup_file(filename):
    backup_name = f"{filename}.backup"
    try:
        with open(filename, 'r') as source:
            with open(backup_name, 'w') as backup:
                backup.write(source.read())
        print(f"Backup created: {backup_name}")
    except Exception as e:
        print(f"Backup failed: {e}")
```

## Performance Tips

1. **Use appropriate buffer sizes for large files**
2. **Process files line by line for memory efficiency**
3. **Use binary mode for non-text files**
4. **Consider using generators for large datasets**
5. **Close files promptly (use context managers)**