class Solution:
    def missingNumber(self, nums: List[int]) -> int:
#         num_set = set(nums)
        
#         for i in range(1, len(nums)+1):
#             if i not in num_set:
#                 return i
#         return 0

        res = len(nums)
    
        for i in range(len(nums)):
            res += (i-nums[i])
        return res