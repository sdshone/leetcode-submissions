class Solution:
    def concatenatedBinary(self, n: int) -> int:
        
        N = 10 **9 + 7
        
        b = ''
        for i in range(1, n+1):
            b += format(i, 'b')
        
        return int(b,2) % N