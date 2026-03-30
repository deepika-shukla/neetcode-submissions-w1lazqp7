# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution: 
    def isSameTree(self, r1, r2):
        if not r1 and not r2:
            return True
        if not r1:
            return False
        if not r2:
            return False

        if r1.val == r2.val:
            return self.isSameTree(r1.left, r2.left) and self.isSameTree(r1.right, r2.right) 
        return False 
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # edge cases subroot is None
        if subRoot is None:
            return True
        
        # if subtree but not root
        if not root:
            return False
        
        # now it can either be on left or right
        # if root matches we need to check for the left an dright
        if self.isSameTree(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)