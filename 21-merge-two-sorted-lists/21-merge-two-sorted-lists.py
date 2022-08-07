# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if not list1: return list2
        if not list2: return list1

        return_node = newlist =  ListNode(0)
        
        
        while list1 and list2:
            if list1.val <= list2.val:
                min_val=list1.val
                list1 = list1.next
            else:
                min_val=list2.val
                list2 = list2.next
            newlist.val=min_val
            newlist.next = ListNode()
            newlist=newlist.next
        
        while list1:
            newlist.val = list1.val
            list1 = list1.next
            if list1:
                newlist.next=ListNode()
                newlist = newlist.next
        
        while list2:
            newlist.val = list2.val
            list2 = list2.next
            if list2:
                newlist.next=ListNode()
                newlist = newlist.next
        
        
        return return_node