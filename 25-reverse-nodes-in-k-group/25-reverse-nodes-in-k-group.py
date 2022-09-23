# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # 1 2 3 4
    # 2 1 3 4
    def reverse(self, node):
        curr = head = node
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            
            prev = curr
            curr = temp
           
        # print(head, prev)
        return head, prev
        
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
 
        if k == 1: return head
        H = ListNode(0, head)
        khead = head
        parent = H
        while khead:
            count = 1
            node = khead
            while count < k and node:
                node = node.next
                count+=1
            if count < k or not node: break
                
            rest = node.next
            node.next = None
            tail, head = self.reverse(khead)
            
            parent.next = head
            tail.next = rest
            
            parent = tail
            khead = rest
            
        return H.next
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            