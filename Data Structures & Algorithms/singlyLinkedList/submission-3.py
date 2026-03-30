class LinkedListNode:
    def __init__(self,val):
        self.val = val
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    
    def get(self, index: int) -> int:
        i = 0
        cur = self.head
        while cur:
            if i == index:
                return cur.val
            i += 1
            cur = cur.next
        return -1
        

    def insertHead(self, val: int) -> None:
        if not self.head:
            self.head = LinkedListNode(val)
            return
        node = LinkedListNode(val)
        node.next = self.head
        self.head = node

        

    def insertTail(self, val: int) -> None:
        if not self.head:
            self.head = LinkedListNode(val)
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = LinkedListNode(val)

    def remove(self, index: int) -> bool:
        if not self.head:
            return False
        if index == 0:
            self.head = self.head.next
            return True 
        cur = self.head
        i = 0
        while cur:
            if cur.next and i == index-1:
                cur.next = cur.next.next
                return True
            i += 1
            cur = cur.next
        return False


    def getValues(self) -> List[int]:
        l = []
        cur = self.head
        while cur:
            l.append(cur.val)
            cur = cur.next
        return l
        
