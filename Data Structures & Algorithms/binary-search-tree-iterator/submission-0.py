# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.i = 0
        cur = self.root
        self.inorder_nodes = []
        stack = []

        while cur or stack:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                self.inorder_nodes.append(cur.val)
                cur = cur.right


    def next(self) -> int:
        val = self.inorder_nodes[self.i]
        self.i += 1
        return val

        

    def hasNext(self) -> bool:
        return self.i < len(self.inorder_nodes)
            
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()