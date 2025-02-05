from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
import html

from ui import QuizInterface

question_bank = []
for question in question_data:
    question_text = str(question["question"])
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)
QuizInterface1=QuizInterface(quiz)
while quiz.still_has_questions():
    QuizInterface1.get_next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
