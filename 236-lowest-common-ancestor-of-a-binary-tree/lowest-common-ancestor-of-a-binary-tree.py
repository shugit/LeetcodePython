class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':    
        return self.sol2(root, p, q)
    def sol2(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def find(node):
            if not node or node == p or node == q:
                return node
            l = find(node.left)
            r = find(node.right)
            if l and r:
                return node
            return l or r
        return find(root)
        
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