# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        final = [root.val]

        def dfs(root):
            if not root:
                return 0
            
            # calculate left and right sum
            leftmax = dfs(root.left)
            rightmax = dfs(root.right)
            
            # Ignore negative sum
            leftmax = max(leftmax, 0)
            rightmax = max(rightmax, 0)

            # now with split
            final[0] = max(final[0], root.val + leftmax + rightmax)
            
            # without split
            return root.val + max(leftmax, rightmax)
        dfs(root)
        return final[0]