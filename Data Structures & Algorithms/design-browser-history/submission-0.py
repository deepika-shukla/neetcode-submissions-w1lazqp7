class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None
class BrowserHistory:

    def __init__(self, homepage: str):
        self.cur = Node(homepage)
        

    def visit(self, url: str) -> None:
        # delete forward history
        new = Node(url)
        self.cur.next = new
        new.prev = self.cur
        self.cur = new

    def back(self, steps: int) -> str:
        prev = self.cur
        i = 0
        while prev.prev:
            prev = prev.prev
            if i == steps-1:
                self.cur = prev
                return prev.val
            i += 1
        self.cur = prev
        return prev.val
        

    def forward(self, steps: int) -> str:
        n = self.cur
        i = 0
        while n.next:
            n = n.next
            if i == steps-1:
                self.cur = n
                return n.val
            i += 1
        self.cur = n
        return n.val
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)