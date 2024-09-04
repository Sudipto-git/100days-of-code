from random import randint

EASY_LEVEL_TURNS = turns = 10
HARD_LEVEL_TURNS = turns = 5

def check_answer(user_guess, actual_answer,turns):
    """checks answer against guess. Returns the number of turns remaining."""
    if user_guess > actual_answer:
        print("too high")
        return turns - 1
    elif user_guess < actual_answer:
        print("too low")
        return  turns - 1
    elif user_guess == actual_answer:
        print(f"You got it! the answer was {actual_answer}") 
        return 


def set_dificfulty():
   level =  input("Choose a difficulty. Type 'easy' or 'hard': ")
   global turns
   if level == "easy":
       return EASY_LEVEL_TURNS #return  used
   else:
        return HARD_LEVEL_TURNS # return used
       
    
def game():
    
    print("Welcome to the number guessing game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = randint(1, 100)
    print(f"Psst, the correct answer is {answer}")


    turns = set_dificfulty()
   

    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("make a guess: "))
        

        turns = check_answer(guess, answer,turns)
        if turns == 0:
            print("You've run out of guesses, you lose")
            return 
        elif guess != answer:
            print("Guess again.")
            print("")
        
        
game()