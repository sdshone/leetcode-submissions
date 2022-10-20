class Solution:
    def intToRoman(self, num: int) -> str:
        num_to_roman = {
            1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'
        }
        roman_num = []
        multiplier = 1
        while (num!=0):
            r = num%10

            roman_digit = num_to_roman.get(r*multiplier)
            if not roman_digit:
                if r==4 or r==9: 
                    roman_digit = num_to_roman.get(multiplier)+num_to_roman.get(r*multiplier+multiplier)
                elif r>4:
                    r=r-5
                    roman_digit = num_to_roman.get(multiplier*5)+num_to_roman.get(multiplier)*r
                else:
                    roman_digit = num_to_roman.get(multiplier)*r
            
            roman_num.append(roman_digit)   
            multiplier *= 10
            num=num//10
        roman_num.reverse()
        return ''.join(roman_num)