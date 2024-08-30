import art




def add(n1,n2):
    return n1+n2

def subtract(n1,n2):
    return n1-n2

def multiply(n1,n2):
    return n1*n2

def divide(n1,n2):
    return n1/n2
# keep everything inside a function
print(art.logo)
opeartions = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}
# value = {}

# while True:

#     operator = (input("What you wanna do? +, -, *, /: "))

#answer = opeartions[opeartion_symbol](num1,num2)
#     for symbol in opeartions:
#         print(symbol)
#

#         if operator == "+" :
#             num1 = int(input("Enter first number: "))
#             num2 = int(input("Enter second number: "))
#             print("{num1} {opeartion_symbol} {num2} = {answer}")
#         elif operator == "-" :
#             num1 = int(input("Enter first number: "))
#             num2 = int(input("Enter second number: "))
#             print("{num1} {opeartion_symbol} {num2} = {answer}")
#         elif operator == "*" :
#             num1 = int(input("Enter first number: "))
#             num2 = int(input("Enter second number: "))
#             print("{num1} {opeartion_symbol} {num2} = {answer}")
#         elif operator == "/" :
#             num1 = int(input("Enter first number: "))
#             num2 = int(input("Enter second number: "))
#             print("{num1} {opeartion_symbol} {num2} = {answer}")
#         else:
#             print("Invalid input")
#             break
def calculator():
    should_continue = True
    num1 = float(input("Enter first number: "))     
    while should_continue:
        
        for symbol in opeartions:
            print(symbol)
        opeartion_symbol = input("Pick an operation: ")
        num2 = float(input("Enter second number: "))
        answer = opeartions[opeartion_symbol](num1,num2)
        print(f"{num1} {opeartion_symbol} {num2} = {answer}")

        choide = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation ans e to close: ")

        if choide == 'y':
            num1 = answer
        elif choide == 'n':
            should_continue = False
            print("\n" * 20)
            num1 = float(input("Enter a new number: "))
            continue
        elif choide == 'e':
            should_continue = False
            print("Goodbye")
            break
        calculator()

calculator() 
    
