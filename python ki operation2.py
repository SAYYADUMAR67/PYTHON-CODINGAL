ch = input("enter a character: ")

if ch.isalpha() and len(ch) == 1:
    print(f"'{ch}' is an alphabet.")
else:
    print(f"'{ch}' is not an alphabet.")
    