class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # result = [[1]*n]*m
        result = []
        for i in range(m):
            result.append([1 for j in range(n)])
        
        if m==1 or n==1:
            return 1
        print(result)
        for r in range(m-2,-1,-1):
            for c in range(n-2, -1, -1):
                print(r,c)
                result[r][c]=result[r+1][c] + result[r][c+1]
            print(result)
        return result[0][0]
            