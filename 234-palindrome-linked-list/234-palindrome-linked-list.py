# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def reverse(self, node):
        
        
        prev = None
        curr = node
        
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            
        
        
        return prev
    
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        if not head: return True
        
        slow = fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        
        reverse_ll = self.reverse(slow)
        while reverse_ll:
            if reverse_ll.val != head.val:
                return False
            reverse_ll = reverse_ll.next
            head = head.next
        return True