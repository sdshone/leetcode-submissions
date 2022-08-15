class Solution:
    def __init__(self):
        
        self.paths = []
        self.cache = {}
        
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        if len(cost) <= 2:
            return min(cost)
        def dfs(i):
            
            if i < 2:
                self.cache[i] = cost[i]
                return cost[i]
            if self.cache.get(i):
                return self.cache.get(i)
            x=dfs(i-1)
            y=dfs(i-2)
            
            self.cache[i] = min(x,y)+ cost[i]
            return self.cache[i]
        
        dfs(len(cost)-1)
        return min(self.cache[len(cost)-1], self.cache.get(len(cost)-2, float('inf')))