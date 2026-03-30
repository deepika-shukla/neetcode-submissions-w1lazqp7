# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # from preorder we will get root
        # and from the index of that root in order
        # we will get the left side belong to keft tree and right side to right tree
        # and we will divide the tree and join the nodes

        # edge case, if no pre or inorder
        # the tree/node doesn't exist return None
        if not preorder or not inorder:
            return None

        #get the root
        root = TreeNode(preorder[0])

        #get the index 
        mid = inorder.index(preorder[0])

        #now divide in two parts
        # left side of inorder will be in root.left,
        # simillarly divide for preorder
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])

        return root 