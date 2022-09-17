class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # "1,3,2" ->  "2,1,3"
        first, second = -1, -1
        for i in range(len(nums)-2, -1, -1):
            if nums[i] < nums[i+1]:
                first = i
                print(i)
                break
        if first != -1:
            for i in range(len(nums)-1, -1, -1):
                if nums[i] > nums[first]:
                    second = i
                    print(i)
                    break
            if second != -1:
                nums[first], nums[second] = nums[second], nums[first]
            
        nums[first+1:] = nums[first+1:][::-1]