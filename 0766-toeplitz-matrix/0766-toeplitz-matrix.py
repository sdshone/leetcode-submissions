class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        
        M, N = len(matrix), len(matrix[0])
        i = j = 0
        while i<M and j<N:
            o = matrix[i][j]
            oi, oj = i, j 
            while i<M and j<N:

                if not matrix[i][j]==o:
                    return False
                i+=1
                j+=1
            i,j = oi, oj+1

        i = j = 0
        while i<M and j<N:
            o = matrix[i][j]
            oi, oj = i, j 
            while i<M and j<N:

                if not matrix[i][j]==o:
                    return False
                i+=1
                j+=1
            i,j = oi+1, oj
        return True