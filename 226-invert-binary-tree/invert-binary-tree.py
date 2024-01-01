# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        return self.sol2(root)
    def sol1(self, root):
        if not root:
            return None
        def invert(curr):
            if not curr.left and not curr.right:
                return
            if curr.left:
                invert(curr.left)
            if curr.right:
                invert(curr.right)
            curr.left, curr.right = curr.right, curr.left
        invert(root)
        return root
    def sol2(self, root):
        if not root:
            return None
        def dfs(node):
            if not node:
                return None
            node.left, node.right = node.right, node.left
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        return root
            