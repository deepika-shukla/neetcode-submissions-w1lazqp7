# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        final = [root.val]

        def find(root):
            if not root:
                return 0
            
            leftmax = find(root.left)
            rightmax = find(root.right)

            # if negative
            leftmax = max(leftmax, 0)
            rightmax = max(rightmax, 0)

            # with split
            final[0] = max(final[0], root.val+leftmax+rightmax)

            return root.val + max(leftmax, rightmax)
        
        find(root)
        return final[0] 