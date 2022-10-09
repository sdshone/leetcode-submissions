class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        
        stack = []
        res = {}
        i=0
        while i< len(nums2):
            
            while stack and stack[-1] < nums2[i]:
                num = stack.pop()    
                res[num] = nums2[i]
                
                
            stack.append(nums2[i])
            i+=1
            
        return [res.get(n, -1) for n in nums1]