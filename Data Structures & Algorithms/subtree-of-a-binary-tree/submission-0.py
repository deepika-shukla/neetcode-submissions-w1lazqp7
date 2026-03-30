# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], sub: Optional[TreeNode]) -> bool:
        if not sub:
            return True
        
        if not root:
            return False

        if self.sametree(root, sub):
            return True
        
        return self.isSubtree(root.left, sub) or self.isSubtree(root.right, sub)

    def sametree(self, root, sub):
        if not root and not sub:
            return True
        
        if root and sub and root.val == sub.val:
            return self.sametree(root.left, sub.left) and self.sametree(root.right, sub.right)

        return False 