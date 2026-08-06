def factorial(u):
    '''this function takes a number and returns its factorial'''
    if u == 0:
        return 1
    else:
        return u * factorial(u-1)

print(factorial.__doc__)
print("the factorial of 0:",factorial(0))
print("the factorial of 1:",factorial(1))
print("the factorial of 2:",factorial(2))
print("the factorial of 5:",factorial(5))
print("the factorial of 10:",factorial(10))
print("the factorial of 100:",factorial(100))