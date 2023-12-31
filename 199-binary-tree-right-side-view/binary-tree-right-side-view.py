# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        return self.rightView(root)
        if not root:
            return []
        q = [root]
        order = []
        while q:
            level = []
            for _ in range(len(q)):
                cur = q.pop(0)
                level.append(cur.val)
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            right = level.pop()
            order.append(right)
        return order
                

    def rightView(self, root):
        if not root:
            return None
        res = []
        def dfs(node, depth):
            if not node:
                return
            if depth > len(res):
                res.append(node.val)
            if node.right:
                dfs(node.right, depth+1)
            if node.left:
                dfs(node.left, depth+1)
        dfs(root, 1)
        return res