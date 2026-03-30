# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        ############## RECUSRIVE ################33
        # # edge case
        # # if list is empty
        # if not head:
        #     return head
        
        # # if both pointer are equal
        # if left == right:
        #     return head

        # # break the linked list
        # # it could be anywhere
        # find = head
        # f1, f2 = False, False
        # index = 1
        # while find:
        #     if index == left:
        #         if not f1:
        #             last1 = find
        #         f1 = True
        #     if index == right:
        #         if not f2:
        #             last2 = find
        #         f2 = True
        #     if f1 and f2:
        #         break
        #     find = find.next
        #     index += 1
        
        # reverse_start = last1
        # reverse_end = last2.next # store the right portion

        # last2.next = None # break the list, to reverse the part

        # # reverse the part
        # prev = None
        # cur = reverse_start

        # while cur:
        #     temp = cur.next
        #     cur.next = prev
        #     prev = cur
        #     cur = temp
        # new_head =  prev # head of reverse list

        # # now we have to combine with head
        # # start from head connect left potion
        # if head != reverse_start:
        #     s = head
        #     while s.next != reverse_start:
        #         s = s.next
        #     s.next = new_head
        # else:
        #     head = new_head   # fix for left == 1


        # # combine right portion
        # reverse_start.next =  reverse_end

        # return head


        ########## ITERATIVE ###################

        # we can divide the problem into three section
        # first is finding the left and right
        # Second reversing the section
        # Third is combining the complete linked list

        # Now to deal with edge cases like reverse from beginning, we
        # can have a dummy node
        dummy = ListNode(0, head)

        # now we have to find the 
        leftprev, cur = dummy, head

        for i in range(left-1):
            leftprev, cur = cur, cur.next
        
        # now leftprev will reach the node before the node reverse start
        # cur will start of the group to reverse
        # now reverse the group
        prev = None

        for i in range(right-left+1):
            tempnext = cur.next
            cur.next = prev
            prev, cur = cur, tempnext
        
        # now we need to combine the reverse group
        # leftprev will be poiniting to the last of reverse group
        # and we want the last to connect with our remaning linked list
        # which will be cur
        leftprev.next.next = cur

        # and leftprev should point to start of reverse group, which will
        # be stored in prev
        leftprev.next = prev

        # now return the next of dummy node
        return dummy.next 
         
                
