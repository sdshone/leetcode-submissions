class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        left, right = 0, len(nums) - 1
        min_nums = 5000
        while left <= right:
            
            mid = (left + right) // 2
            print(mid)
            if nums[mid] >= nums[left]:
                min_nums = min(min_nums, nums[left])
                left = mid + 1
            
            else:
                min_nums = min(min_nums, nums[mid])
                right = mid - 1
        return min_nums