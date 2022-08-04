class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        
        ROWS, COLS = len(heights), len(heights[0])
        
        pacific, atlantic = set(), set()
        
        def dfs(r, c, ocean, old_height):
            if ((r,c) in ocean or r<0 or c<0 or r==ROWS or c==COLS or
            heights[r][c] < old_height):
                return
            ocean.add((r,c))
            
            for row, col in [(r,c+1), (r,c-1), (r+1,c), (r-1,c)]:
                dfs(row, col, ocean, heights[r][c])
        
        
        for col in range(COLS):
            dfs(0, col, pacific, heights[0][col])
            dfs(ROWS-1, col, atlantic, heights[ROWS-1][col])
            
        for row in range(ROWS):
            dfs(row, 0, pacific, heights[row][0])
            dfs(row, COLS-1, atlantic, heights[row][COLS-1])
        
        return pacific.intersection(atlantic)