# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #we have to reverse the linked list, therefore we need to break link
        # from next node and make a link to previous node

        if not head or not head.next:
            #if not linked list or only with 1 node
            return head

        p1 = head
        p2 = head.next
        p3 = p2.next
        
        #first node will become last poiniting to None
        # second will point to first
        p2.next = p1
        p1.next = None

        #now check till we reach last node and change the links
        while p3:
            p1 = p2
            p2 = p3
            p3 = p3.next
            p2.next = p1
        
        #new head will be p2
        return p2