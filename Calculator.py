# This is assignment 0 where I make a simple calculator to
# add, subtract, multiply, and divide

# Get which numbers to use and what operation to utilize
print("This is a simple calculator.")
print("It can add, subtract, multiply, and divide two numbers.")
# boolean variable to enable driving of the program and display of results
calculate = True
while calculate:
    # take user input from first number, then operand, then second number
    num1 = float(input("Enter a number to perform an operation on: "))
    operation = input("Enter either sign to do a following operation: +, -, *, / ")
    while operation != "+" and operation != "-" and operation != "*" and operation != "/":
        operation = input("Error: Illegal Operand. Please enter +, -, *, or / ")
    num2 = float(input("Enter a second number to perform an operation with: "))
    # instantiate result variable to refresh for new numbers
    res = float
    # if/else statements to determine what operation to use
    if operation == "+":
        # perform addition
        res = num1 + num2
    elif operation == "-":
        # perform subtraction
        res = num1 - num2
    elif operation == "*":
        # perform multiplication
        res = num1 * num2
    else:
        # operation = "/", so perform division
        res = num1 / num2
    print("Result: ")
    print(res)
