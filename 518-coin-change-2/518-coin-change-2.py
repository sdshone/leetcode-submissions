class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # coins.sort()
        res = {}
        def dfs(i, a):
            
            if a==amount:
                return 1
            if a>amount or i ==len(coins):
                return 0
            if (i,a) in res:
                return res[(i,a)]
            
            res[(i,a)] = dfs(i, a+coins[i]) + dfs(i+1,a)
            return res[(i,a)]
        
        return dfs(0,0)