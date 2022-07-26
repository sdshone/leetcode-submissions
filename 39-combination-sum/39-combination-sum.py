class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []
        def dfs(i, curr, total):
            
            if total == target:
                res.append(curr.copy())
                return
            
            if total > target or i >= len(candidates):
                return
            
            dfs(i, curr + [candidates[i]], total + candidates[i])
            dfs(i + 1, curr, total)
        
        dfs(0, [], 0)
        return res