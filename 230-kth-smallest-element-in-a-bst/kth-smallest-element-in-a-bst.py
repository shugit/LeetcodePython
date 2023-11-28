# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []
        def find(curr):
            if len(res) >= k:
                return 
            if not curr:
                return 
            find(curr.left)
            res.append(curr.val)
            find(curr.right)
        find(root)
        return res[k-1]