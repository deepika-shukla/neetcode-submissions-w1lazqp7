# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # we have to merge k lists
        # we will create a helper function to merger

        # check if lists is empty
        if len(lists) == 0:
            return None
        
        while len(lists) > 1:
            #create two groups and merge
            mergedLists = []
            for i in range(0, len(lists),2):
                l1 = lists[i]
                if i+1 < len(lists):
                    l2 = lists[i+1]
                else:
                    l2 = None
                mergedLists.append(self.merge(l1, l2))
            lists = mergedLists
        return lists[0]


    
    def merge(self, l1,l2):
        #create a dummy node
        dummy = ListNode()
        temp = dummy

        #traverse both list
        while l1 and l2:
            #compare the values
            if l1.val < l2.val:
                dummy.next = l1
                l1 = l1.next
            else:
                dummy.next = l2
                l2 = l2.next
            dummy = dummy.next
        
        if l1:
            dummy.next = l1
        if l2:
            dummy.next = l2
        return temp.next
