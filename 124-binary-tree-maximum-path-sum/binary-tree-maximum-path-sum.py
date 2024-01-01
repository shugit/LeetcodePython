# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        return self.sol2(root)
    def sol1(self, root):
        if not root:
            return 0
        maxi = float('-inf')
        def maxSum(curr):
            nonlocal maxi
            left = maxSum(curr.left) if curr.left else 0
            right = maxSum(curr.right) if curr.right else 0
            curr_max = max(0, left) + curr.val + max(0, right)
            maxi = max(maxi, curr_max)
            return curr.val + max(left,right,0)
        maxSum(root)
        return maxi
    def sol2(self, root):
        if not root:
            return 0
        res = -inf
        def dfs(node):
            if not node:
                return 0
            nonlocal res
            left = max(dfs(node.left),0)
            right = max(dfs(node.right),0)
            res = max(res, left + node.val + right)
            return node.val + max(left,right)
        dfs(root)
        return res
