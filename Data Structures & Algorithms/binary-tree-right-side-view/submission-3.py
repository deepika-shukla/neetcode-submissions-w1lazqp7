# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        l = []
        queue = collections.deque()
        queue.append(root)
        while queue:
            lenq = len(queue)
            level = []
            for i in range(lenq):
                node = queue.popleft()
                if node:
                    level.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
            if level:
                # print(level)
                l.append(level[-1])
            
  
        return l  
        
