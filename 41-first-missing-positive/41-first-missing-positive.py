class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        seen = set()
        
        for num in nums:
            if num > 0 :
                seen.add(num)
        i=0
        print(seen)
        for i in range(1,len(seen)+1):
            if i not in seen:
                return i
        return i+1