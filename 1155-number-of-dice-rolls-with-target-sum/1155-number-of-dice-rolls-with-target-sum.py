class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        
        cache = {}
        mod = 10**9 + 7
        def dfs(n, k, target):
            
            if n == 1:
                return int(0 < target <= k)
            if (target,n) in cache:
                return cache[(target,n)]
            
            cache[(target,n)] = 0
            
            for i in range(1, k+1):
                cache[(target,n)] += dfs(n-1, k, target-i)
            cache[(target,n)] = cache[(target,n)] % mod
            
            return cache[(target,n)]
        return dfs(n,k,target)
