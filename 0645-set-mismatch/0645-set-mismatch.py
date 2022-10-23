class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        
        
        
        
        N=len(nums)
        seen = set([i for i in range(1,N+1)])
        repeat, missing = -1, N
        for i in range(N):
            if nums[i] not in seen:
                repeat = nums[i]
            else:
                seen.remove(nums[i])
        missing = seen.pop() if seen else missing
        return repeat, missing