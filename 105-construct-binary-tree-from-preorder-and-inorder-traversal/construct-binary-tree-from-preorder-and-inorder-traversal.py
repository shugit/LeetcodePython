# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def dfs(preorder, inorder):
            if not preorder:
                return None
            val = preorder[0]
            idx = inorder.index(val)
            node = TreeNode(val)
            node.left = dfs(preorder[1:idx+1], inorder[0:idx])
            node.right = dfs(preorder[idx+1:], inorder[idx+1:])
            return node
        return dfs(preorder, inorder)