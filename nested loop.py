string=input("Enter a string: ")
character=input("Enter a character to count: ")
i=0
count=0
while i<len(string):
    if string[i]==character:
        count+=1
    i+=1
print("Number of occurrences of '{}': {}".format(character, count))