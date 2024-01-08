# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        findP = False
        findQ = False
        def find(node):
            if not node:
                return node
            left = find(node.left)
            right = find(node.right)
            if left and right:
                return node
            if node.val == p.val:
                nonlocal findP
                findP = True
                return node
            if node.val == q.val:
                nonlocal findQ
                findQ = True
                return node
            return left or right
        n = find(root)
        if findP and findQ:
            return n
        else:
            return None