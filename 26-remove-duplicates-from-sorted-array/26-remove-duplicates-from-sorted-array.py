class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        if not nums: return 0
        i, j = 0,0
        N = len(nums)
        
        while j < N:
            curr = j
            while j < N and i < N and nums[curr] == nums[j]:
                j+=1
            j-=1
            nums[i] = nums[j]
            j+=1
            i+=1
            # print(i,j)
            # print(nums)
        
        return i