# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        
        if not lists: return
        
        amount = len(lists)
        interval = 1
        while interval < amount:
            for i in range(0, amount-interval, interval*2):
                lists[i] = self.merge2Lists(lists[i], lists[i+interval])
            interval *=2
        return lists[0]
        
        
    def merge2Lists(self, l1, l2):
        
        head = point = ListNode(0)
        
        while l1 and l2:
            if l1.val <= l2.val:
                point.next = l1
                l1 = l1.next
            else:
                point.next = l2
                l2 = l1
                l1 = point.next.next
            point = point.next
        if l1:
            point.next = l1
        else:
            point.next = l2
        return head.next