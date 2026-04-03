import tkinter as tk
import random

# score variables
my_score = 0
cpu_score = 0

def play(move):
    global my_score, cpu_score

    choices = ["Rock", "Paper", "Scissors"]
    cpu = random.choice(choices)

    if move == cpu:
        result = "Tie!"
        clr = "black"

    elif (move == "Rock" and cpu == "Scissors") or \
         (move == "Paper" and cpu == "Rock") or \
         (move == "Scissors" and cpu == "Paper"):
        result = "You Win!"
        my_score += 1
        clr = "green"

    else:
        result = "CPU Wins!"
        cpu_score += 1
        clr = "red"

    show_choice.config(text=f"You: {move} | CPU: {cpu}")
    show_result.config(text=result, fg=clr)
    show_score.config(text=f"You: {my_score}  CPU: {cpu_score}")

def reset():
    global my_score, cpu_score
    my_score = 0
    cpu_score = 0
    show_choice.config(text="Choose your move")
    show_result.config(text="")
    show_score.config(text="You: 0  CPU: 0")


app = tk.Tk()
app.title("Rock Paper Scissors")
app.geometry("380x420")

tk.Label(app, text="Rock Paper Scissors",
         font=("Calibri", 16, "bold")).pack(pady=15)

show_score = tk.Label(app, text="You: 0  CPU: 0")
show_score.pack(pady=5)

show_choice = tk.Label(app, text="Choose your move")
show_choice.pack(pady=5)

show_result = tk.Label(app, text="", font=("Arial", 13, "bold"))
show_result.pack(pady=15)

frame = tk.Frame(app)
frame.pack(pady=10)

tk.Button(frame, text="Rock",
          width=10,
          command=lambda: play("Rock")).grid(row=0, column=0, padx=5)

tk.Button(frame, text="Paper",
          width=10,
          command=lambda: play("Paper")).grid(row=0, column=1, padx=5)

tk.Button(frame, text="Scissors",
          width=10,
          command=lambda: play("Scissors")).grid(row=0, column=2, padx=5)

tk.Button(app, text="Reset",
          command=reset).pack(pady=20)

app.mainloop()
