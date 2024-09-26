import random
import data

def game():
    print("Welcome to the Higher Lower Game!")
    
    score = 0 #initial score is 0
    game_continue = True
    
    while game_continue:
        
        person1, person2 = random.sample(data.keys(), 2) #randomly choose 2 data from data.py
        
        data1 = random.data[person1] #randomly choose data from data.py
        data2 = random.data[person2]
        
        print("Who has more follower?")
        print(f"{data1['name']}, a {data1['profession']} from {data1['country']}")
        print("VS")
        print(f"{data2['name']}, a {data2['profession']} from {data2['country']}")
        
        guess = input("Type 'A' or 'B': ").upper()
        
        compare_result = compare()
        
        
def compare():
    """compare the follower of 2 data"""
    global data1, data2
    
    if data1['follower'] > data2['follower']:
        return 'A'    
        
    else:
        return 'B'
    
        
game()
    
    