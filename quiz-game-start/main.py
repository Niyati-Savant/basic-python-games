from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank=[]
for item in question_data:
    x = item['text']
    y = item['answer']
    obj = Question(x,y)
    question_bank.append(obj)

quiz_brain = QuizBrain(question_bank)
while quiz_brain.still_has_ques():
    quiz_brain.next_question()

print(f"Final Score is {quiz_brain.score}")