# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if not head or k == 0: return head
        # find list len of list
        
        curr = head
        length = 1
        
        while curr.next:
            curr = curr.next
            length += 1
        
        curr.next = head
        
        k= length - (k%length)
        
        while k > 0:
            curr = curr.next
            k -= 1
        new_head = curr.next
        curr.next = None
    
        
        return new_head
              
                
                
                
                
                
                
                
                
                
                
                