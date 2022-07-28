# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # if not head: return None
        # prev, curr = None, head
        # _next = head.next
        # while curr:
        #     nxt = curr.next
        #     curr.next = prev
        #     prev = curr
        #     curr = nxt
        # return prev
        
        # Recursive
        
        if not head: return None
        
        new_head = head
        if head.next:
            new_head = self.reverseList(head.next)
            head.next.next = head
        head.next = None
        
        return new_head