class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d ={}
        for n in nums:
            if n in d:
                d.pop(n)
                continue
            d[n] = 1
        return list(d.keys())[0]