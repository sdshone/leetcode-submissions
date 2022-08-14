class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        
        def bfs(r,c):
            if (r,c) in visited:
                return
            visited.add(tuple([r,c]))

            q = collections.deque(tuple([r,c]))
            
            while q:
                r= q.popleft()
                c=q.popleft()
                if r+1 <ROWS and (r+1, c) not in visited and grid[r+1][c]=='1': 
                    q.extend([r+1,c])
                    visited.add(tuple([r+1,c]))
                if r-1 >=0 and (r-1, c) not in visited and grid[r-1][c]=='1': 
                    q.extend([r-1,c])
                    visited.add(tuple([r-1,c]))
                if c+1 <COLS and (r, c+1) not in visited and grid[r][c+1]=='1': 
                    q.extend([r,c+1])
                    visited.add(tuple([r,c+1]))
                if c-1 >=0 and (r, c-1) not in visited and grid[r][c-1]=='1': 
                    q.extend([r,c-1])
                    visited.add(tuple([r,c-1]))
                
        
        islands = 0
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) not in visited and grid[r][c]=='1':
                    bfs(r,c)
                    islands+=1

        return islands