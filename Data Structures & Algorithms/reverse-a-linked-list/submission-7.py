# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p3 = None
        p1 = head
        if not head or not head.next:
            return head
        p2 = head.next

        if p2.next:
            p3 = p2.next
        
        p2.next = p1
        p1.next = None

        while p3:
            p1 = p2
            p2 = p3
            p3 = p3.next
            p2.next = p1
        
        head = p2
        return head

        if not head or not head.next:
            return head
        cur = head
        next = head.next
        cur.next = None

        while next:
            temp = next.next
            next.next = cur
            cur = next
            next = temp 
        return cur
