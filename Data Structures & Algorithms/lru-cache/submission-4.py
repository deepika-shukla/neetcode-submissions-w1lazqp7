class Node:
    def __init__(self,key,val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        # we need left and right pointer
        self.left = Node(0, 0)
        self.right = Node(0, 0)

        # we need to connect them
        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node):
        # we need to rmeove from left

        prev, next = node.prev, node.next
        prev.next = node.next
        next.prev = prev
    
    def insert(self, node):
        #to the right
        prev = self.right.prev
        self.right.prev = node
        node.next = self.right
        prev.next = node
        node.prev = prev



    def get(self, key: int) -> int:
        if key in self.cache:
            # we need to add in right since its most used
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1
        

    def put(self, key: int, val: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, val)
        self.insert(self.cache[key])

        # now if capacity is increased, we need to remove LRU
        # that means from left
        if len(self.cache) > self.capacity:
            lru_node = self.left.next
            self.remove(lru_node)
            #also delete from hashmap
            del self.cache[lru_node.key]
        
