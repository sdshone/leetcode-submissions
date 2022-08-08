class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # nums.sort()
        
        dp = [1] * len(nums)
        
        for i in range(len(nums)-2,-1,-1):
            max_c = [1]
            for j in range(i+1, len(nums)):
                if nums[j] > nums[i]:
                    max_c.append(1+ dp[j])
            dp[i] = max(max_c)
        return max(dp)