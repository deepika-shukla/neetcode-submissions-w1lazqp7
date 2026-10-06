# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # we will use inorder which will give sorted list
        # we can stop at kth index

        listOfNodes = []

        def inorder(root):
            if not root:
                return []
            inorder(root.left)
            listOfNodes.append(root.val)
            if len(listOfNodes) == k:
                return listOfNodes
            inorder(root.right)
        inorder(root)
        print(listOfNodes)
        return listOfNodes[k-1]
