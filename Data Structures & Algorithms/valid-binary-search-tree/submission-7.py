# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        #empty tree is a valid tree
        #with this below solution the problem is it checks for current root and its left right child
        #it does not check for its grandparent
        # if not root:
        #     return True
        
        # if root.left and root.left.val >= root.val:
        #     return False

        # if root.right and root.right.val <= root.val:
        #     return False
        
        # return self.isValidBST(root.left) and self.isValidBST(root.right )

        #we have to keep track of min left and right val

        def valid(root,left,right):
            if not root:
                return True

            if not( left < root.val < right):
                return False
            
            return valid(root.left, left, root.val) and valid(root.right, root.val, right)
        return valid(root,-10000,10000)
    