# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        maxi = -inf
        def dfs(cur, curMax, curMin):
            nonlocal maxi
            if not cur:
                maxi = max(maxi, abs(curMax - curMin))
                return
            maxi = max(maxi, abs(curMax - curMin))
            curMin = min(curMin, cur.val)
            curMax = max(curMax, cur.val)
            dfs(cur.left, curMax,curMin )
            dfs(cur.right, curMax, curMin)
        dfs(root, root.val, root.val)
        return maxi
        