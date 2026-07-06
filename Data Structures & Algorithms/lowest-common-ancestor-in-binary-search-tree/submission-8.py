# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # we can have three cases 
        # one they can be either of left or right
        # one of them could be root
        # one can be parent of another

        def dfs(p,q, root):
            # if one of them is root
            if p.val == root.val:
                return p
            if q.val == root.val:
                return q

            # if they exist on same side
            if p.val < root.val and q.val < root.val:
                return dfs(p,q, root.left)
            elif p.val > root.val and q.val > root.val:
                return dfs(p,q,root.right)
            else:
                # if on oppsite side, root is the parent
                return root
        return dfs(p,q,root)
            

