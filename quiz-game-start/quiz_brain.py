class QuizBrain:
    def __init__(self, q_list):
        self.question_no = 0
        self.question_list = q_list
        self.score = 0

    def next_question(self):
        current_q = self.question_list[self.question_no]
        self.question_no += 1
        user_ans = input(f"Q{self.question_no}. {current_q.text} (True or False)")
        self.check_ans(user_ans, current_q.answer)

    def still_has_ques(self):
        total_no_ques = len(self.question_list)
        if self.question_no >= total_no_ques:
            return False
        else:
            return True

    def check_ans(self, user_ans, correct_ans):
        if user_ans.lower() == correct_ans.lower():
            print("That's correct")
            self.score += 1

        else:
            print("Wrong Ans")
            print(f"Corrct Ans is {correct_ans}")
        print(f"Current score is {self.score}/{self.question_no}")
        print("\n")
