class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []
        def dfs(i, target,  comb):
            if target == 0:
                res.append(list(comb))
                return

            for nxt in range(i, len(candidates)):
                if nxt>i and candidates[nxt] == candidates[nxt-1]:
                    continue
                pick = candidates[nxt]
                if target - pick < 0:
                    break
                comb.append(pick)
                dfs(nxt+1, target-pick, comb)
                comb.pop()
       
        candidates.sort()
        dfs(0, target, [])
        return res

# class Solution:
#     def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

#         def backtrack(comb, remain, curr, results):

#             if remain == 0:
#                 # make a deep copy of the resulted combination
#                 results.append(list(comb))
#                 return

#             for next_curr in range(curr, len(candidates)):

#                 if next_curr > curr \
#                   and candidates[next_curr] == candidates[next_curr-1]:
#                     continue
    
#                 pick = candidates[next_curr]
#                 # optimization: skip the rest of elements starting from 'curr' index    
#                 print(comb)
#                 if remain - pick < 0:
#                     break

#                 comb.append(pick)
#                 backtrack(comb, remain - pick, next_curr + 1, results)
#                 comb.pop()

#         candidates.sort()

#         comb, results = [], []
#         backtrack(comb, target, 0, results)

#         return results