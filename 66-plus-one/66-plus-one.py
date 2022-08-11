class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        l = len(digits)
        if l == 1:
            digits = [digits[0]+1] if digits[0] != 9 else [1,0]
            return digits
        num_nines = 0
        for i in range(l-1, -1, -1):
            if digits[i] !=9:
                
                break
            else:
                num_nines +=1
                digits.pop()
            
        if digits == []:
            return [1]+[0]*num_nines
        else:
            digits[-1] += 1
            return digits+[0]*num_nines
        
        # if digits[-1] == 9:
        #     digits.pop()
        #     digits.extend([1,0])
        # else:
        #     n = digits.pop()
        #     digits.append(n+1)
        return digits