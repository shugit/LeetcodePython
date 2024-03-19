# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        path = []

        def inorder(root):
            if not root: return

            inorder(root.left)
            path.append(root)
            inorder(root.right)

        inorder(root)
        n = len(path)

        def construct(low, high):
            if low > high: return
            mid = (low + high) // 2

            node = path[mid]
            node.left = construct(low, mid - 1)
            node.right = construct(mid + 1, high)

            return node

        return construct(0, n - 1)
        