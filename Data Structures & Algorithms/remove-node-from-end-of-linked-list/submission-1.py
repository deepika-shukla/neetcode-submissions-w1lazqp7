# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], end: int) -> Optional[ListNode]:
        # edge cases
        if head.next is None:
            head = None
            return
        
        if head.next.next is None:
            if end == 2:
                head = head.next
                return head
            else:
                head.next = None
                return head
        count = 0
        n = head
        while n is not None:
            n = n.next
            count  += 1
        print(count)

        # edge case
        if count == end:
            head = head.next
            return head

        temp = 0
        h1 = head
        while True:
            temp += 1
            if temp == (count - end):
                h1.next = h1.next.next
                return head
            h1 = h1.next
