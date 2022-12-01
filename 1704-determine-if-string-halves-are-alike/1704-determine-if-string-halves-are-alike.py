class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        
        count = 0
        i = 0
        S = len(s)
        while i < S:
            if s[i] in vowels:
                if i < S//2:
                    count += 1
                else:
                    count -= 1
            i += 1
        return count == 0