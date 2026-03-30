# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = [0]

        def dfs(root):
            if not root:
                return 0
            
            height_l = dfs(root.left)
            height_r = dfs(root.right)

            diameter[0] = max(diameter[0], height_l + height_r)
        
            return 1 + max(height_l, height_r)
        
        dfs(root)
        return diameter[0]


