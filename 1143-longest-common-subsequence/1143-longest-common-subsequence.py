class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        memo = {}
        
        def dp(i, j):
            
            
            if (i,j) in memo:
                return memo[(i,j)]
            if i<0 or j<0: return 0
            if text1[i] == text2[j]:
                memo[(i,j)]=1+ dp(i-1, j-1)
                return memo[(i,j)]
            
            else:
                memo[(i,j)]=max(dp(i-1,j), dp(i, j-1))
                return max(dp(i-1,j), dp(i, j-1))
            
        return dp(len(text1)-1, len(text2)-1)