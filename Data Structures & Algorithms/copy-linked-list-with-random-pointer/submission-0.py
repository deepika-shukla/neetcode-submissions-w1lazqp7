"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        #we need to create a copy of original list
        #one point to notice, we are creating copy of node,
        #and it is pointing to a node for which we didn't create copy
        #it will be difficult
        #therefore first we will create the copy of nodes
        #in hashmap, then create copy of next and random pointers

        oldtonew = {None : None} # we also need to take care of an edge case when its None
        cur = head
        while cur:
            #create a copy node
            copy = Node(cur.val)
            oldtonew[cur] = copy
            cur = cur.next
        
        cur = head
        while cur:
            copy = oldtonew[cur]
            copy.next = oldtonew[cur.next]
            copy.random = oldtonew[cur.random]
            cur = cur.next
        
        return oldtonew[head]

        
