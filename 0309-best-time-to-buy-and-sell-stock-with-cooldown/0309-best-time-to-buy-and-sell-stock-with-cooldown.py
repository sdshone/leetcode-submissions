class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        
#         buy = float('-inf')
#         sell = 0
#         cooldown = float('-inf')
        
#         for p in prices:
            
#             buy = max(buy, sell-p)
#             sell = max(sell, cooldown)
#             cooldown = buy+p
#         return max(buy, cooldown, sell)
        

#         P = len(prices)
#         dp = {}
#         def dfs(i, sell):

#             if i >= P:
#                 return 0
#             if (i,sell) in dp:
#                 return dp[(i,sell)]

#             if sell is not None:
#                 t = prices[i]-sell
#                 dp[(i,sell)] = max(t+dfs(i+2, None), dfs(i+1, sell))
#             else:
#                 #buy
#                 dp[(i,sell)] = max(dfs(i+1, prices[i]),  dfs(i+1, sell))
#             return dp[(i,sell)]  

#         return dfs(0, None)
    
        P = len(prices)
        dp = [[0 for _ in range(2)] for _ in range(P+2)]
        
        for i in range(P-1, -1, -1):
            
            dp[i][1]  = max(-prices[i]+dp[i+1][0], dp[i+1][1])
            dp[i][0]  = max(prices[i]+dp[i+2][1], dp[i+1][0])
        
        return dp[0][1]
    
    
    