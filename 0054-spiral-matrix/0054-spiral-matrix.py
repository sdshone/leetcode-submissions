class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        M, N = len(matrix), len(matrix[0])
        count = M* N
        res = []
        i = j = 0
        d = [0,1]
        
        while len(res) < count:
            
            res.append(matrix[i][j])
            matrix[i][j]=120
            
            ni, nj = i+d[0], j+d[1]
            
            if 0<=ni<M and 0<=nj<N and matrix[ni][nj]!=120:
                i,j = ni,nj
            else:
                d[0], d[1] = d[1], -d[0]
                i,j = i+d[0], j+d[1]
                
        return res