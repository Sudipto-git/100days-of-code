MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def is_resources_sufficient(order,ingredients):
    for item in ingredients:
        if ingredients[item] >= resources[item]:
            print(f"sorry there is not enough {item}")
            return False
        
    return True

def process_coins():
    print("please insert coins")
    total = int(input("how many quarters?")) * 0.25
    total += int(input("how many dimes?")) * 0.1
    total += int(input("how many nickles?")) * 0.05
    total += int(input("how many pennies?")) * 0.01
    return total

def is_transaction_successful(money_recived,drink_cost):
    if money_recived >= drink_cost:
        change = round(money_recived - drink_cost,2)
        print(f"Here is your change{change}")
        
        global  profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money, Money refunded")
        return False
    
def make_coffee(drink_name,order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
        
    print(f"Here is your {drink_name} ☕️ . Enjoy!")


is_on = True

while is_on:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ")
    if user_choice == 'off':
        is_on = False
        print("machine is off, Thank you")
        
    elif user_choice =='report':
        print(f"water: {resources['water']}ml")
        print(f"milk: {resources['milk']}ml")
        print(f"coffee: {resources['coffee']}g")
        print(f"money: ${profit}")
    
    else:
        drink = MENU[user_choice]
        print(drink)
        if is_resources_sufficient(user_choice,drink['ingredients']):
            payment = process_coins()
            if is_transaction_successful(payment,drink['cost']):
                make_coffee(user_choice,drink['ingredients'])
                
        