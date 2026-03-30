# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        final = [root.val]

        def cal(root):
            if not root:
                return 0
            
            leftmax = cal(root.left)
            rightmax = cal(root.right)
            leftmax = max(leftmax, 0)
            rightmax = max(rightmax,0)

            # cal with splits
            final[0] = max(final[0], leftmax + root.val + rightmax)

            return root.val + max(leftmax, rightmax)
        
        cal(root)

        
        return final[0]