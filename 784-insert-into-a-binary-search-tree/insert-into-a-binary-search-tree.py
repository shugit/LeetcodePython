# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def insert(curr):
            if not curr:
                return TreeNode(val)
            if val < curr.val:
                curr.left = insert(curr.left)
            else:
                curr.right = insert(curr.right)
            return curr
        return insert(root)