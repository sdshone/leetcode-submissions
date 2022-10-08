class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        sol=[]
        def dfs(queens ,diag1, diag2):
            p=len(queens)
            if p==n:
                sol.append(queens)
                return
            
            for q in range(n):
                if q not in queens and p-q not in diag1 and p+q not in diag2:
                    dfs(queens+[q], diag1+[p-q], diag2+[p+q])
            
            
            
        
        dfs([],[],[])
        # print(sol)
        
        return [['.'*i+'Q'+'.'*(n-i-1) for i in s] for s in sol]
        
        
#         res = set()
#         def dfs(i,j,res):
#             if i>n or j>n:
#                 return
#             if len(res)==n:
#                 sol.append(list(res))
#             diag1 = i-j
#             diag2 = j+i
#             safe=True
#             for x,y in res:
#                 if i==x or j==y or x-y==diag1 or y+x==diag2:
#                     safe=False
#             if not safe: return
#             res.add((i,j))
#             for z in range(n):
#                 dfs(i+1,z, res)
#             res.remove((i,j))
            
#         sol=[]
#         for i in range(n):
#             dfs(0,i,set())
#             print(res)
#             if len(res)==n:
#                 sol.append(list(res))

#             res=set()
#         new_sol =[]
#         for s in sol:
#             board=[['.' for _ in range(n)] for _ in range(n)]
#             for x,y in s:
#                 board[x][y]='Q'
#                 board[x] = ''.join(board[x])
#                 print(board[x])
                
#             new_sol.append(board)
#         return new_sol
        
                
                # 00 01 02 
                # 10 11 12
                # 20 21 22