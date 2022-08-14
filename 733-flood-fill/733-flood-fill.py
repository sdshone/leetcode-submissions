class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        ROWS, COLS = len(image), len(image[0])
        
        src_color = image[sr][sc]
        done = set()
        def dfs(r,c): 
            if (r,c) in done or r < 0 or c < 0 or r >= ROWS or c >= COLS or image[r][c]!=src_color:
                return
            

            done.add(tuple([r,c]))
            image[r][c] = color
            for row, col in [(r+1,c), (r-1,c), (r,c+1), (r,c-1)]:
                dfs(row, col)

        dfs(sr,sc)
        return image