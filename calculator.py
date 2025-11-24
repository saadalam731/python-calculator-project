# Basic Calculator Project
# Made by Saad Alam Shaikh (25BCE10850) - VIT Bhopal

def arithmetic_operation(choice, num1, num2):
    if choice == "1":
        return num1 + num2
    elif choice == "2":
        return num1 - num2
    elif choice == "3":
        return num1 * num2
    elif choice == "4":
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero"
    else:
        return "Invalid Choice"
def take_input():
    print("Simple Calculator")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Enter choice (1/2/3/4): ")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    return choice, num1, num2

def display_result(result):
    print("Result:", result)

choice, num1, num2 = take_input()
result = arithmetic_operation(choice, num1, num2)
display_result(result)
