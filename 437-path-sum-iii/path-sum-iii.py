# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        res = 0
        h = {}
        def dfs(node, curSum):
            nonlocal res
            if not node:
                return
            curSum += node.val
            if curSum == targetSum:
                res += 1
            res += h.get(curSum - targetSum, 0)
            h[curSum] = h.get(curSum,0)+1
            dfs(node.left, curSum)
            dfs(node.right, curSum)
            h[curSum] -= 1

        dfs(root, 0)
        return res
