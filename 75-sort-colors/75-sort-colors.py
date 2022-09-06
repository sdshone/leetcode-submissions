class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def swap(i,j):
            nums[i], nums[j] = nums[j], nums[i]
            
        red, blue = 0, len(nums)-1
        i=0
        while i <(len(nums)):
            
            if nums[i] == 2 and i < blue:
                swap(i, blue)
                blue -=1
                i-=1
            elif nums[i] == 0 and i > red:
                swap(i, red)
                red +=1
                i-=1
            i+=1
            # print(nums)
            