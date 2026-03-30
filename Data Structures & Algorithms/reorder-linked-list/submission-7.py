# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverse(self, head):
        prev = None
        second = head

        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        
        return prev


    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        head2 = slow.next
        cur = head
        slow.next = None

        new_reversed = self.reverse(head2)

        t = dummy = ListNode()

        while cur and new_reversed:
            dummy.next = cur
            cur = cur.next
            dummy = dummy.next
            dummy.next = new_reversed
            dummy = dummy.next
            new_reversed = new_reversed.next
        
        if cur:
            dummy.next = cur
        if new_reversed:
            dummy.next = new_reversed
        
        head = t.next



        