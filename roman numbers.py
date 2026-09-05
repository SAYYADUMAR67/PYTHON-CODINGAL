class RomanConverter:
    _ROMAN_MAP = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'),   (90, 'XC'),  (50, 'L'),  (40, 'XL'),
        (10, 'X'),    (9, 'IX'),   (5, 'V'),   (4, 'IV'),
        (1, 'I')
    ]
 
    def int_to_roman(self, num: int) -> str:
        if not isinstance(num, int) or not (0 < num < 4000):
            raise ValueError("Input must be an integer between 1 and 3999.")
 
        roman_numeral = []
        for value, symbol in self._ROMAN_MAP:
            count, num = divmod(num, value)
            roman_numeral.append(symbol * count)
            if num == 0:
                break
                
        return "".join(roman_numeral)
 
if __name__ == "__main__":
    converter = RomanConverter()
    
    print(f"{'Int':<5} {'Roman':<8} | {'Int':<5} {'Roman':<8} | {'Int':<5} {'Roman':<8} | {'Int':<5} {'Roman':<8}")
    print("-" * 54)
    
    for i in range(1, 26):
        col1 = f"{i:<5} {converter.int_to_roman(i):<8}"
        col2 = f"{i+25:<5} {converter.int_to_roman(i+25):<8}"
        col3 = f"{i+50:<5} {converter.int_to_roman(i+50):<8}"
        col4 = f"{i+75:<5} {converter.int_to_roman(i+75):<8}"
        print(f"{col1} | {col2} | {col3} | {col4}")
 