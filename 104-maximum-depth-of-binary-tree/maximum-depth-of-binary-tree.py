# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.recur(root)
        
    def recur1(self, root):
        if not root:
            return 0
        def md(curr):
            left_depth = md(curr.left) if curr.left else 0
            right_depth = md(curr.right) if curr.right else 0
            return max(left_depth, right_depth) + 1
        return md(root)

    def recur(self, root):
        if not root:
            return 0
        
        res = -inf
        def dfs(node, depth):
            nonlocal res
            if not node:
                return
            res = max(res, depth)
            dfs(node.left, depth+1)
            dfs(node.right, depth+1)
            return
        dfs(root, 1)
        return res

    def BDS(self, root: Optional[TreeNode]):
        if not root:
            return 0
        queue = [root]
        order = []
        while queue:
            level = []
            size = len(queue)
            for _ in range(size):
                curr = queue.pop(0)
                level.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            if level:
                order.append(level)
        return len(order)