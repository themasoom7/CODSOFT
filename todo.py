import tkinter as tk
from tkinter import messagebox
from datetime import datetime

def add_new_item():
    task = entry.get().strip()
    due = due_entry.get().strip()

    if task:
        current_time = datetime.now().strftime("%d-%m %H:%M")

        if due:
            task_text = f"{task} | Due: {due} | Added: {current_time}"
        else:
            task_text = f"{task} | Added: {current_time}"

        task_box.insert(tk.END, task_text)
        entry.delete(0, tk.END)
        due_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Enter a task first!")

def remove_task():
    try:
        index = task_box.curselection()[0]
        task_box.delete(index)
    except IndexError:
        messagebox.showwarning("Warning", "Select a task to remove!")

def mark_completed():
    try:
        index = task_box.curselection()[0]
        task = task_box.get(index)
        if not task.startswith("✔"):
            task_box.delete(index)
            task_box.insert(index, "✔ " + task)
    except IndexError:
        messagebox.showwarning("Warning", "Select a task!")

def clear_all():
    confirm = messagebox.askyesno("Confirm", "Delete all tasks?")
    if confirm:
        task_box.delete(0, tk.END)

def save_tasks():
    tasks = task_box.get(0, tk.END)
    with open("tasks.txt", "w") as f:
        for t in tasks:
            f.write(t + "\n")
    messagebox.showinfo("Saved", "Tasks saved!")

def load_tasks():
    try:
        with open("tasks.txt", "r") as f:
            for line in f:
                task_box.insert(tk.END, line.strip())
    except FileNotFoundError:
        pass


root = tk.Tk()
root.title("Masoom's Task Manager")
root.geometry("450x560")

title = tk.Label(root, text="Task Tracker", font=("Quadrat", 24, "bold"))
title.pack(pady=10)

entry = tk.Entry(root, width=35)
entry.pack(pady=5)
entry.insert(0, "Enter task")

due_entry = tk.Entry(root, width=35)
due_entry.pack(pady=5)
due_entry.insert(0, "Due date (e.g. 05-04 18:00)")

tk.Button(root, text="Add Task", width=20, command=add_new_item).pack(pady=5)

frame = tk.Frame(root)
frame.pack()

scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

task_box = tk.Listbox(frame, width=50, height=13, yscrollcommand=scrollbar.set)
task_box.pack()

scrollbar.config(command=task_box.yview)

tk.Button(root, text="Mark Completed", width=20, command=mark_completed).pack(pady=5)
tk.Button(root, text="Remove Task", width=20, command=remove_task).pack(pady=5)
tk.Button(root, text="Clear All", width=20, command=clear_all).pack(pady=5)
tk.Button(root, text="Save Tasks", width=20, command=save_tasks).pack(pady=5)

load_tasks()

root.mainloop()
