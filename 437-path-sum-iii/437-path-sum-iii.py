# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        
        count = 0
        prefix = defaultdict(lambda: 0)
        prefix[0] = 1
        def dfs(node, curr_sum):
            nonlocal count
            
            if not node:
                return
            
            curr_sum = curr_sum + node.val
            # print(prefix)
            count += prefix[curr_sum - targetSum]
            
            prefix[curr_sum] += 1
            dfs(node.left, curr_sum)
            dfs(node.right, curr_sum)
            
            prefix[curr_sum] -=1
            
        
        dfs(root,0)
        # print(count, prefix)
        return count
    
#         count = 0
#         def dfs(node, total):
#             nonlocal count
#             if total == targetSum:
#                 count += 1           
#             if not node:
#                 return
#             # print(total)

#             dfs(node.left, total + node.val)
#             dfs(node.left, total)
            
#             dfs(node.right, total + node.val)
#             dfs(node.right, total)
            
            
#         dfs(root, 0)
#         return int(count/2) if count > 0 else 0
            
            
            
            
            
            
            
            