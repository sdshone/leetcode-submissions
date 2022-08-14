class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0]) 
        p = 0
        for row in range(ROWS):
            for col in range(COLS):
                
                
                if grid[row][col] == 1:
                    
                    if row -1 < 0 or grid[row-1][col] ==0:
                        p +=1
                    if row +1 >= ROWS or grid[row+1][col]==0:
                        p+=1
                    if col -1 < 0 or grid[row][col-1]==0:
                        p+=1
                    if col +1 >=COLS or grid[row][col+1]==0:
                        p+=1
                # print(p)
        return p