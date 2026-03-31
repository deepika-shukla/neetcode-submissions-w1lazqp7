# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        # we will use post order, first children and then parent
        def backtrack(root):
            if not root:
                return None
            
            # first run for children
            root.left = backtrack(root.left)
            root.right = backtrack(root.right)

            # then check for parent
            if not root.left and not root.right and root.val == target:
                return None
            return root 
        
        return backtrack(root)