class Solution:
    def numSquares(self, n: int) -> int:
        
        
        
        dp = [100 for _ in range(n+1)]
        dp[0] = 0
        
        r = 1
        sq = r*r
        
        while sq <= n:
            for i in range(sq, n+1):
                dp[i] = min(dp[i], dp[i-sq]+1)
            r += 1
            sq = r*r
        # print(max(dp))
        return dp[n]

#         dp = {}
#         def dfs(n):
            
#             if n == 0:
#                 return 0
#             elif n < 0:
#                 return float('inf')
#             if n in dp:
#                 return dp[n]
            
#             minimum = n
#             i = int(sqrt(n))
            
#             while i >= 1:
#                 minimum = min(minimum, dfs(n - (i*i)))
#                 i -= 1
#             dp[n] = minimum+1
#             return dp[n]
        
#         return dfs(n)