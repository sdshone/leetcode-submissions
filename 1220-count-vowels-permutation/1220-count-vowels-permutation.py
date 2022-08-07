class Solution:
    def countVowelPermutation(self, n: int) -> int:
        
        # a -> e, i, u
        # e -> a, i
        # i -> e, o
        # o -> i
        # u -> o, i
        
        a,e,i,o,u=0,1,2,3,4
        
        mod = pow(10,9)+7
        
        dp = [[1]*5,[0]*5]
        
        for j in range(1, n):
            # dp.append([0,0,0,0,0])
            dp[1][a] = (dp[0][e] + dp[0][i] + dp[0][u]) % mod
            
            dp[1][e] = (dp[0][a] + dp[0][i]) % mod
            
            dp[1][i] = (dp[0][e] + dp[0][o] ) % mod
            
            dp[1][o] = dp[0][i] 
            
            dp[1][u] = (dp[0][o] + dp[0][i]) % mod
            
            dp[0]=dp[1]
            dp[1]=[0]*5
            
            
        return sum(dp[0]) % mod