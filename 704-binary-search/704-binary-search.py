class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        
        i, j = 0, len(nums) - 1
        
        while i <= j:
            mid = (i+j)//2
            print(i,j,mid)
            if nums[mid] < target:
                i = mid+1
            elif nums[mid] > target:
                j = mid-1
            else: # found the match
                return mid
        return -1