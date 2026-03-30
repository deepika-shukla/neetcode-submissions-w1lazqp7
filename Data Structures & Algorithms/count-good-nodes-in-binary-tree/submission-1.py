# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # edge case : root will always be good node
        # if tree is emtpy no good node
        # keep track of max in the path
        # we are using preorder
        def good(root, maxVal):
            if not root:
                return 0
            
            res = 1 if root.val >= maxVal else 0

            # update max
            maxVal = max(maxVal, root.val)
            # check on both left and right
            res += good(root.left, maxVal)
            res += good(root.right, maxVal)

            return res
        
        # call for root, passing root value
        return good(root, root.val)
