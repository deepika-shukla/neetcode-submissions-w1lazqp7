# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # ############ Recursive DFS ################3
        # if not root:
        #     return []
        
        # ans = []

        # def preorder(root):
        #     ans.append(root.val)
        #     if root.left:
        #         preorder(root.left)
        #     if root.right:
        #         preorder(root.right)
        
        # preorder(root)
        # return ans


        # ############### ITERATIVE DFS ##############
        # Pre means : root -> left -> right
        stack = []
        cur = root
        ans = []
        while cur or stack:
            if cur:
                # we need to print root first
                ans.append(cur.val)
                # then store the right and move left

                if cur.right:
                    stack.append(cur.right)
                cur = cur.left
            else:
                # then we need to pop
                cur = stack.pop()
        return ans
