class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        cache = {}
        ROWS, COLS = len(grid), len(grid[0])
        if not grid: return 0
        def dfs(i, j,):
            
            if i == ROWS -1 and j == COLS -1:
                return grid[i][j]
            
            if i > ROWS -1 or j > COLS - 1:
                return float('inf')
            if cache.get((i,j)): return cache[(i,j)]
            cache[(i,j)] = min(dfs(i+1,j), dfs(i, j+1)) + grid[i][j]
            
            return cache[(i,j)]
        
        dfs(0, 0)
        # print(cache)
        
        return cache.get((0,0), grid[0][0])