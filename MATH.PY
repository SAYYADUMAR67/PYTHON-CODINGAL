start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))
 
squares = [i**2 for i in range(start, end + 1)]
print(f"\nAll squares in range: {squares}")
 
even_squares = [num for num in squares if num % 2 == 0]
odd_squares = [num for num in squares if num % 2 != 0]
 
print(f"Even squares: {even_squares}")
print(f"Odd squares: {odd_squares}")