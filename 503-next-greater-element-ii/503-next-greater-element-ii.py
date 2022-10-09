class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        
        stack = []
        res = [-1]*len(nums)
        
        for _ in range(2):
            for i in range(len(nums)):
                
                while stack and nums[stack[-1]] < nums[i]:
                    idx=stack.pop()
                    res[idx]=nums[i]
                
                stack.append(i)
            # print(res, stack)
        return res