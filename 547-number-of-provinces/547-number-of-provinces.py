class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        ROWS, COLS = len(isConnected), len(isConnected)
        
        def dfs(row):
            visited.add(row)
            for col in range(COLS):
                if isConnected[row][col] == 1 and col not in visited:
                    dfs(col)
            
        visited  = set()
        number_of_provinces = 0
        for row in range(ROWS):
            if row not in visited:
                number_of_provinces += 1
                dfs(row)
            
        return number_of_provinces