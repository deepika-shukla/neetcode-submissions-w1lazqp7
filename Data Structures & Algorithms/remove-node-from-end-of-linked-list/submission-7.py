# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # two iteration approach

        # edge cases, when linked list is empty, when only one node
        if not head:
            return []
        
        # count nodes 
        nodes = 0
        cur = head
        while cur:
            cur = cur.next
            nodes += 1
        
        # first node deletion
        if nodes - n == 0:
            return head.next
        
        cur2 = head
        pos = 0
        while cur2.next:
            pos += 1
            if pos == (nodes - n):
                cur2.next = cur2.next.next
                return head
            cur2 = cur2.next
        return head


        
        
