import tkinter as tk
from tkinter import messagebox
import json

# Load quiz data from JSON
def load_questions():
    with open("questions.json", "r") as f:
        return json.load(f)

questions = load_questions()

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🧠 Quiz Application")
        self.root.geometry("500x350")

        self.q_no = 0
        self.score = 0
        self.selected_option = tk.StringVar()

        self.create_widgets()
        self.display_question()

    def create_widgets(self):
        self.question_label = tk.Label(self.root, text="", font=("Arial", 14), wraplength=400, justify="left")
        self.question_label.pack(pady=20)

        self.option_buttons = []
        for i in range(4):
            rb = tk.Radiobutton(self.root, text="", variable=self.selected_option,
                                value="", font=("Arial", 12), anchor="w", justify="left")
            rb.pack(fill="x", padx=20, pady=5)
            self.option_buttons.append(rb)

        self.next_button = tk.Button(self.root, text="Next", command=self.next_question, font=("Arial", 12), bg="#4CAF50", fg="white")
        self.next_button.pack(pady=20)

    def display_question(self):
        q = questions[self.q_no]
        self.question_label.config(text=f"Q{self.q_no + 1}: {q['question']}")
        self.selected_option.set(None)
        for i, option in enumerate(q["options"]):
            self.option_buttons[i].config(text=option, value=option)

    def next_question(self):
        selected = self.selected_option.get()
        if not selected:
            messagebox.showwarning("Warning", "Please select an option!")
            return

        if selected == questions[self.q_no]['answer']:
            self.score += 1

        self.q_no += 1

        if self.q_no < len(questions):
            self.display_question()
        else:
            self.show_result()

    def show_result(self):
        result = f"🎉 Your Score: {self.score} out of {len(questions)}"
        messagebox.showinfo("Quiz Completed", result)
        self.root.destroy()


# Run the app
root = tk.Tk()
app = QuizApp(root)
root.mainloop()
