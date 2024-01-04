# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        res = 0
        def dfs(node):
            nonlocal res
            if not node:
                return
            dfs(node.right)
            res += node.val
            node.val = res
            dfs(node.left)
        dfs(root)
        return root