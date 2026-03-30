# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # the node could be the parent itself
        if root.val == p.val or root.val == q.val:
            return root
        
        #check on left side
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p,q)
        elif p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p,q)
        else:
            # the current root will be the parent
            return root