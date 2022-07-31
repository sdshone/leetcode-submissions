class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        if not grid: return 0
        island_count = 0
        visited = set()
        rows = len(grid)
        cols = len(grid[0])
        
        
        def bfs(r,c):
            q = collections.deque()
            
            visited.add((r,c))
            q.append((r,c))
            while q:
                row, col = q.popleft()
                drs = [[0,1], [0,-1], [1,0], [-1,0]]
                for dr, dc in drs:
                    r, c = row+dr, col+dc
                    if r in range(rows) and \
                       c in range(cols) and \
                       (r,c) not in visited and \
                       grid[r][c] == '1':
                        q.append((r,c))
                        visited.add((r,c))
                    
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r,c) not in visited:
                    bfs(r,c)
                    island_count += 1
        return island_count