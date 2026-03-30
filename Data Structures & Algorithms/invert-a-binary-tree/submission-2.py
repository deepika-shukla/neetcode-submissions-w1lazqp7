# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # we need to invert binary tree
        # that means left should be right and right should be left and
        # repeate for all nodes

        #if we reach the end return
        if root is None:
            return None
        
        root.left, root.right = root.right, root.left

        #then call the fuction for left and right child
        self.invertTree(root.left)
        self.invertTree(root.right)

        #return the root 
        return root

