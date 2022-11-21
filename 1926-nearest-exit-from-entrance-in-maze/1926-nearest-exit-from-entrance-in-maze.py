class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        
        ROWS, COLS = len(maze), len(maze[0])
        dirs = ((1,0), (-1,0), (0,1), (0,-1))
        
        start_row, start_col = entrance
        maze[start_row][start_col] = '+'
        
        q = collections.deque()
        q.append([start_row, start_col, 0])
        
        while q:
            curr_row, curr_col, curr_distance = q.popleft()
            for d in dirs:
                next_row = curr_row + d[0]
                next_col = curr_col + d[1]
                
                if 0<=next_row<ROWS and 0<=next_col<COLS \
                and maze[next_row][next_col] == '.':
                    if next_row in [0, ROWS-1] or \
                    next_col in [0, COLS-1]:
                        return curr_distance + 1
                    maze[next_row][next_col] = '+'
                    q.append([next_row, next_col, curr_distance+1])
        return -1