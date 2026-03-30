# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

            def dfs(root):
                if not root:
                    return [True, 0]
                
                h_left = dfs(root.left)
                h_right = dfs(root.right)

                balance = h_left[0] and h_right[0] and abs(h_left[1] - h_right[1]) <= 1

                return [balance, 1 + max(h_left[1], h_right[1])]
            return dfs(root)[0]

            
