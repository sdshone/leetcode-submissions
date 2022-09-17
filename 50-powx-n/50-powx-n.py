class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        if n == 0:
            return 1
        
        total, val, left = 1, x, abs(n)
        
        
        while left > 1:
            # print(total, val, left)
            if left % 2 == 0:
                left = left // 2
                val = val * val
            else:
                total *= val
                left -= 1

        return total * val if n > 0 else 1 / (total * val)