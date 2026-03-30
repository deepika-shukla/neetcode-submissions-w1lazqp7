# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # create a new list
        new = dummy = ListNode()

        #take two pointer for 2 sorted list
        l1, l2 = list1, list2

        #now traverse both link until we reach end for one
        while l1 and l2:
            #check for the value
            if l1.val < l2.val:
                dummy.next = ListNode(l1.val)
                l1 = l1.next
            else:
                dummy.next = ListNode(l2.val)
                l2 = l2.next
            dummy = dummy.next
        
        if l1:
            dummy.next = l1
        if l2:
            dummy.next = l2
        return new.next