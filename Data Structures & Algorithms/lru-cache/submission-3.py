class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev, self.next = None, None

class LRUCache:

    def __init__(self, capacity: int):
        # size of our hashmap
        self.capacity = capacity

        # we can store key value in nodes
        # and at left we will insert LRU, at right MRU
        
        # we will have are cache
        self.cache = {} # it will store key which will node addres as value and have key/value

        # also we need left and right ro store LRU, MRU
        self.left, self.right = Node(0,0), Node(0,0)

        # also join them because insertion we will do in the middle of these
        self.left.next, self.right.prev = self.right, self.left

    # to remove node from list
    def remove(self, node):
        # now to remove any node from double linked list
        # we only need to update the pointer of its prev and next node
        # to each other , therefore the current node will be out of list
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev
    
    #insert at right
    def insert(self, node):
        # to insert at right, we have self.right to help with last node
        # we have to insert before self.right
        # and after the node which is before self.right

        # to get before node
        # before = self.right.prev

        # before.next = node
        # node.next = self.right
        # self.right.prev = node
        # node.prev = before
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev


    def get(self, key: int) -> int:
        # if the key exists we need to return that value
        # however we need to store in recent as it is recently used
        if key in self.cache:
            #remove from the left
            self.remove(self.cache[key])
            #insert at the right
            self.insert(self.cache[key])
            return self.cache[key].val
        
        # if key doesn't exists
        return -1

        


    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        #insert in list now it is most frequent
        self.insert(self.cache[key])

        # also check if the capacity has increased, then we have remove LRU
        # which we will find at left side
        if len(self.cache) > self.capacity:
            # the node which we have to remove, will be next to self.left
            lru_node = self.left.next
            self.remove(lru_node)
            #also delete from hashmap
            del self.cache[lru_node.key]
            
