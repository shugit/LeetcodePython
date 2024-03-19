# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        d = set(to_delete)
        res = []
        def dfs(node):
            if not node:
                return None
            node.left = dfs(node.left)
            node.right = dfs(node.right)
            if node.val in d:
                if node.left:
                    res.append(node.left)
                if node.right:
                    res.append(node.right)
                return None 
            else:    
                return node
        if dfs(root):
            res.append(root)
        return res
