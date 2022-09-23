class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        N = len(nums)
        res = []
        nums.sort()
        res_set = set()
        def dfs(idx, sol):
            
            if idx >= N:
                stra = ''.join(str(sol))
                if stra not in res_set:
                    res_set.add(stra)
                    res.append(sol)
                return
            # while idx+1< N and nums[idx+1] == nums[idx]:
            #     idx+=1
                
            take = dfs(idx+1, sol + [nums[idx]])
            not_take = dfs(idx+1, sol)
            
        
        dfs(0, [])
        # print(res)
        # res.sort()
        return res