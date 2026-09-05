class Node:
    def __init__(self, val=0):
        self.val = val
        self.next = None
class MyLinkedList:

    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        i = 0
        if not self.head:
            return -1
        cur = self.head
        while cur:
            if i == index:
                return cur.val
            i += 1
            cur = cur.next
        return -1

    def addAtHead(self, val: int) -> None:
        node = Node(val)
        temp = self.head
        self.head = node
        node.next = temp
        
        

    def addAtTail(self, val: int) -> None:
        if not self.head:
            self.head = Node(val)
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = Node(val)
        

    def addAtIndex(self, index: int, val: int) -> None:
        i = 0
        if not self.head and index != 0:
            return
        cur = self.head
        node = Node(val)
        while cur:
            if i == index - 1:
                temp = cur.next
                cur.next = node
                node.next = temp
                return
            i += 1
            cur = cur.next



        

    def deleteAtIndex(self, index: int) -> None:
        if not self.head:
            return
        
        cur = self.head
        i = 0
        while cur.next:
            if i == index -1:
                cur.next = cur.next.next
                return
            i += 1
            cur = cur.next
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)