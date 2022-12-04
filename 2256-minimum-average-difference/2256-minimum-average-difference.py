class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        
        prefix = [0]*len(nums)
        suffix = [0]*(len(nums)+1)
        
        for idx,num in enumerate(nums):
            prefix[idx] = num+ prefix[idx-1]
        for idx in range(len(nums)-1, -1, -1):
            suffix[idx] = nums[idx] + suffix[idx+1]
        res = float('inf')
        res_index = 0

        for i in range(len(nums)-1,-1,-1):

            if (len(nums) - i-1):
                v = abs(int(prefix[i]/(i+1)) - int(suffix[i+1]/(len(nums) - i-1)))
            else:
                v = int(prefix[i]/(i+1))
            res = min(res, v)

            if v==res:
                res_index = i

        return res_index