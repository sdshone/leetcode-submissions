class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        
        row, col = 0, len(matrix[0])-1
        
        while 0<=row<len(matrix) and 0<=col<len(matrix[0]):
            
            value = matrix[row][col]
            # print(row, col, value)
            if target < value:
                col -= 1
            elif target > value:
                row += 1
            else:
                return True
            
        return False