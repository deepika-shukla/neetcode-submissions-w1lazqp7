# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = node = head

        while node.next:
            d = self.getDivisor(node, node.next)
            print(d)
            new = ListNode(d)
            temp = node.next
            node.next = new
            new.next = temp
            node = new.next

        return dummy
    
    def getDivisor(self, n1, n2):
        if n1.val % n2.val == 0:
            return n2.val
        if n2.val % n1.val == 0:
            return n1.val
        for i in range(max(n1.val, n2.val),1,-1):
            if n1.val % i == 0 and n2.val % i == 0:
                return i

        return 1

        
