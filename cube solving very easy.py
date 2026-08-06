def cube (number):
    return number*number*number
def three_cubes (number):
    if number % 3 == 0:
        return cube(number)
    else:
        return False
print(three_cubes(9))
print(three_cubes(4))