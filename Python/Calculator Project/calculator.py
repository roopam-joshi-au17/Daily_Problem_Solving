from art import logo
#Addition
def add(n1,n2):
    return n1+n2
#Subtract
def subtract(n1,n2):
    return n1-n2
#Multiplication
def multiply(n1,n2):
    return n1*n2
#Divison
def divide(n1,n2):
    return n1/n2 

operations={"+":add,
            "-":subtract,
            "*":multiply,
            "/":divide
            }
def calculator():
    print(logo)
    num1= float(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)
    should_continue=True
    while should_continue:
        operation_symbol= input("Pick an operation : ")
        num2= float(input("What's the next number?: "))
        calculation_function= operations[operation_symbol]
        answer= calculation_function(num1,num2)      
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        continue_opeation=input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit: ").lower()
        if continue_opeation=="y":
            num1=answer
        else:
            should_continue=False
            calculator()
calculator()


