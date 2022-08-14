class Solution:
    def climbStairs(self, n: int) -> int:
        
        cache = defaultdict(int)
        
        def dfs(i):
            if i==1 or i==2:
                return i
            if cache.get(i):
                return cache[i]
            
            cache[i] = dfs(i-2)+dfs(i-1)
            return cache[i]
        
        return dfs(n)