class Solution:
    def maxProfit(self, prices: List[int]) -> int:
    
        if len(prices) == 1: return 0
        max_profit = 0
        i,j=0,1
        while j<len(prices):
            if prices[j]<prices[i]:
                i=j
                j+=1
                continue
            max_profit = max(max_profit, prices[j]-prices[i])
            print(max_profit)
            j+=1
        return max_profit