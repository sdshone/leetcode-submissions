class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        result = [[0]*n]*m
        for row in result:
            row[-1]=1
        for r in range(len(row)):
            row[r]=1
        
        for i in range(m-2,-1,-1):
            for j in range(n-2,-1,-1):
                result[i][j] = result[i+1][j]+result[i][j+1]
        return result[0][0]