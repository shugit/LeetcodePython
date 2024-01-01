# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        return self.recur(root)

    def recur1(self, root):
        if not root:
            return 0
        maxi = 0
        def dia(curr):
            nonlocal maxi
            if not curr.left and not curr.right:
                return 1
            left = dia(curr.left) if curr.left else 0
            right = dia(curr.right) if curr.right else 0
            maxi = max(maxi, left + right)
            return max(left, right) + 1
        dia(root)
        return maxi

    def recur(self, root):
        if not root:
            return 0
        res = -inf
        def dfs(node):
            if not node:
                return 0
            nonlocal res
            left = dfs(node.left)
            right = dfs(node.right)
            res = max(res, left + right)
            return max(left, right) + 1
        dfs(root)
        return res