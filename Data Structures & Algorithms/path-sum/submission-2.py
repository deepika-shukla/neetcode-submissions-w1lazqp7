# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def backtrack(node, cur):
            if not node:
                return False

            cur += node.val

            if not node.left and not node.right:
                # we need sum from root to leaf, so at edge node we will check if we are able to find target sum at this path
                return cur == targetSum
            
            return backtrack(node.left, cur) or      backtrack(node.right, cur)

        return backtrack(root, 0)

            