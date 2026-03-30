# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        #recursive
        # if not root or not p or not q:
        #     return None
        # if root.val == p or root.val == q:
        #     return root
        # if max(p.val, q.val) < root.val:
        #     return self.lowestCommonAncestor(root.left, p, q)
        # if min(p.val, q.val) > root.val:
        #     return self.lowestCommonAncestor(root.right, p, q)
        # else:
        #     return root
        
        #iterative
        #start from root
        curr = root

        while curr:
            if curr.val == p.val or curr.val == q.val:
                return curr
            if p.val < curr.val and q.val < curr.val:
                curr = curr.left
            elif p.val > curr.val and q.val > curr.val:
                curr = curr.right
            else:
                return curr



