class Solution:

    dp = [0]

    def numSquares(self, n: int) -> int:

        dp = self.dp

        perfectSq = [pow(i,2) for i in range(1, int(sqrt(n))+1)]

        while len(dp) < n+1:

            dpI = inf

            for ps in perfectSq:
                if len(dp)<ps: break
                dpI = min(dpI,1+dp[-ps])
            
            dp.append(dpI)
        
        return dp[n]









# class Solution:
#     def numSquares(self, n: int) -> int:
        
        
        
#         dp = [100 for _ in range(n+1)]
#         dp[0] = 0
        
#         r = 1
#         sq = r*r
        
#         while sq <= n:
#             for i in range(sq, n+1):
#                 dp[i] = min(dp[i], dp[i-sq]+1)
#             r += 1
#             sq = r*r
#         # print(max(dp))
#         return dp[-1]

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