# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        
        # nodes = set()
        # while headA or headB:
        #     # print(headA.val)
        #     # print(headB in nodes)
        #     if headA == headB:
        #         return headA
        #     if headA in nodes:
        #         return headA
        #     elif headB in nodes:
        #         return headB
        #     if headA:
        #         nodes.add(headA)
        #         headA = headA.next
        #     if headB:
        #         nodes.add(headB)
        #         headB = headB.next
        
        refA = headA
        refB = headB
        count = 0
        while refA != refB:
            refA = refA.next
            refB = refB.next  
            if refA is None:
                count+=1
                if count == 2:
                    return
                refA = headB
            if refB is None:
                refB = headA

        return refA
                
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            