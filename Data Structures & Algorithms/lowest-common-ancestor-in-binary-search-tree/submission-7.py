# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # if they are no different sides, the split will be LCA
        # otherwise we need to traverse left or right
        # one can be parent of other

        # if one of them is root
        if p.val == root.val or q.val == root.val:
            return root
        
        # if they exist on different parts
        if (p.val < root.val and q.val > root.val) or (q.val < root.val and p.val > root.val):
            return root
        
        # serach on left
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        
        else:
            return self.lowestCommonAncestor(root.right, p, q)