class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        
        first, second = nums[0], nums[nums[0]]
        
        while first != second:
            first = nums[first]
            second = nums[nums[second]]
            
        second = nums[0]
        first = nums[first]
        while first != second:
            first = nums[first]
            second = nums[second]
        
        # print(first, second)
        
        return second