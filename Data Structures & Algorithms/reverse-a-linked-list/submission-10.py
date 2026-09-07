# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # /////// ITERATIVE
        # if not head:
        #     return head
        
        # prev, nextt = None, head

        # while nextt:
        #     temp = nextt.next
        #     nextt.next = prev
        #     prev = nextt
        #     nextt = temp
        # return prev


        # ////////// RECUSRIVE
        if not head:
            return None
        
        newhead = head
        if head.next:
            newhead = self.reverseList(head.next)
            head.next.next = head # my next should point to me
        head.next = None # i should point to None if i am last node

        return newhead
        
