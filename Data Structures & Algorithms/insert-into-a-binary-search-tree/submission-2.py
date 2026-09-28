# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        if not root:
            return TreeNode(val)
        
        curr = root
        while curr:
            if val > curr.val:
                if not curr.right:
                    curr.right = TreeNode(val)
                    return root
                else:
                    curr = curr.right
            else:
                if not curr.left:
                    curr.left = TreeNode(val)
                    return root
                else:
                    curr = curr.left
        






















        # # if no tree
        # if not root:
        #     # create tree node with val 
        #     return TreeNode(val)
        
        # curr = root
        # # while there is a tree
        # while curr:
        #     # if the value is greater than the current node go right subtree
        #     if val > curr.val:
        #         # if there are no more sub nodes
        #         if not curr.right:
        #             # make the next right node equal to val
        #             curr.right = TreeNode(val)
        #             return root
        #         else:
        #             #if there is then continue traversing the tree down the right 
        #             curr = curr.right
        #     # if the value is less than the current node then go left subtree
        #     else:
        #         if not curr.left:
        #             curr.left = TreeNode(val)
        #             return root
        #         else:
        #             curr = curr.left
        

        
