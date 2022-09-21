class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        
        N, M = len(nums), len(multipliers)
        
        # dp ={}
#         def dfs(left, total):
#             if total == M:
#                 return 0
            
#             if (left, total) in dp:
#                 return dp[(left, total)]
            
#             l = nums[left] * multipliers[total] + dfs(left+1, total+1)
#             r = nums[N-1 - (total - left)] * multipliers[total] + dfs(left, total+1)
            
#             dp[(left, total)] = max(l, r)
            
#             return dp[(left,total)]

#         return dfs(0, 0)
    
        dp = [[0] * (M+1) for _ in range(M+1)]
        
        for total in range(M-1, -1, -1):
            for left in range(total, -1, -1):
                
                dp[total][left] = max(nums[left] * multipliers[total] + dp[total+1][left+1], nums[N-1 - (total - left)] * multipliers[total] + dp[total+1][left])
                
        
        return dp[0][0]