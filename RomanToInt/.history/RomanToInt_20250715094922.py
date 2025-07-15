"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII,
 which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. 
Instead, the number four is written as IV. Because the one is before the five we subtract it making four. 
The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.
"""

roman_to_int = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

roman = str(input("Roman Number: "))
print(roman)
total = 0
# reversed_number = ""

# for char in roman:
#     reversed_number = char + reversed_number  

# print(reversed_number)

qty = len(roman)

for i in range(qty-1):
    c1 = roman[i]
    c2 = roman[i+1]

    if c1 == 'I' and c2 in ['V', 'X']:
        total += roman_to_int[c2] - roman_to_int[c1]
        i += 1  # Skip the next character since it's already processed
    
    else:
        total += roman_to_int[c1]
        
    if i == qty - 2:  # Check if it's the last character
        total += roman_to_int[c2]
    
print(total)

# for char in roman:
#     if char in roman_to_int:
        
#         total += roman_to_int[char]    
#     else:
#         print(f"Invalid character: {char}")
        
    # print(roman_to_int[char])

    # def romanToInt(self, s: str) -> int:
        
        
    #     total = 0
    #     prev_value = 0
        
    #     for char in s:
    #         value = roman_to_int[char]
    #         if value > prev_value:
    #             total += value - 2 * prev_value
    #         else:
    #             total += value
    #         prev_value = value
            
    #     return total
