# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # we will divide the list in two halves
        # then we will reverse the last half
        # and combine both list

        n1 = head

        slow, fast = n1, n1

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        n2 = slow.next
        #break the list
        slow.next = None

        # revser n2
        curr, prev = n2, None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        n2 = prev

        new = dummy = ListNode()
        while n1 and n2:
            dummy.next = n1
            n1 = n1.next
            dummy = dummy.next
            dummy.next = n2
            n2 = n2.next
            dummy = dummy.next
        if n1:
            dummy.next = n1
        if n2:
            dummy.next = n2
        head = new.next
        
        