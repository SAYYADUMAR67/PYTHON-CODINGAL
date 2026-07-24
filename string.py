string = input("Enter a string: ")
string2 = "" 
for i in string:
    string2 = i + string2
print("\nthe original string =", string)
print("the reversed string =", string2)