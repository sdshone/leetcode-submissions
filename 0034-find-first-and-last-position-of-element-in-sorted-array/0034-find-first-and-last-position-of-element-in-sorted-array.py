class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        if not nums: return [-1,-1]
        i,j = 0, len(nums)-1
        
        while i <= j:
            mid = (i+j)//2

            if nums[mid] == target:
                break
            elif nums[mid] < target:
                i = mid+1
            else:
                j = mid-1
        
        if nums[mid]==target:
            s = e = mid
            while s>=0 and nums[s]==target:
                s-=1
            while e<len(nums) and nums[e]==target:
                e+=1
            return [s+1,e-1]
        else: return [-1,-1]