# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], sub: Optional[TreeNode]) -> bool:
        #if root is None but not subroot then 
        if not sub:
            return True
        if not root:
            return False

        if self.isSameTree(root, sub):
            #now we found the start, we have to check from here we get equal subtree
            return True
        
        return self.isSubtree(root.left,sub) or self.isSubtree(root.right, sub)
        
    def isSameTree(self,root, sub):
        if not root and not sub:
            return True
        
        if root and sub and root.val == sub.val:
            return self.isSameTree(root.left, sub.left) and self.isSameTree(root.right, sub.right) 
        return False

