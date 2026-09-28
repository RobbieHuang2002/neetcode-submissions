# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        

        result = []
        hashmap = {}
        stack = [(root, 1)]

        while stack:
            node, depth = stack.pop()
            if depth not in hashmap:
                hashmap[depth] = [node.val]
            else:
                hashmap[depth].append(node.val)

            if node.right:
                stack.append((node.right, depth + 1))
            if node.left:
                stack.append((node.left, depth +1))
        
        for values in hashmap.values():
            result.append(values)
        return result
