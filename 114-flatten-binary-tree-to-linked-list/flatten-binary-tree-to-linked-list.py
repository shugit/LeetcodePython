# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        return self.sol3(root)

    def sol4(self, root):
        if not root:
            return None
        stack = [root]
        while stack:
            node = stack.pop()
            if node.left and node.right:
                stack.append(node.right)
                stack.append(node.left)
                node.left, node.right = None, node.left
            elif node.right:
                stack.append(node.right)
            elif node.left:
                stack.append(node.left)
                node.left, node.right = None, node.left
            elif len(stack) < 1:
                break
            else:
                node.right = stack[-1]

    def sol1(self, root):
        if not root:
            return None
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            rTail = dfs(node.right)
            left = node.left
            right = node.right
            node.left = None
            node.right = left
            cur = node
            while cur.right:
                cur = cur.right
            cur.right = right
            return 
        dfs(root)


    def sol2(self, root):
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

    def sol3(self, root: Optional[TreeNode]) -> None:
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
