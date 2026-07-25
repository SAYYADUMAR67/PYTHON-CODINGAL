def power_with_for_loop(base, exponent):
    result = 1
    for _ in range(exponent):
        result *= base
    return result
 
def power_with_while_loop(base, exponent):
    result = 1
    while exponent > 0:
        result *= base
        exponent -= 1
    return result
 
base_num = 3
exp_num = 4
 
print(f"Using For Loop: {base_num}^{exp_num} = {power_with_for_loop(base_num, exp_num)}")
print(f"Using While Loop: {base_num}^{exp_num} = {power_with_while_loop(base_num, exp_num)}")
 