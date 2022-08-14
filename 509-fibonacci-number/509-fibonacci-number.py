class Solution:
    def fib(self, n: int) -> int:
        
        cache = [-1]*(n+1)
        def dfs(i):
            
            if i < 2:
                return i
            print(i)
            if cache[i]!=-1:
                return cache[i]

            cache[i] = dfs(i-1)+dfs(i-2)
            return cache[i]
    
        return dfs(n)