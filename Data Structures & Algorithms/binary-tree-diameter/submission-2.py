# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = [0]

        def height(root):
            if not root:
                return 0
            
            h_l = height(root.left)
            h_r = height(root.right)
        
            diameter[0] = max(diameter[0], h_l + h_r)

            return 1 + max(h_l, h_r)
        
        height(root)
        return diameter[0]
