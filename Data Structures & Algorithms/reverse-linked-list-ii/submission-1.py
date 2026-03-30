# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # edge case
        # if list is empty
        if not head:
            return head
        
        # if both pointer are equal
        if left == right:
            return head

        # break the linked list
        # it could be anywhere
        find = head
        f1, f2 = False, False
        index = 1
        while find:
            if index == left:
                if not f1:
                    last1 = find
                f1 = True
            if index == right:
                if not f2:
                    last2 = find
                f2 = True
            if f1 and f2:
                break
            find = find.next
            index += 1
        
        reverse_start = last1
        reverse_end = last2.next # store the right portion

        last2.next = None # break the list, to reverse the part

        # reverse the part
        prev = None
        cur = reverse_start

        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        new_head =  prev # head of reverse list

        # now we have to combine with head
        # start from head connect left potion
        if head != reverse_start:
            s = head
            while s.next != reverse_start:
                s = s.next
            s.next = new_head
        else:
            head = new_head   # fix for left == 1


        # combine right portion
        reverse_start.next =  reverse_end

        return head

         
                
