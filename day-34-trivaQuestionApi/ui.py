from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#6c58ad"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzer")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        
        self.score_label = Label(self.window, text="Score: 0", bg=THEME_COLOR, fg="white")
        self.score_label.grid(row=0, column=1)
        
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Some Question Text",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic")
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        
        # Buttons
        true_image = PhotoImage(file="/Users/sudipto/Documents/code/projects/100days of code/day-34-trivaQuestionApi/images/true.png")
        self.true_button = Button(image=true_image, highlightthickness=0, width=100, height=97, command=self.true_pressed)
        self.true_button.grid(row=2, column=0)
        
        false_image = PhotoImage(file="/Users/sudipto/Documents/code/projects/100days of code/day-34-trivaQuestionApi/images/false.png")
        self.false_button = Button(image=false_image, highlightthickness=0, width=100, height=97, command=self.false_pressed)
        self.false_button.grid(row=2, column=1)
        
        self.get_next_question()
        
        self.window.mainloop()
        
    def get_next_question(self):
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
            self.canvas.config(bg="white")
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz!")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
         
    def true_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)
        
    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)
        
    def give_feedback(self, is_right):
        self.window.after(1000, self.get_next_question)
        if is_right:
            self.canvas.config(bg="#5fc246")
        else:
            self.canvas.config(bg="#00a0cc")
        self.window.after(1000, self.get_next_question)