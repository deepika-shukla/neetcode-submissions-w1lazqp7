# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # head of both list are one's position
        # addition will start from here

        #new list with sum
        new = ListNode()
        #copy the head of new list
        head = new

        #initialize carry
        carry = 0

        while l1 or l2 or carry:
            if l1:
                v1 = l1.val
            else:
                v1 = 0

            v2 = l2.val if l2 else 0

            val = v1 + v2 + carry
            carry = val // 10
            val = val % 10
            head.next = ListNode(val)

            head = head.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        return new.next



        