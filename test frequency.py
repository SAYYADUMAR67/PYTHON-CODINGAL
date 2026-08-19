test_dict = {'code': 2, 'Gfg': 3, 'ide': 3}
target_value = 3
 
frequency = 0
for value in test_dict.values():
    if value == target_value:
        frequency += 1
 
print(f"The frequency of {target_value} is: {frequency}")