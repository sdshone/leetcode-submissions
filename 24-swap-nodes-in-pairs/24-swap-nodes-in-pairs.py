# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head: return
        root = head
        return_node = None
        prev = ListNode(0, root)
        while root and root.next:
            nxt = root.next
            temp = nxt.next
            root.next = temp
            nxt.next = root
            prev.next=nxt
            if not return_node:
                return_node = nxt
            prev = root
            root = temp
            
        return return_node if return_node else head