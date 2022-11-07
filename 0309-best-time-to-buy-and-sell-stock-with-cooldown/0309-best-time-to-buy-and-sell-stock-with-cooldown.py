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
        

        P = len(prices)
        dp = {}
        def dfs(i, sell):

            if i >= P:
                return 0
            if (i,sell) in dp:
                return dp[(i,sell)]
            # no buy no sell
            
            if sell is not None:
                t = prices[i]-sell
                dp[(i,sell)] = max(t+dfs(i+2, None), dfs(i+1, sell))
            else:
                #buy
                dp[(i,sell)] = max(dfs(i+1, prices[i]),  dfs(i+1, sell))
            return dp[(i,sell)]
        

        return dfs(0, None)