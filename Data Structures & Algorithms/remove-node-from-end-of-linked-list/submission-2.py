# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], end: int) -> Optional[ListNode]:
        #edge cases
        if head is None:
            return head
        
        count = 0
        n = head
        while n:
            n = n.next
            count += 1
        
        if count == end:
            head = head.next
            return head
        
        curr = 1
        temp = head
        while temp:
            if curr == (count - end):
                temp.next = temp.next.next
                return head
            temp = temp.next
            curr += 1
        return head

        

