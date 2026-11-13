class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}

        # join left and right
        self.left = Node(0,0)
        self.right = Node(0,0)


        # left LRU, right MRU
        self.left.next = self.right
        self.right.prev = self.left
    
    def remove(self, node):
        # to remove from list
        left, right = node.prev, node.next
        left.next = right
        right.prev = left
    
    def insert(self, node):
        # insert to the right
        # get last node
        last = self.right.prev

        last.next = node
        node.next = self.right
        node.prev = last
        self.right.prev = node
        

    def get(self, key: int) -> int:
        if key in self.cache:
            # we need to move to right as it is recently used
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1
        

    def put(self, key: int, value: int) -> None:
        # if key already exits we need to update value
        if key in self.cache:
            self.remove(self.cache[key])

        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])
        

        if len(self.cache) > self.cap:
            # remove from left
            # get the first node
            lru_node = self.left.next
            self.remove(lru_node)
            del self.cache[lru_node.key]

        
