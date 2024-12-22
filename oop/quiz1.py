# class user:
#     def __init__(self,user_id,user_name):
#         self.id = user_id
#         self.name = user_name
#         self.followers = 0
#         pass
        

# user_1 = user("001","John")
# user_2 = user("002","Jane")

# print(user_1.name)

class question:
    def __init__(self,question_1,answer):
        self.question1 = question_1
        self.question2 = answer
        pass
    
    
student_1 = question("Whats your name? ","jhon")
student_11 = question("Whats your age? ",30)

print(student_1.question1,student_1.question2)
print(student_11.question1,student_11.question2)