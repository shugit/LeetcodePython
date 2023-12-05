# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        def bfs(arr):
            if not arr:
                return None
            node = TreeNode(arr[0])
            i = 1
            while i < len(arr) and arr[i] < node.val:
                i += 1
            node.left = bfs(arr[1:i])
            node.right = bfs(arr[i:])
            return node
        return bfs(preorder)