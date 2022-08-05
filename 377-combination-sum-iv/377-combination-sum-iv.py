class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
#         result = set()
#         def dfs(index, curr):
#             print(curr)
#             total = sum(curr)
#             if total > target or index >= len(nums) or nums[index]>target:
#                 return
            
#             if total == target:
#                 # curr.append(nums[index])
#                 result.add(tuple(curr))
#                 return

#             # for i in range(len(nums)):
#             dfs(index, curr+[nums[index]])
#             dfs(index+1, curr+[nums[index]])
            
#         for i in range(len(nums)):
#             dfs(i,[])
#         print(result)
#         return result
                
        dp = {0:1}
        for total in range(1, target+1):
            dp[total] = 0
            for n in nums:
                dp[total] += dp.get(total-n,0)
        return dp[target]