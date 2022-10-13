class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        N = len(nums)
        res = []
        def dfs(i, arr):
            
            if i >=N:
                
                for r in res:
                    if r==arr:
                        break
                else:
                    res.append(arr)
                return
            
            take = dfs(i+1, arr+[nums[i]])
            not_take = dfs(i+1, arr)
        
        dfs(0,[])
        return res
            
            