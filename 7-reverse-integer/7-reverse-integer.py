class Solution:
    def reverse(self, x: int) -> int:
        
        
        
        if x >= 0:
            r =  int(str(x)[::-1])
        else:

            r = -1*int(str(abs(x))[::-1])

        
        if ((r >= (-(2**31))) and (r<=((2**31)-1))):  
            return r
        return 0