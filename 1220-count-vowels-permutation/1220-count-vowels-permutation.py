class Solution:
    def countVowelPermutation(self, n: int) -> int:
        
        # a -> e, i, u
        # e -> a, i
        # i -> e, o
        # o -> i
        # u -> o, i
        
        a,e,i,o,u=0,1,2,3,4
        
        mod = pow(10,9)+7
        
        dp = [[1]*5]
        
        for j in range(1, n):
            dp.append([0,0,0,0,0])
            dp[j][a] = (dp[j-1][e] + dp[j-1][i] + dp[j-1][u]) % mod
            
            dp[j][e] = (dp[j-1][a] + dp[j-1][i]) % mod
            
            dp[j][i] = (dp[j-1][e] + dp[j-1][o] ) % mod
            
            dp[j][o] = (dp[j-1][i] ) % mod
            
            dp[j][u] = (dp[j-1][o] + dp[j-1][i]) % mod
            
        print(dp)
        return sum(dp[n-1]) % mod