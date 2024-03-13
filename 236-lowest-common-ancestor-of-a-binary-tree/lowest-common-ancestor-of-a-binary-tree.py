class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def find(node):
            if not node:
                return None
            if node.val == p.val or node.val == q.val:
                return node
            left = find(node.left)
            right = find(node.right)
            if left and right:
                return node
            return left or right
        return find(root)