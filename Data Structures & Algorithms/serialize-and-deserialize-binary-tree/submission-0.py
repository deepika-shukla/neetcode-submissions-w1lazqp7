# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        # we need to convert tree in string
        # we can use preorder
        # whenever we recieve Null node, we appnend N
        # otherwise its value
        res= []

        def dfs(root):
            if not root:
                # append N
                res.append("N")
                return 
            # if not Null append the value in string format
            res.append(str(root.val))
            # call the function for left and right
            dfs(root.left)
            dfs(root.right)
        
        dfs(root)
        # our lis will be appened with all value of nodes and N
        # convert list into string seperated by ','
        return ",".join(res) 

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        # we get data in string format, we need to convert in list
        list_of_nodes = data.split(",")
        self.i = 0

        # now again we can run dfs to form the tree
        def dfs():
            if list_of_nodes[self.i] == "N":
                # increase the pointer
                self.i += 1
                return None # no node present
            
            #create the node
            node = TreeNode(int(list_of_nodes[self.i]))
            # simillary run for left and right node
            self.i += 1
            node.left = dfs()
            node.right = dfs()
            return node
        return dfs()
