# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #we have to find the max depth which means
        #max of left length and right length

        #if root is None means height is 0
        if not root:
            return 0

        #otherwise we will add 1 and check the max of left and right
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        

