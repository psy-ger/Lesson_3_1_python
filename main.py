"""Calculator"""

variable_first = int(input("Enter first number: "))
variable_second = int(input("Enter first second: "))
operator_option = input("Enter operator: ")
#v1
if operator_option == "+":
    print(variable_first + variable_second)
elif operator_option == "-":
    print(variable_first - variable_second)
elif operator_option == "*":
    print(variable_first * variable_second)
elif operator_option == "/":
    if variable_second == 0:
        print("Error: Division by zero is not allowed!")
        exit()
    print(variable_first / variable_second)
else:
    print("Error")
#v2
match operator_option:
    case '+':
        print(variable_first + variable_second)
    case '-':
        print(variable_first - variable_second)
    case '/':
        if variable_second == 0:
            print("Error: Division by zero is not allowed!")
            exit()
        print(variable_first / variable_second)
    case '*':
        print(variable_first * variable_second)
    case _:
        print("Error")