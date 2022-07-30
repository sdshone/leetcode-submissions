class Solution:
    def rob(self, nums: List[int]) -> int:
        
# O(n) Space complexity        
#         if not nums:
#             return 0
#         if len(nums) == 1:
#             return nums[0]
        
#         dp = [0]*len(nums)
#         dp[0] = nums[0]
#         dp[1] = max(nums[0], nums[1])
        
#         for i in range(2, len(nums)):
#             dp[i] = max(dp[i-2]+nums[i], dp[i-1])
#         print(dp)
#         return dp[-1]
        
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        first = nums[0]
        second = max(nums[0], nums[1])
        curr = second
        for i in range(2, len(nums)):
            curr = max(first+nums[i], second)
            first = second
            second = curr
        
        return curr