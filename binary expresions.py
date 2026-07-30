def decimal_to_binary(decimal_num):
    
    if decimal_num == 0:
        return "0"
        
    binary_result = ""
    
    while decimal_num > 0:
        
        remainder = 0
        while decimal_num % 2 != 0:
            remainder = 1
            decimal_num = decimal_num - 1
            
        binary_result = str(remainder) + binary_result
        
        
        decimal_num = decimal_num // 2
        
    return binary_result

number = 13
print(f"The binary representation of {number} is: {decimal_to_binary(number)}")