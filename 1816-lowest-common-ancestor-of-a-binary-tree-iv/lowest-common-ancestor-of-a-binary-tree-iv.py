# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        vals = set([x.val for x in nodes])
        def find(node):
            if not node:
                return node
            if node.val in vals:
                return node
            left = find(node.left)
            right = find(node.right)
            if left and right:
                return node
            return left or right

        return find(root)