# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten2(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def preorder(curr):
            if not curr:
                return None
            leftTail = preorder(curr.left)
            rightTail = preorder(curr.right)
            if curr.left:
                leftTail.right = curr.right
                curr.right = curr.left
                curr.left = None
            last = rightTail or leftTail or curr
            return last
        preorder(root)
        return 

    def flatten(self, root: Optional[TreeNode]) -> None:
        node_list = []
        def preorder(curr):
            if not curr:
                return
            node_list.append(curr)
            preorder(curr.left)
            preorder(curr.right)
        preorder(root)
        for i in range(0, len(node_list)):
            node_list[i].left = None
            if i + 1 < len(node_list):
                node_list[i].right = node_list[i+1]
        return

