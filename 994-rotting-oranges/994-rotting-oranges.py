class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        
        ROWS, COLS = len(grid), len(grid[0])
        dp = [ [1000]*COLS for i in range(ROWS)]
        visited = set()
#         def dfs(i, j, mins):
#             print(mins)
#             if (i,j) in visited:
#                 return
#             visited.add((i,j))
#             if grid[i][j] == 0:
#                 return
#             # if grid[i][j] == 2:
#             #     # dp[i][j]=0
#             #     return
#             # if grid[i][j] == 1:
#             dp[i][j] = min(dp[i][j], mins+1)

#             if i+1 in range(ROWS):
#                 dfs(i+1, j, mins+1)
#             if i-1 in range(ROWS):
#                 dfs(i-1, j, mins+1)
#             if j+1 in range(COLS):
#                 dfs(i, j+1, mins+1)
#             if j-1 in range(COLS):
#                 dfs(i, j-1, mins+1)
            
        q = collections.deque()
        def bfs(i,j,mins):
            
            # if (i,j) in visited:
            #     return
            # visited.add((i,j))
            q = collections.deque()
            q.append((i,j))
            visited = set()
            while q:
                
                for z in range(len(q)):
                    # print(f'z: {z}')
                    i,j = q.popleft()
                    if (i,j) in visited:
                        continue
                    # j = q.popleft()
                    visited.add((i,j))

                    dp[i][j] = min(dp[i][j], mins)
                    if i+1 in range(ROWS) and grid[i+1][j]==1 and (i+1,j) not in visited:

                        q.append((i+1, j))
                    if i-1 in range(ROWS) and grid[i-1][j]==1 and (i-1,j) not in visited:
                        q.append((i-1, j))
                    if j+1 in range(COLS) and grid[i][j+1]==1 and (i,j+1) not in visited:
                        q.append((i, j+1))

                    if j-1 in range(COLS) and grid[i][j-1]==1 and (i,j-1) not in visited:
                        q.append((i, j-1))

                mins+=1
            
            
            
            
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 2:
                    bfs(i, j, 0)
        
        max_count = 0
        for i in range(ROWS):
            for j in range(COLS):
                if dp[i][j]==1000 and grid[i][j]==1:
                    return -1
                elif dp[i][j]!=1000:
                    max_count = max(max_count,dp[i][j])
                    
        
        return max_count