class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_have_question(self):
        return self.question_number < len(self.question_list)
        #############Same we can write###########
        # if self.question_number < len(self.question_list):
        #     return True
        # else:
        #     return False

    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        user_ans = input(f'Q {self.question_number + 1}: {self.current_question.text} (true/false)').lower()
        self.question_number += 1
        self.check_ans(user_ans, self.current_question.ans)

    def check_ans(self, userans, realans):
        if userans.lower() == realans.lower():
            self.score += 1
            print(f'You are right and your score is {self.score}/{self.question_number}')
        else:
            print(f'You are wrong and your score is {self.score}/{self.question_number}')
        print(f'write ans is {self.current_question.ans}')
        print('######################')
