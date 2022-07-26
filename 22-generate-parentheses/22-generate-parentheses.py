class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result=[]
        def backtrack(s, opened, closed):
            if len(s) == 2*n:
                result.append(s)
                return
            
            if opened < n:
                backtrack(f'{s}(', opened+1,closed)
            if closed < opened:
                backtrack(f'{s})',opened,closed+1)
        backtrack('',0,0)
        return result