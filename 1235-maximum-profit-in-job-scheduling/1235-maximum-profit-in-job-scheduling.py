class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        
        
        # step 1 sort the data based on start time
        
        jobs = sorted(zip(startTime ,endTime ,profit))
        
        def binarySearch(nums: List[int], target) -> int:
            
            l, r = 0, len(nums)
            while l < r:
                m = (l+r) // 2
                if nums[m][0] < target:
                    l = m + 1
                else:
                    r = m
            # l = l if l< len(nums) else len(nums)-1
            # print(l,r, target)
            if l >= len(nums): return None
            return nums[l-1][0] 
        
        @lru_cache(None)
        def dfs(i):
            if i >= len(jobs) : return 0
            # k = binarySearch(jobs, jobs[i][1])
            k = bisect_left(jobs, jobs[i][1], key = lambda x: x[0])
            x = dfs(k) if k is not None else 0
            return max(dfs(i+1), jobs[i][2] + x)
    
        return dfs(0)