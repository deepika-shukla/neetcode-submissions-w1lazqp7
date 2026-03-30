# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        max_h = [0]

        def h(root):
            if not root:
                return 0
            
            left_path = h(root.left)
            right_path = h(root.right)

            #include root
            max_h[0] = max(max_h[0], left_path + right_path)

            return 1 + max(left_path, right_path)
        
        h(root)
        return max_h[0]

