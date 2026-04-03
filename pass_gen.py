import tkinter as tk
from tkinter import messagebox
import random
import string

def Generate_password():
    try:
        size = int(length_box.get())

        if size < 4:
            messagebox.showwarning("Invalid", "Minimum length is 4")
            return

        letters_small = string.ascii_lowercase
        letters_big = string.ascii_uppercase
        numbers = string.digits
        special = "!@#$%^&*()_+-=[]{}<>?"

        pwd_list = [
            random.choice(letters_small),
            random.choice(letters_big),
            random.choice(numbers),
            random.choice(special)
        ]

        all_characters = letters_small + letters_big + numbers + special

        for _ in range(size - 4):
            pwd_list.append(random.choice(all_characters))

        random.shuffle(pwd_list)
        password = "".join(pwd_list)

        output_label.config(text="Password: " + password)

        window.clipboard_clear()
        window.clipboard_append(password)

    except ValueError:
        messagebox.showerror("Error", "Enter valid number")


window = tk.Tk()
window.title("Password Generator")
window.geometry("380x320")
window.resizable(False, False)

tk.Label(window, text="Password Generator Tool",
         font=("Calibri", 15, "bold")).pack(pady=15)

tk.Label(window, text="Password Length").pack()

length_box = tk.Entry(window, width=8, justify="center")
length_box.insert(0, "12")
length_box.pack(pady=5)

tk.Button(window,
          text="Generate Password",
          command=Generate_password,
          width=18).pack(pady=15)

output_label = tk.Label(window,
                        text="Your password will appear here",
                        wraplength=300)
output_label.pack(pady=10)

tk.Label(window,
         text="Auto copied to clipboard",
         font=("Arial", 9),
         fg="gray").pack(side="bottom", pady=8)

window.mainloop()
