import array as arr
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}
 
result_method_a = set_a.symmetric_difference(set_b)
 
result_method_b = set_a ^ set_b
 
print("Symmetric Difference (Method A):", result_method_a)
print("Symmetric Difference (Method B):", result_method_b)
 

arr.array_1 = [10, 20, 30, 40]
arr.array_2 = [30, 40, 50, 60]
 
arr.array_result = list(set(arr.array_1) ^ set(arr.array_2))
 
print("Symmetric Difference of Arrays:", arr.array_result)