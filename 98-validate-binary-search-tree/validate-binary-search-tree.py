# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(curr,left,right):
            if not curr:
                return True
            if not (left < curr.val < right):
                return False
            return valid(curr.left, left, curr.val) and valid(curr.right, curr.val, right)
        return valid(root, float("-inf"), float("inf"))
            
    