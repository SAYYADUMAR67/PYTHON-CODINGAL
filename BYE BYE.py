valid = False
while not valid:
    try:
        value = int(input("Enter a number: "))
        while value%2==0:
            print("tata bye bye goodbye see you.")
        valid = True
    except ValueError:
        print("GET OUT GODDAMN IT.")