class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        if x < 0: return False
        num = x
        new_num = 0
        factor = 10
        
        while num:
            # print(num%10, new_num, factor)
            new_num = new_num* factor + num % 10 
            if new_num == 0: return False
            num = num // 10
            # factor *= 10
            # print(num, new_num)
        return new_num == x