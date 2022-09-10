class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        
#         maxP = 0
#         def dfs(i, j, t, curr):
#             nonlocal maxP
#             if k >= t:
#                 maxP = max(maxP, sum(curr) + dp[i][j])
#                 return
#             curr.append(dp[i][j])
#             t+=1
#             for y,z in enumerate(dp[i][j:]):
#                 print(z)
#                 if z > 0:  
#                     dfs(j, j+y, t+1, curr)
#             curr.pop()
        
        
#         pricesL = len(prices)
#         dp = [[0 for _ in range(pricesL)] for _ in range(pricesL)] 
        
#         for i in range(pricesL):
            
#             for j in range(i+1, pricesL):
#                 # print(i, j)
#                 if prices[j] - prices[i] > 0:
#                     dp[i][j] = prices[j] - prices[i]
        
#         for i in range(pricesL):
#             for j in range(i+1, pricesL):
#                 if dp[i][j] > 0:
#                     dfs(i,j, 1, [])
        
#         return maxP



        if k == 0:  return 0
        dp = [[1000, 0] for _ in range(k+1)]

        for price in prices:
            for i in range(1, k+1):
                
                dp[i][0] = min(dp[i][0], price - dp[i - 1][1])
                dp[i][1] = max(dp[i][1], price - dp[i][0])
                
            print(dp)
        return dp[k][1]

        




















            