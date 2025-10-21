import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get()
    if task != "":
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task!")

def delete_task():
    try:
        selected = task_listbox.curselection()[0]
        task_listbox.delete(selected)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete!")

def clear_all():
    task_listbox.delete(0, tk.END)

root = tk.Tk()
root.title("Task Manager")
root.geometry("350x300")

tk.Label(root, text="Enter Task:").pack(pady=5)
task_entry = tk.Entry(root, width=30)
task_entry.pack(pady=5)

tk.Button(root, text="Add Task", width=12, command=add_task).pack(pady=5)
tk.Button(root, text="Delete Task", width=12, command=delete_task).pack(pady=5)
tk.Button(root, text="Clear All", width=12, command=clear_all).pack(pady=5)

task_listbox = tk.Listbox(root, width=40, height=10)
task_listbox.pack(pady=10)

root.mainloop()