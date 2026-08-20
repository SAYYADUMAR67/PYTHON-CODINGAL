keys = ['name', 'role', 'language']
values = ['Alice', 'Developer', 'Python']
 
result_1 = [f"{k.upper()}: {v}" for k, v in zip(keys, values)]
print("1. Zip Result:", result_1)
 
 
numbers = [10, 20, 30, 40, 50]
 
result_2 = [num * idx for idx, num in enumerate(numbers) if idx % 2 == 0]
print("2. Enumerate Result:", result_2)
 
 
scores = [55, 82, 65, 91, 43]
 
result_3 = ["Pass" if score >= 70 else "Fail" for score in scores]
print("3. Conditional Result:", result_3)

matrix = [[1, 2], [3, 4], [5, 6]]
 
result_4 = [element for row in matrix for element in row]
print("4. Flattened Matrix:", result_4)
 

sentence = "Advanced Python!"
 
result_5 = [char.upper() for char in sentence if char.lower() in 'aeiou']
print("5. Filtered Vowels:", result_5)