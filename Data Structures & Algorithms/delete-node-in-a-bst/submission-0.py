# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #function to find minimum in tree
    def find_min_node(self, root):
        cur = root
        #now chcek for left node if it exist
        while cur and cur.left:
            #keep going left until you find a leaf node
            cur = cur.left
        #the node which you are on will be smalled
        return cur

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # now for deleting we have to make sure for two things
        # the node could be with 0 or 1 nodes, return None or the only child
        # the node could be with 2 nodes, replace with leaf node


        # edge case, if tree is empty
        if not root:
            return None
        
        #now check the ket is smaller or greater or equal to root
        if root.val < key:
            #search in right tree
            root.right = self.deleteNode(root.right, key)
        elif root.val > key:
            #search in left tree,
            root.left = self.deleteNode(root.left, key)
        else:
            #if the root itself needs to be deleted
            # first check if 1 child or no child is present
            if not root.left:
                # if root.left is not present, then only right child will be there
                return root.right
            if not root.right:
                # if right is not present, the include left in tree
                return root.left
            else:
                # now both child are present
                # first we will fina the node with minimum val at the right
                minimum = self.find_min_node(root.right)
                #we found the leaf node with least vale, replace the value with the Node which needs to be deleted
                root.val = minimum.val
                #now we nedd to delete that node
                root.right = self.deleteNode(root.right, minimum.val)

        return root