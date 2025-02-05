from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self,quizbrain:QuizBrain):
        self.quiz = quizbrain
        self.window=Tk()
        self.score=0
        self.window.title("quizzer")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.score_label=Label(text="Score: 0",fg="white",bg=THEME_COLOR)
        self.score_label.grid(row=0,column=1)
        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.fr_text = self.canvas.create_text(150, 125, width=280,text="Default_Text", font=("Ariel", 20, "italic"))

        self.canvas.grid(row=1,column=0,columnspan=2,pady=50)

        true_image=PhotoImage(file="images/true.png")
        self.true_button=Button(image=true_image,highlightthickness=0,command=self.true_answer)

        self.true_button.grid(row=2,column=0)

        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_image, highlightthickness=0,command=self.false_answer)

        self.false_button.grid(row=2, column=1)
        self.get_next_question()

        self.window.mainloop()



    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text=self.quiz.next_question()
            self.canvas.itemconfig(self.fr_text,text=q_text)
        else:
            self.canvas.itemconfig(self.fr_text,text="You have reached the end of the questions")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")


    def true_answer(self):
        is_right=self.quiz.check_answer("True")
        self.get_feedback(is_right)


    def false_answer(self):
        is_right=self.quiz.check_answer("False")
        self.get_feedback(is_right)


    def get_feedback(self,is_right):
        self.window.after(1000,func=self.get_next_question)
        if is_right:
            self.canvas.config(bg="green")
            self.score=self.score+1
            self.score_label.config(text=f"Score: {self.score}")
        elif not is_right:
            self.canvas.config(bg="red")
            self.score_label.config(text=f"Score: {self.score}")



