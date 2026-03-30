# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        # ####### DFS #########
        # def check(left, root, right):
        #     if not root:
        #         return True
            
        #     if left < root.val < right:
        #         return check(left, root.left, root.val) and check(root.val, root.right, right)
            
        #     return False
        
        # return check(-999999, root, 999999)

        ########## BFS ############ 

        q = deque()

        ans = True
        left = -9999
        right = 9999
        q.append([ left, root, right ])
        while q:
            left, node, right = q.popleft()
            if not (left < node.val < right):
                return False
            
            if node.left:
                q.append([left, node.left, node.val])
            if node.right:
                q.append([node.val, node.right, right])
        return True

