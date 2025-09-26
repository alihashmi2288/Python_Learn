"""
Todo List Application
====================

Created by: Syed Ali Hashmi
LinkedIn: https://www.linkedin.com/in/hashmiali2288

A command-line todo application demonstrating file operations, classes, and data persistence.
Features: add/remove tasks, mark complete, save/load from file, priority levels.
"""

import json
import os
from datetime import datetime, date
from enum import Enum

class Priority(Enum):
    """Task priority levels."""
    LOW = 1
    MEDIUM = 2
    HIGH = 3

class Task:
    """Represents a single todo task."""
    
    def __init__(self, title, description="", priority=Priority.MEDIUM):
        self.id = None
        self.title = title
        self.description = description
        self.priority = priority
        self.completed = False
        self.created_date = datetime.now()
        self.completed_date = None
    
    def mark_complete(self):
        """Mark task as completed."""
        self.completed = True
        self.completed_date = datetime.now()
    
    def mark_incomplete(self):
        """Mark task as incomplete."""
        self.completed = False
        self.completed_date = None
    
    def to_dict(self):
        """Convert task to dictionary for JSON serialization."""
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'priority': self.priority.value,
            'completed': self.completed,
            'created_date': self.created_date.isoformat(),
            'completed_date': self.completed_date.isoformat() if self.completed_date else None
        }
    
    @classmethod
    def from_dict(cls, data):
        """Create task from dictionary."""
        task = cls(data['title'], data['description'], Priority(data['priority']))
        task.id = data['id']
        task.completed = data['completed']
        task.created_date = datetime.fromisoformat(data['created_date'])
        if data['completed_date']:
            task.completed_date = datetime.fromisoformat(data['completed_date'])
        return task
    
    def __str__(self):
        status = "✓" if self.completed else "○"
        priority_symbols = {Priority.LOW: "↓", Priority.MEDIUM: "→", Priority.HIGH: "↑"}
        priority_symbol = priority_symbols[self.priority]
        
        return f"[{status}] {priority_symbol} {self.title}"

class TodoList:
    """Manages a collection of todo tasks."""
    
    def __init__(self, filename="todos.json"):
        self.tasks = []
        self.filename = filename
        self.next_id = 1
        self.load_tasks()
    
    def add_task(self, title, description="", priority=Priority.MEDIUM):
        """Add a new task."""
        task = Task(title, description, priority)
        task.id = self.next_id
        self.next_id += 1
        self.tasks.append(task)
        return task
    
    def remove_task(self, task_id):
        """Remove a task by ID."""
        for i, task in enumerate(self.tasks):
            if task.id == task_id:
                removed_task = self.tasks.pop(i)
                return removed_task
        return None
    
    def get_task(self, task_id):
        """Get a task by ID."""
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None
    
    def mark_complete(self, task_id):
        """Mark a task as complete."""
        task = self.get_task(task_id)
        if task:
            task.mark_complete()
            return True
        return False
    
    def mark_incomplete(self, task_id):
        """Mark a task as incomplete."""
        task = self.get_task(task_id)
        if task:
            task.mark_incomplete()
            return True
        return False
    
    def get_tasks(self, completed=None, priority=None):
        """Get filtered list of tasks."""
        filtered_tasks = self.tasks
        
        if completed is not None:
            filtered_tasks = [t for t in filtered_tasks if t.completed == completed]
        
        if priority is not None:
            filtered_tasks = [t for t in filtered_tasks if t.priority == priority]
        
        return filtered_tasks
    
    def save_tasks(self):
        """Save tasks to JSON file."""
        try:
            data = {
                'next_id': self.next_id,
                'tasks': [task.to_dict() for task in self.tasks]
            }
            
            with open(self.filename, 'w') as f:
                json.dump(data, f, indent=2)
            
            return True
        except Exception as e:
            print(f"Error saving tasks: {e}")
            return False
    
    def load_tasks(self):
        """Load tasks from JSON file."""
        try:
            if os.path.exists(self.filename):
                with open(self.filename, 'r') as f:
                    data = json.load(f)
                
                self.next_id = data.get('next_id', 1)
                self.tasks = [Task.from_dict(task_data) for task_data in data.get('tasks', [])]
            
        except Exception as e:
            print(f"Error loading tasks: {e}")
            self.tasks = []
            self.next_id = 1

def display_menu():
    """Display the main menu."""
    print("\n" + "=" * 50)
    print("                TODO LIST MANAGER")
    print("=" * 50)
    print("1. Add Task")
    print("2. View All Tasks")
    print("3. View Pending Tasks")
    print("4. View Completed Tasks")
    print("5. Mark Task Complete")
    print("6. Mark Task Incomplete")
    print("7. Remove Task")
    print("8. Task Statistics")
    print("9. Save Tasks")
    print("0. Exit")
    print("=" * 50)

def display_tasks(tasks, title="Tasks"):
    """Display a list of tasks."""
    print(f"\n{title}")
    print("-" * len(title))
    
    if not tasks:
        print("No tasks found.")
        return
    
    for task in tasks:
        created = task.created_date.strftime("%Y-%m-%d")
        print(f"{task.id:2d}. {task} (Created: {created})")
        if task.description:
            print(f"    Description: {task.description}")

def get_priority_input():
    """Get priority level from user."""
    print("\nPriority levels:")
    print("1. Low (↓)")
    print("2. Medium (→)")
    print("3. High (↑)")
    
    while True:
        try:
            choice = int(input("Enter priority (1-3): "))
            if choice in [1, 2, 3]:
                return Priority(choice)
            else:
                print("Please enter 1, 2, or 3.")
        except ValueError:
            print("Please enter a valid number.")

def get_task_id_input(todo_list, prompt="Enter task ID: "):
    """Get a valid task ID from user."""
    while True:
        try:
            task_id = int(input(prompt))
            if todo_list.get_task(task_id):
                return task_id
            else:
                print("Task ID not found. Please try again.")
        except ValueError:
            print("Please enter a valid number.")

def show_statistics(todo_list):
    """Display task statistics."""
    all_tasks = todo_list.get_tasks()
    completed_tasks = todo_list.get_tasks(completed=True)
    pending_tasks = todo_list.get_tasks(completed=False)
    
    high_priority = todo_list.get_tasks(priority=Priority.HIGH)
    medium_priority = todo_list.get_tasks(priority=Priority.MEDIUM)
    low_priority = todo_list.get_tasks(priority=Priority.LOW)
    
    print("\n" + "=" * 30)
    print("        TASK STATISTICS")
    print("=" * 30)
    print(f"Total Tasks:      {len(all_tasks)}")
    print(f"Completed:        {len(completed_tasks)}")
    print(f"Pending:          {len(pending_tasks)}")
    print()
    print("By Priority:")
    print(f"  High (↑):       {len(high_priority)}")
    print(f"  Medium (→):     {len(medium_priority)}")
    print(f"  Low (↓):        {len(low_priority)}")
    
    if all_tasks:
        completion_rate = (len(completed_tasks) / len(all_tasks)) * 100
        print(f"\nCompletion Rate:  {completion_rate:.1f}%")

def main():
    """Main application loop."""
    todo_list = TodoList()
    
    print("Welcome to Todo List Manager!")
    print("Your tasks are automatically saved.")
    
    while True:
        display_menu()
        
        try:
            choice = input("\nEnter your choice (0-9): ").strip()
            
            if choice == "0":
                todo_list.save_tasks()
                print("Tasks saved. Goodbye!")
                break
            
            elif choice == "1":  # Add Task
                title = input("Enter task title: ").strip()
                if not title:
                    print("Task title cannot be empty.")
                    continue
                
                description = input("Enter description (optional): ").strip()
                priority = get_priority_input()
                
                task = todo_list.add_task(title, description, priority)
                print(f"✓ Added task: {task}")
            
            elif choice == "2":  # View All Tasks
                tasks = todo_list.get_tasks()
                display_tasks(tasks, "All Tasks")
            
            elif choice == "3":  # View Pending Tasks
                tasks = todo_list.get_tasks(completed=False)
                display_tasks(tasks, "Pending Tasks")
            
            elif choice == "4":  # View Completed Tasks
                tasks = todo_list.get_tasks(completed=True)
                display_tasks(tasks, "Completed Tasks")
            
            elif choice == "5":  # Mark Complete
                pending_tasks = todo_list.get_tasks(completed=False)
                if not pending_tasks:
                    print("No pending tasks to complete.")
                    continue
                
                display_tasks(pending_tasks, "Pending Tasks")
                task_id = get_task_id_input(todo_list, "Enter task ID to mark complete: ")
                
                if todo_list.mark_complete(task_id):
                    task = todo_list.get_task(task_id)
                    print(f"✓ Marked complete: {task.title}")
                else:
                    print("Failed to mark task complete.")
            
            elif choice == "6":  # Mark Incomplete
                completed_tasks = todo_list.get_tasks(completed=True)
                if not completed_tasks:
                    print("No completed tasks to mark incomplete.")
                    continue
                
                display_tasks(completed_tasks, "Completed Tasks")
                task_id = get_task_id_input(todo_list, "Enter task ID to mark incomplete: ")
                
                if todo_list.mark_incomplete(task_id):
                    task = todo_list.get_task(task_id)
                    print(f"○ Marked incomplete: {task.title}")
                else:
                    print("Failed to mark task incomplete.")
            
            elif choice == "7":  # Remove Task
                all_tasks = todo_list.get_tasks()
                if not all_tasks:
                    print("No tasks to remove.")
                    continue
                
                display_tasks(all_tasks, "All Tasks")
                task_id = get_task_id_input(todo_list, "Enter task ID to remove: ")
                
                confirm = input(f"Are you sure you want to remove task {task_id}? (y/N): ")
                if confirm.lower() == 'y':
                    removed_task = todo_list.remove_task(task_id)
                    if removed_task:
                        print(f"✓ Removed task: {removed_task.title}")
                    else:
                        print("Failed to remove task.")
                else:
                    print("Task removal cancelled.")
            
            elif choice == "8":  # Statistics
                show_statistics(todo_list)
            
            elif choice == "9":  # Save Tasks
                if todo_list.save_tasks():
                    print("✓ Tasks saved successfully!")
                else:
                    print("✗ Failed to save tasks.")
            
            else:
                print("Invalid choice. Please try again.")
        
        except KeyboardInterrupt:
            print("\n\nSaving tasks and exiting...")
            todo_list.save_tasks()
            break
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()