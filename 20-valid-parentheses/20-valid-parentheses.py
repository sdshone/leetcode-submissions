class Solution:
    def isValid(self, s: str) -> bool:
        temp = []
        mapping = {
            '{':'}',
            '[':']',
            '(':')',
            
        }
        for char in s:
            if char in ['(', '{', '[']:
                temp.append(char)
            else:
                len_temp = len(temp)
                if len_temp > 0 and mapping.get(temp[len_temp - 1], '') == char:
                    temp.pop()
                else:
                    return False
        if len(temp) == 0:
            return True
        return False