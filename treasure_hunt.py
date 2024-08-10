print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[Sudipto]
********************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")  
choice1 = input('Youre at a crossroad, where do you want to go? Type "left" or "right"\n').lower()

if choice1 =='right':
    print("Game Over! you fall into a hole")
else:
    print("You've come to a lake. There is an island in the middle of the lake.")
    choice2 = input('Type "wait" to wait for a boat. Type "swim" to swim across\n')
    if choice2 == "swim":
        print("Game Over! You were eaten by a tortoise")
    else:
        print("You arrive at the island unharmed. There is a house with 3 doors. RED has a treasure, WHITE has fire and BLACK has a monster. Choose wisely!!!")
        
    choice3 = input('Which door do you want to open? Type "red", "white" or "black"\n')
    if choice3 == "red":
        print("Congratulations! You found the treasure")
    elif choice3 == "white":
        print("Game Over! You were burned by fire")
    else:
        print("Game Over! You were eaten by a monster")
        
print("Thank you for playing")