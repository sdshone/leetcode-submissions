class Solution:
    def getSum(self, a: int, b: int) -> int:
        MAX = 0x7FFF
        zero = 0xFFFF
        while b:
            a, b = (a^b)&zero, ((a&b)<<1)&zero
        return a if a <=MAX else ~(a^zero)