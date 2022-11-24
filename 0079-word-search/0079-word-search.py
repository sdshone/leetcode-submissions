class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        
        def dfs(i, r, c, sol):

            if i == len(word):
                return True
            if r<0 or r >= len(board) or c<0 or c >= len(board[0]) or (r,c) in sol:
                return False

            
            if board[r][c] == word[i]:
                sol.add((r,c))
                res = (dfs(i+1, r+1,c, sol) or
                dfs(i+1, r,c+1, sol) or
                dfs(i+1, r-1,c, sol) or
                dfs(i+1, r,c-1, sol))
                sol.remove((r,c))
                return res
                
            return False
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == word[0] and dfs(0, r, c, set()):
                    return True
        return False