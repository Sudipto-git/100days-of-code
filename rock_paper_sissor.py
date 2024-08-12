# Rock
import random

a =("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

# Paper
b = ("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

# Scissors
c =("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
while True:
    
    print("Welcome to Rock, Paper, Scissors Game")
    user_input = input("Enter your choice: a for Rock, b for Paper, c for Scissors: ")
    option = ["a", "b", "c"]
    computer_choice = random.choice(option)


    if user_input == "a":
        print("You chose Rock")
        print(a)
        print("Computer chose:",computer_choice)
        if computer_choice == "a":
            print(a)
            print("It's a draw")
        elif computer_choice == "b":
            print(b)
            print("You lose")
        else:
            print(c)
            print("You win")
        
    elif user_input == "b":
        print("You chose Paper")
        print(b)
        print("Computer chose:",computer_choice)
        if computer_choice == "a":
            print(a)
            print("You win")
        elif computer_choice == "b":
            print(b)
            print("It's a draw")
        else:
            print(c)
            print("You lose")
        
    elif user_input == "c" :
        print("You chose Scissors")
        print(c)
        print("Computer chose:",computer_choice)
        if computer_choice == "a":
            print(a)
            print("You lose")
        elif computer_choice == "b":
            print(b)
            print("You win")
        else:
            print(c)
            print("It's a draw")
    else:
        print("Invalid input")


    
    
    print("Do you want to play again?")
    play_again = input("Enter y for Yes and n for No: ")
    if play_again != "y":
        print("Thank you for playing")
        break
   
