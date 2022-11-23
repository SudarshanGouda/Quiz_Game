from data import question_data
from Question_model import Question
from Quiz_brain import QuizBrain

question_bank=[]

for question in question_data:
    question_text=question['text']
    question_ans=question['answer']
    new_question=Question(question_text,question_ans)
    question_bank.append(new_question)

quiz=QuizBrain(question_bank)

while quiz.still_have_question():
    quiz.next_question()