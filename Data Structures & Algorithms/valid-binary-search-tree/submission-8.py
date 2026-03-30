# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def check(left, root, right):
            if not root:
                return True
            
            if left < root.val < right:
                return check(left, root.left, root.val) and check(root.val, root.right, right)
            
            return False
        
        return check(-999999, root, 999999)