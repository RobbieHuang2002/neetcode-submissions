# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        stack = [(root, root.val)]
        result = 0 
        while stack:
            node, max_value = stack.pop()

            if node.val >= max_value:
                result += 1
            
            if node.right:
                stack.append((node.right, max(max_value, node.right.val)))
            if node.left:
                stack.append((node.left, max(max_value, node.left.val)))

        return result
