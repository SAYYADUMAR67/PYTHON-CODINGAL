try:
    num1, num2 = map(int, input("Enter two numbers separated by comma: ").split(","))
    result = num1 / num2
    print(f"The result of {num1} divided by {num2} is: {result}")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except SyntaxError:
    print("Error: Invalid input format. Please enter two numbers separated by a comma.")
except:
    print("Error error wrong input.")
else:
    print("The operation was successful.")
finally:
    print("Execution completed.")