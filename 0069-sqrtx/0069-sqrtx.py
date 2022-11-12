class Solution:
    def mySqrt(self, x: int) -> int:
        
        
        
        if x in [1,2]: return 1
        
        
        r = x if x <20 else int(x/2)
        i=1
        for i in range(r):
            if i*i > x:
                break
        return i-1