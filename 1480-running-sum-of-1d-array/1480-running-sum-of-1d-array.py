class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        
        # running_sum = [nums[0]]*len(nums)
        # for index in range(1,len(nums)):
        #     running_sum[index] = running_sum[index - 1] + nums[index]
        running_sum = [nums[0]]
        for index in range(1,len(nums)):
            running_sum.append(running_sum[index - 1] + nums[index])
        return running_sum