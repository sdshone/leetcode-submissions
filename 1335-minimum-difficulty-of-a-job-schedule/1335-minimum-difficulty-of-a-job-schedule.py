class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        
        J = len(jobDifficulty)
        if d>J:
            return -1
        memo={}
        # @lru_cache(None)
        def dfs(i,d):
            if (i,d) in memo: return memo[(i,d)]
            if d==0:
                if i==J: return 0
                else: return float('inf')
            if i==J: return float('inf')
           
            ans = float('inf')
            count_max = 0

            for idx in range(i, J):
                count_max = max(count_max, jobDifficulty[idx])
                ans = min(ans, count_max+ dfs(idx+1, d-1))
            memo[(i,d)] = ans
            return ans
        return dfs(0, d)