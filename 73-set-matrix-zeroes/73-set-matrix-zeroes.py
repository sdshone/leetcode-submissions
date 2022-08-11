class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        ROWS, COLS = len(matrix), len(matrix[0])
        zeros_row = set()
        zeros_col = set()
        for row in range(ROWS):
            for col in range(COLS):
                if matrix[row][col] == 0:
                    zeros_row.add(row)
                    zeros_col.add(col)
        
        for row in range(ROWS):
            for col in range(COLS):
                if row in zeros_row or col in zeros_col:
                    matrix[row][col] = 0
                
                