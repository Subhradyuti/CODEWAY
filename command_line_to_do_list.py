import os
import json
from datetime import datetime

def load_tasks():
    if os.path.exists('tasks.json'):
        with open('tasks.json', 'r') as file:
            tasks = json.load(file)
        return tasks
    else:
        return []

def save_tasks(tasks):
    with open('tasks.json', 'w') as file:
        json.dump(tasks, file)

def display_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        print("To-Do List:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task['title']} - {task['date']} - Due Date: {task.get('due_date', 'Not set')} - Priority: {task.get('priority', 'Not set')}")

def add_task(tasks, title, due_date=None, priority=None):
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    new_task = {'title': title, 'date': date, 'due_date': due_date, 'priority': priority}
    tasks.append(new_task)
    save_tasks(tasks)
    print(f"Task '{title}' added successfully.")

def update_task(tasks, index, title=None, due_date=None, priority=None):
    if 1 <= index <= len(tasks):
        task = tasks[index - 1]

        if title:
            task['title'] = title
        if due_date:
            task['due_date'] = due_date
        if priority:
            task['priority'] = priority

        save_tasks(tasks)
        print(f"Task '{task['title']}' updated successfully.")
    else:
        print("Invalid task index.")

def remove_task(tasks, index):
    if 1 <= index <= len(tasks):
        removed_task = tasks.pop(index - 1)
        save_tasks(tasks)
        print(f"Task '{removed_task['title']}' removed successfully.")
    else:
        print("Invalid task index.")

def main():
    tasks = load_tasks()

    while True:
        print("\n1. Display tasks")
        print("2. Add task")
        print("3. Update task")
        print("4. Remove task")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            display_tasks(tasks)
        elif choice == '2':
            title = input("Enter task title: ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            priority = input("Enter priority: ")
            add_task(tasks, title, due_date, priority)
        elif choice == '3':
            display_tasks(tasks)
            index = int(input("Enter the task index to update: "))
            title = input("Enter new task title (press enter to keep the existing title): ")
            due_date = input("Enter new due date (YYYY-MM-DD, press enter to keep the existing due date): ")
            priority = input("Enter new priority (press enter to keep the existing priority): ")
            update_task(tasks, index, title, due_date, priority)
        elif choice == '4':
            display_tasks(tasks)
            index = int(input("Enter the task index to remove: "))
            remove_task(tasks, index)
        elif choice == '5':
            print("Exiting the To-Do List application.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
