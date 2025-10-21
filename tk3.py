import tkinter as tk
from tkinter import messagebox

questions = [
    "What is the capital of France?",
    "Which planet is known as the Red Planet?",
    "Who wrote 'Hamlet'?",
    "What is 5 + 3?"
]

options = [
    ["Paris", "London", "Berlin", "Rome"],
    ["Earth", "Mars", "Jupiter", "Venus"],
    ["Shakespeare", "Newton", "Einstein", "Darwin"],
    ["5", "8", "9", "7"]
]

answers = [0, 1, 0, 1]
current_q = 0
score = 0

def next_question():
    global current_q, score
    selected = choice.get()
    if selected == -1:
        messagebox.showwarning("Warning", "Please select an answer!")
        return
    if selected == answers[current_q]:
        score += 1
    current_q += 1
    if current_q < len(questions):
        load_question()
    else:
        messagebox.showinfo("Quiz Completed", f"Your Score: {score}/{len(questions)}")
        root.destroy()

def load_question():
    choice.set(-1)
    question_label.config(text=questions[current_q])
    for i in range(4):
        options_btns[i].config(text=options[current_q][i])

root = tk.Tk()
root.title("Mini Quiz")
root.geometry("400x300")

question_label = tk.Label(root, text="", wraplength=350, font=("Arial", 12))
question_label.pack(pady=20)

choice = tk.IntVar(value=-1)
options_btns = []
for i in range(4):
    rb = tk.Radiobutton(root, text="", variable=choice, value=i, font=("Arial", 10))
    rb.pack(anchor="w")
    options_btns.append(rb)

tk.Button(root, text="Next", command=next_question).pack(pady=20)

load_question()
root.mainloop()