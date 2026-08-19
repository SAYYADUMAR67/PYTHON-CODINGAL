num1 = [1,2,3,4,5]
num2 = [6,7,8,9,10]
result = map(lambda x,y: x+y,num1,num2)
print ("addition of two list")
print(list(result))
num = [1,2,3,4,5]
def sq(n):
    return n*n
square = list(map(sq,num))
print(square)