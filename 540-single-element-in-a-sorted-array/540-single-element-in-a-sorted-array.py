class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        
        
        
        def dfs(nums):
            N=len(nums)
            if N==1:
                return nums[0]
            
            mid = N//2

            if nums[mid] == nums[mid-1]:
                if mid%2!=0:
                    x=dfs(nums[mid+1:])
                else:
                    x=dfs(nums[:mid-1])
            elif(nums[mid] == nums[mid+1]):
                if mid%2==0:
                    x=dfs(nums[mid+2:])
                else:
                    x=dfs(nums[:mid])
            else: x= nums[mid]
            
            return x
    
        return dfs(nums)