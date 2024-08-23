from word_lists import word_list
import hangman_art

lives = 6

import random




chosen_word = random.choice(word_list)
print(f"the chosen word is {chosen_word}\n")

for length in range(len(chosen_word)):
        print("_", end=" ")
print("\n")

game_over = False
correct_letters = []

while not game_over:
    guess = input("Guess a letter: ").lower()
    length = len(chosen_word)
    
    display = ""

    for letter in chosen_word:
        if letter == guess:

            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_ "

    print(display)
    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            game_over = True
            print("***************** You lose! *****************")
            print(hangman_art.ending_pic[0])
        
        print(hangman_art.HANGMANPICS[lives])  
        
    
    
    if "_" not in display:
        game_over = True
        print("**************** You win! ****************")
        
    print(f"**************** {lives}/6 lives left ****************")
    