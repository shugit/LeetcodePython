# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class SearchNode:
    def __init__(size, mini, maxi):
        self.size = size
        self.mini = mini
        self.maxi = maxi

class Solution:
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        res = 0
        def search(node):
            nonlocal res
            if not node:
                return 0, inf, -inf
            left_size, left_mini, left_maxi = search(node.left)
            right_size, right_mini, right_maxi = search(node.right)

            if left_size < 0 or right_size < 0 or left_maxi >= node.val or right_mini <= node.val:
                return -1, 0, 0
            res = max(res, left_size + 1 + right_size)
            return (left_size + 1 + right_size, min(left_mini, node.val), max(right_maxi, node.val))
        search(root)
        return res
