class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        
        
        if start == end:
            return 0
        if not bank or end not in bank:
            return -1
        
        def diff(s, e):
            count = 0
            for i in range(8):
                if s[i] != e[i]:
                    count+=1
            return count
        
        def dfs(curr, bank, steps):
            
            if curr == end:
                return steps
            if not bank or steps>10:
                return -1
            res = float('inf')
            for idx in range(len(bank)):
                if diff(curr, bank[idx])==1:
                    new_curr = bank.pop(idx)
                    res = min(res, dfs(new_curr, bank, steps+1))
                    bank.append(new_curr)
            return res
    
        ans = dfs(start, bank, 0)
        return ans if ans !=float('inf') else -1