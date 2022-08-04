class Solution:
    def canJump(self, nums: List[int]) -> bool:
        last_index = len(nums)-1
        results = {}
#         def dfs(index):
#             if index == last_index:
#                 return True
#             if results.get(index) is not None and results.get(index):
#                 return True
#             if nums[index] == 0 or index > last_index:
#                 results[index] = False
#                 return False
                

#             for new_index in range(1, nums[index]+1):
#                 if dfs(new_index+index): 
#                     results[index] = True
#                     return True
#             results[index] = False
#             return False
#         return dfs(0)

    
    
        for i in range(last_index,-1,-1):
            if nums[i] + i >= last_index:
                last_index = i
        return not last_index
                    
            
            
            
            
            
            
            
            
            
            