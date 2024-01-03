# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def dfs(inorder, postorder):
            if not inorder or not postorder:
                return None
            root = TreeNode(postorder.pop())
            idx = inorder.index(root.val)
            root.left = dfs(inorder[0:idx], postorder[0:idx])
            root.right = dfs(inorder[idx+1:], postorder[idx:])
            return root
        return dfs(inorder, postorder)
