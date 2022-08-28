class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:

        diag = defaultdict(list)
        ROWS, COLS = len(mat), len(mat[0])
        for i in range(ROWS):
            for j in range(COLS):
                diag[i-j].append(mat[i][j])
        
        for k in diag:
            diag[k].sort(reverse=True)
        
        for i in range(ROWS):
            for j in range(COLS):
                mat[i][j] = diag[i-j].pop()
        
        return mat
        