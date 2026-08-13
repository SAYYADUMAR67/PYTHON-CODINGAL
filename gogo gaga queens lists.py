queen = [3,2,5,1,6,4,7,8,9,10]
print(queen)
count = 0
for i in queen:
    count += 1
    print("The number of queens in the list is:", count)
average = sum(queen)/len(queen)
print("The average of the queens in the list is:", average)
print(count)
queen.sort()
print("smallest element in the list is:", queen[0])
print("largest element in the list is:", queen[-1])