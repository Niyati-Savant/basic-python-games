from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizzInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.config(background=THEME_COLOR, pady=20, padx=20)
        self.window.title("Quizzer")

        self.score_label = Label(text=f"Score: {quiz_brain.score}", background=THEME_COLOR, highlightthickness=0,
                                 foreground="white")
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, background="white")
        self.question_text = self.canvas.create_text(150, 125,
                                                     text="Lorem ipsum",
                                                     font=("Arial", 20, "italic"),
                                                     width=280,
                                                     fill=THEME_COLOR)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        tick = PhotoImage(file="./images/true.png")
        self.true_button = Button(image=tick, highlightthickness=0, command=self.true)
        self.true_button.grid(row=2, column=0)

        cross = PhotoImage(file="./images/false.png")
        self.false_button = Button(image=cross, highlightthickness=0, command=self.false)
        self.false_button.grid(row=2, column=1)

        self.get_next_ques()
        self.window.mainloop()

    def get_next_ques(self):
        self.canvas.config(background="white")
        if self.quiz.still_has_questions():

            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text,text="You have completed the Quiz")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true(self):
        self.check_ans(self.quiz.check_answer("True"))

    def false(self):
        self.check_ans(self.quiz.check_answer("False"))

    def check_ans(self, user_ans):
        if user_ans:
            self.canvas.config(background="green")
        else:
            self.canvas.config(background="red")

        self.window.after(2000, self.get_next_ques)
