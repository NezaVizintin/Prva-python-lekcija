number1 = int(input("Enter the first number: "))
operation = input("Enter the operation: ")
number2 = int(input("Enter the second number: "))

if operation == "+":
    print(number1 + number1)
elif operation == "-":
    print(number1 - number2)
elif operation == "*":
    print(number1 * number2)
elif operation == "/":
    print(number1 / number2)
else:
    print("I don't recognise the operation.")