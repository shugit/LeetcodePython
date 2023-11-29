# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced2(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        def height(curr):
            if not curr.left and not curr.right:
                return 1
            left = height(curr.left) if curr.left else 0
            right = height(curr.right) if curr.right else 0
            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1
            else:
                return max(left, right) + 1
        res = height(root)
        return res >= 0

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(curr):
            if not curr:
                return 0
            leftHeight = height(curr.left)
            rightHeight = height(curr.right)
            if leftHeight == -1 or rightHeight == -1 or abs(rightHeight-leftHeight) > 1:
                return -1
            return max(leftHeight, rightHeight)+1
        res = height(root)
        return True if res != -1 else False
            