class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        
        nums.sort()
        i = 0
        N = len(nums)
        while i <  N:
            if nums[i] == val:
                curr = i
                while curr < N and nums[curr] == val:
                    curr +=1
                if curr == N: return i
                while i < curr and curr < N:
                    nums[i] = nums[curr]
                    i+=1
                    curr+=1
                return i
            i +=1
        return N
                