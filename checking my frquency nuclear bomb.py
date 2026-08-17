test_dict = {'condigal': 2, 'is': 2, 'best': 2, 'for' : 2, 'coding': 1}

print("The oringal dictionary" + str(test_dict))

kfc = 2
res = 0
for key in test_dict:
    if test_dict[key] == kfc:
        res = res + 1

print("frequency of kfc is : " + str(res))