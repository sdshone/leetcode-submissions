class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        
        
        # dynamic programming
        
        N = len(nums)
        ans = [0] * N
        
        for i in range(2, N):
            if nums[i] - nums[i-1] == nums[i-1] - nums[i-2]:
                ans[i] += ans[i-1]+1
        return sum(ans)