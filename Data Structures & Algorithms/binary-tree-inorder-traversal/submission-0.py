# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # push node to the stack 
        # keep going to the left of each node 
        # once that it is null, pop and add to the res array
        # now check the right subtree of the new node 
        
        stack = []
        res = []
        curr = root

        while curr or stack: 
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            res.append(curr.val)
            curr = curr.right

        return res

