class Solution:
    def romanToInt(self, s: str) -> int:
        i = 0
        mapping = {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000,
            'IV':4,
            'IX':9,
            'XL':40,
            'XC':90,
            'CD':400,
            'CM':900,
        }
        value = 0
        while i < len(s):
            
            if s[i] in ['V', 'L', 'D','X', 'C', 'M']:
                if i-1 in range(len(s)) and mapping.get(s[i-1:i+1]):
                    value+=mapping.get(s[i-1:i+1])
                    value-= mapping.get(s[i-1])
                    print(i,value)
                    i=i+1
                    continue

            value+=mapping.get(s[i])
            print(i,value)
            i+=1
        return value