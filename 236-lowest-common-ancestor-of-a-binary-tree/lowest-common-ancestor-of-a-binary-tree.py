class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':    
        return self.sol1(root, p, q)
    def sol1(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def find(node):
            if not node or node == p or node == q:
                return node
            if node.val == p.val or node.val == q.val:
                return node
            left = find(node.left)
            right = find(node.right)
            if left and right:
                return node
            return left or right
        return find(root)