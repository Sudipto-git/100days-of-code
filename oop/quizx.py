from data import quiz_data

class QuizBrain:
    def __init__(self, question_list):
        self.question_list = question_list
        self.question_number = 0
        self.score = 0
        
    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        
        input(f"Q.{self.question_number}: {current_question['question']} (True/False): ")