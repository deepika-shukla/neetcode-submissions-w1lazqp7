# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # we need to delete the node, we can replace with smallest node in right 

        # edge case
        if not root:
            return root
        if key > root.val:
            # we need to right side
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            # check if left tree or right tree exist
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            else:
                # we need to serach for smallest at right
                cur = root.right
                while cur.left:
                    cur = cur.left
                
                root.val = cur.val
                # now delete this node
                root.right = self.deleteNode(root.right, root.val)
        return root

        