class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        nonzeroidx = 0
        N=len(nums)
        
        for i in range(N):
            if nums[i]!=0:
                nums[nonzeroidx]=nums[i]
                nonzeroidx+=1
        # print(nums)
        
        for i in range(nonzeroidx,N):
            nums[i]=0
        return nums