class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        max_path = 1
        dp = {}
        N=len(matrix)
        M=len(matrix[0])
        def dfs(i,j,prev):
            
            if i<0 or i>=N or j<0 or j>=M or matrix[i][j] <=prev:
                return 0
            if (i,j) in dp:
                return dp[(i,j)]
                
            dirs = [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]
            res = 1
            for x,y in dirs:
                res = max(res, 1+dfs(x,y, matrix[i][j]))
            dp[(i,j)] = res
            return res
        for i in range(N):
            for j in range(M):
                x=dfs(i,j, -1)
        return max(dp.values())