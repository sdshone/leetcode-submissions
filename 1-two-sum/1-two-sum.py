class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        value_index = {}
        
        for idx, num in enumerate(nums):
            
            if (target - num) in value_index:
                return [value_index[(target - num)], idx]
        
            value_index[num] = idx
        
            
            