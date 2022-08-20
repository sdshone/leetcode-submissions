# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        
        maxSum = 0
        
        slow = fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        if fast == slow.next:
            return head.val + slow.val
        first = head
        second = self.reverseList(slow)
        
        while second:
            twoSum = first.val + second.val
            maxSum = max(maxSum, twoSum)
            first = first.next
            second = second.next
        return maxSum
        
    def reverseList(self, rlist):
        
        prev = None
        curr = rlist
        
        while curr:
            
            nxt = curr.next
            curr.next = prev
            
            prev = curr
            curr = nxt
        return prev
            
            
            
            
            
            
            
            
            
            
            
            
            
            