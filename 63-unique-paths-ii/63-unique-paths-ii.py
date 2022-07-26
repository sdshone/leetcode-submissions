class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        numWays = obstacleGrid
        
        ROWS, COLS = len(numWays), len(numWays[0])
        for i in range(ROWS):
            for j in range(COLS):
                numWays[i][j] = int(not bool(numWays[i][j]))

        if numWays[-1][-1] == 0: return 0
        
        for i in range(ROWS-1,-1,-1):
            for j in range(COLS-1,-1,-1):
                if numWays[i][j] != 0:
                    if i+1 >= ROWS and j+1 < COLS:
                        numWays[i][j] = numWays[i][j+1]
                    elif j+1 >= COLS and i+1 < ROWS:
                        numWays[i][j] = numWays[i+1][j]
                    elif j+1 < COLS and i+1 < ROWS:
                        numWays[i][j] = numWays[i+1][j]+numWays[i][j+1]

        return numWays[0][0]
        