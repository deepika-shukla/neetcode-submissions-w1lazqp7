# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head is None or head.next is None:
            return head
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        head2 = slow.next
        slow.next = None
 
        if head2.next:
            p1 = head2
            p2 = head2.next
            p3 = p2.next

            p2.next = p1
            p1.next = None

            while p3:
                p1 = p2
                p2 = p3
                p3 = p3.next
                p2.next = p1
            head2 = p2
            

        first, second = head, head2
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2