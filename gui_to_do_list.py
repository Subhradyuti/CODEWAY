import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import json

class ToDoApp:
    def __init__(self, master):
        self.master = master
        self.master.title("To-Do List App")

        self.tasks = []

        self.task_var = tk.StringVar()
        self.due_date_var = tk.StringVar()
        self.priority_var = tk.StringVar()
        self.selected_task_index = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        # Entry for task
        task_entry = tk.Entry(self.master, textvariable=self.task_var, width=40)
        task_entry.grid(row=0, column=0, padx=10, pady=10)

        # Entry for due date
        due_date_entry = tk.Entry(self.master, textvariable=self.due_date_var, width=40)
        due_date_entry.grid(row=0, column=1, padx=10, pady=10)

        # Entry for priority
        priority_entry = tk.Entry(self.master, textvariable=self.priority_var, width=40)
        priority_entry.grid(row=0, column=2, padx=10, pady=10)

        # Buttons
        add_button = tk.Button(self.master, text="Add Task", command=self.add_task)
        add_button.grid(row=1, column=0, padx=10, pady=10)

        remove_button = tk.Button(self.master, text="Remove Task", command=self.remove_task)
        remove_button.grid(row=1, column=1, padx=10, pady=10)

        update_button = tk.Button(self.master, text="Update Task", command=self.update_task)
        update_button.grid(row=1, column=2, padx=10, pady=10)

        # Listbox to display tasks
        self.task_listbox = tk.Listbox(self.master, width=60, height=10)
        self.task_listbox.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

        # Entry for selecting task to update
        selected_task_entry = tk.Entry(self.master, textvariable=self.selected_task_index, width=10)
        selected_task_entry.grid(row=3, column=0, padx=10, pady=10)

        # Populate listbox with existing tasks
        self.display_tasks()

    def add_task(self):
        task = self.task_var.get().strip()
        due_date = self.due_date_var.get().strip()
        priority = self.priority_var.get().strip()

        if task:
            date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            new_task = {'title': task, 'date': date, 'due_date': due_date, 'priority': priority}
            self.tasks.append(new_task)
            self.save_tasks()
            self.display_tasks()
            self.task_var.set("")  # Clear the task entry
            self.due_date_var.set("")  # Clear the due date entry
            self.priority_var.set("")  # Clear the priority entry
        else:
            messagebox.showwarning("Warning", "Task cannot be empty!")

    def remove_task(self):
        selected_task_index = self.task_listbox.curselection()

        if selected_task_index:
            index = int(selected_task_index[0])
            removed_task = self.tasks.pop(index)
            self.save_tasks()
            self.display_tasks()
            messagebox.showinfo("Task Removed", f"Task '{removed_task['title']}' removed successfully.")
        else:
            messagebox.showwarning("Warning", "Please select a task to remove.")

    def update_task(self):
        index = int(self.selected_task_index.get())
        if 0 <= index < len(self.tasks):
            task = self.tasks[index]
            task['title'] = self.task_var.get().strip()
            task['due_date'] = self.due_date_var.get().strip()
            task['priority'] = self.priority_var.get().strip()
            self.save_tasks()
            self.display_tasks()
            messagebox.showinfo("Task Updated", f"Task '{task['title']}' updated successfully.")
        else:
            messagebox.showwarning("Warning", "Invalid task index.")

    def display_tasks(self):
        self.task_listbox.delete(0, tk.END)  # Clear existing tasks in listbox
        for i, task in enumerate(self.tasks):
            self.task_listbox.insert(tk.END, f"{i}. {task['title']} - {task['date']}")

    def save_tasks(self):
        with open('tasks.json', 'w') as file:
            json.dump(self.tasks, file)

def main():
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
