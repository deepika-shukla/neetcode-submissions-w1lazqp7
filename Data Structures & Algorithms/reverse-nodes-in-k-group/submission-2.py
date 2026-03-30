# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverse(self, head):
        p1 =head
        p2 = p1.next
        p3 = p2.next

        p2.next = p1
        p1.next = None

        while p3 is not None:
            p1 = p2
            p2= p3
            p3 = p3.next
            p2.next = p1
        return p2

    def print_l(self, head):
        if head is None:
            print("linked list is empty, my friend")
            return
        n = head
        while n is not None:
            print(n.val," --> ", end=" ")
            n = n.next

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1:
            return head
        rev = dummy = ListNode()
        curr = head
        count = 0

        while curr:
            if count == 0:
                new = curr
            count += 1
            print(count)
            if count % k == 0:
                count = 0
                temp = curr.next
                curr.next = None
                # self.print_l(new)
                # print(new.val)
                h = self.reverse(new)
                # self.print_l(h)
            
            if count  == 0:
                while rev.next:
                    rev = rev.next
                rev.next = h
                curr = temp
            else:
                curr = curr.next
        
        if count == 0:
            return dummy.next
        else:
            while rev.next:
                rev = rev.next
            rev.next = temp
        return dummy.next


