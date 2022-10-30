class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        
        # x, y, obstacles, steps
        q = deque([(0,0,k,0)])
        seen = set()
        
        while q:
            x, y, left, steps = q.popleft()
            if (x,y,left) in seen or left<0:
                continue
            if (x, y) == (m-1, n-1):
                return steps
            seen.add((x,y,left))
            if grid[x][y] == 1:
                left-=1
            for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
                new_x, new_y = x+dx, y+dy
                if 0<=new_x<m and 0<=new_y<n:
                    q.append((new_x, new_y, left, steps+1))
        return -1




# class Solution:
#     def shortestPath(self, grid: List[List[int]], k: int) -> int:
       
        
#         M, N = len(grid), len(grid[0])
    
#         q = deque([(0,0,k,0)])
#         visited = set()
        
#         while q:
#             i, j, left, count = q.popleft()
            
#             if (i,j, left) in visited or left<0 : continue
            
#             if i==M-1 and j==N-1: return count
    
#             for x, y in [(i+1,j), (i,j+1), (i-1,j), (i, j-1)]:
                
#                 if 0<=x<M and 0<=y<N and (left-grid[x][y])>=0:
#                     q.append((x,y,left-grid[x][y],count+1))

                    
#         return -1
    
    
    
#         M, N = len(grid), len(grid[0])
#         self.res = float('inf')

#         def dfs(path_total, i, j, k):
            


#             if i>=M or j>=N or i<0 or j<0: return
#             if i == M-1 and j == N-1:
#                 self.res = min(self.res, path_total)
#                 return     
#             if k == 0 and grid[i][j]==1:
#                 return
#             if grid[i][j]==2:
#                 return
#             if self.res == M+N-2:
#                 return
            
#             if grid[i][j]:
#                 k-=1
            
#             temp = grid[i][j]
#             grid[i][j] = 2
#             dfs(path_total+1, i+1, j, k)
#             dfs(path_total+1, i, j+1, k)
#             dfs(path_total+1, i-1, j, k)
#             dfs(path_total+1, i, j-1, k)

            
#             grid[i][j] = temp
        
#         dfs(0,0,0,k)
#         return -1 if self.res == float('inf') else self.res



            
    
    
    
    
    
    
    
    
    
    
    
    