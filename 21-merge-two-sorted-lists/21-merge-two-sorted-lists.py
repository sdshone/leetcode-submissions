# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if not list1 and not list2: return None
        new_list_head = new_list = ListNode(0)
        while list1 and list2:
            if list1.val <= list2.val:
                min_v = list1.val
                list1=list1.next
            else:
                
                min_v = list2.val
                list2=list2.next

            new_list.val = min_v
            new_list.next = ListNode()
            if not new_list_head:
                new_list_head = new_list
            new_list = new_list.next
            
          
        
        while list1:
            new_list.val =list1.val
            if list1.next:
                new_list.next = ListNode()
                new_list = new_list.next
            list1=list1.next
        
        while list2:
            new_list.val =list2.val
            if list2.next:
                new_list.next = ListNode()
                new_list = new_list.next
            list2=list2.next
        
        return new_list_head