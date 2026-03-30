# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        ########### Recursive solution
        # if not root:
        #     root = TreeNode(val)
        #     return root
        
        # if val > root.val:
        #     if root.right:
        #         self.insertIntoBST(root.right, val)
        #     else:
        #         root.right = TreeNode(val)
        # else:
        #     if root.left:
        #         self.insertIntoBST(root.left, val)
        #     else:
        #         root.left = TreeNode(val)
        # return root


        ####### Iterative Solution
        cur = root

        while cur:
            if cur.val > val:
                if cur.left :
                    cur = cur.left
                else:
                    cur.left = TreeNode(val)
                    return root
            else:
                if cur.right:
                    cur = cur.right
                else:
                    cur.right = TreeNode(val)
                    return root
        return TreeNode(val)