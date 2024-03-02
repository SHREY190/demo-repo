logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

def add(n1,n2):
    return n1 + n2

def substract(n1,n2):
    return n1-n2

def multiply(n1,n2):
    return n1 * n2

def divide(n1,n2):
    return n1 / n2

operation = {"+":add, "-":substract, "*":multiply, "/":divide}
def calculator():
    print(logo)

    num1 = float(input("What's the first number?: "))

    for symbol in operation:
        print(symbol)

    operation_used = input("Pick an operation from the line above: ")

    num2 = float(input("What's the second number?: "))

    if operation_used in operation:
        calculation_func = operation[operation_used]
        answer = calculation_func(num1,num2)
        print(f"{num1} {operation_used} {num2} = {answer}")

    more_calc = input(f"Type 'y' to continiue calculating with {answer}, or type 'n' to start a new calculation or type 'end' to exit : ")

    while more_calc=="y":

        operation_used = input("Pick an operation from the line above: ")

        num2 = float(input("What's the second number?: "))

        if operation_used in operation:
            calculation_func = operation[operation_used]
            second_answer = calculation_func(answer,num2)
            print(f"{answer} {operation_used} {num2} = {second_answer}")
            answer = second_answer

        more_calc = input(f"Type 'y' to continiue calculating with {answer}, or type 'n' to start a new calculation or type 'end' to exit : ")
    if more_calc=="n":
        calculator()

calculator()




