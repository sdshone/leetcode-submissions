class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        
        M, N = len(grid), len(grid[0])
        
        
        def dfs(row, col):
            
            if row == M:
                return col
            if grid[row][col]==1:
                if 0<=col+1<N and grid[row][col+1]==1:
                    row+=1
                    col+=1
                else:
                    return -1
            else:
                if 0<=col-1<N and grid[row][col-1]==-1:
                    row+=1
                    col-=1
                else:
                    return -1
            return dfs(row, col)

        res = []
        for i in range(N):
            res.append(dfs(0,i))
            
        return res