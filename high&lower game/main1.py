import random
from game_data import data
from art import logo, vs

print(logo)
score = 0
account_a = random.choice(data)
account_b = random.choice(data)


def format_data(account):
    """format the data into printable aformat"""
    account_name = account['name']
    account_follower_count = account['follower_count']
    account_country = account['country']
    account_description = account['description']
    return(f"{account_name}, a {account_follower_count}, from {account_country}, with description: {account_description}")

def check_answer(user_guess, a_followers, b_followers):
    """take a user's guess and the follower counts and returns if they got the right answer or not"""
    if a_follower_count > b_follower_count:
        return user_guess == "a"
    
    
game_should_continue = True
    
#generate a random account from the game data
while game_should_continue:
    account_a = account_b
    account_b = random.choice(data)
    
    while account_a == account_b:
        account_b = random.choice(data)

    print(f"compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Against B: {format_data(account_b)}.")

    #Ask user for a guess
    guess = input("Who has more followers? Type 'A' or 'B': ").lower

    #Check if user is correct

    #get follower count of each account
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]

    is_correct = check_answer(guess, a_follower_count, b_follower_count)
    

    #use if statement to check if user is correct


    #Give user feedback on their guess
    if is_correct:
        score += 1
        print(f"You're right! current score = {score}")
    else:
        print(f"Sorry, that's wrong. Game over. {score}")
        game_should_continue = False

    #keep score


    #Make game repeatable

    # making account at position B become the next account at position A