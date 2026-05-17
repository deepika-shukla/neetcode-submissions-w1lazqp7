# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return 
        
        # first divide the list in two parts using slow/fast pointer
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # now slow.next will be the head of second half
        head2 = slow.next
        # break second half
        slow.next = None

        # reverse the second half
        cur = head2 
        prev = None

        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        
        # new head of reverse second half - prev
        # now we will merge them
        c = head
        new = dummy = ListNode()
        while c and prev:
            new.next = c
            c = c.next
            new = new.next
            new.next = prev
            prev = prev.next
            new = new.next
        
        if c:
            new.next = c
        if prev:
            new.next = prev
        



