try:
    # Your code that may raise a ValueError
    value = int(input("Enter a number: "))
    print(f"You entered: {value}")
except ValueError:
    print("GET OUT!.")