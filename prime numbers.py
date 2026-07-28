lower=int(input("Enter the lower limit: "))
upper=int(input("Enter the upper limit: "))
print("Prime numbers between {} and {} are:".format(lower, upper))
for num in range(lower, upper + 1):
    if num > 1:
        for i in range(2, int(num**0.5) + 1):
            if (num % i) == 0:
                break
        else:
            print(num)