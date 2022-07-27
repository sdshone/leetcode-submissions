class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top = 0
        bottom = len(matrix) - 1
        
        while top <= bottom:
            mid = (top + bottom)// 2
            if matrix[mid][-1] < target:
                top = mid + 1
            elif matrix[mid][0] > target:
                bottom = mid - 1
            else:
                break
        if top <= bottom:
            left, right = 0, len(matrix[0])
            while left <= right:
                row_mid = (left + right) // 2
                if matrix[mid][row_mid] < target:
                    left = row_mid + 1
                elif matrix[mid][row_mid] > target:
                    right = row_mid - 1
                else:
                    return True
        return False