class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        
        count = len(matrix) * len(matrix[0])
        res = []
        i = j = 0
        d = [0,1]
        
        while len(res) < count:
            
            res.append(matrix[i][j])
            matrix[i][j]=120
            
            ni, nj = i+d[0], j+d[1]
            
            if 0<=ni<len(matrix) and 0<=nj<len(matrix[0]) and matrix[ni][nj]!=120:
                i,j = ni,nj
            else:
                d[0], d[1] = d[1], -d[0]
                i,j = i+d[0], j+d[1]
                
        return res