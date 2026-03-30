# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        
        p1=head
        p2=head.next
        p3=p2.next

        p2.next = p1
        p1.next = None

        while p3:
            p1= p2
            p2= p3
            p3= p3.next
            p2.next = p1
        
        head = p2
        return head