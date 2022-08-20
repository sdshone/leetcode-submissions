class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        
        i,j = 0,0
        maxSum = nums[0]
        currSum = 0
        
        for n in nums:
            if currSum < 0:
                currSum = 0
            currSum +=n
            maxSum = max(maxSum, currSum)
            
        return maxSum
            