class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        def find(node, depth):
            if not node:
                return None, depth
            leftLca, leftDepth = find(node.left, depth + 1)
            rightLca, rightDepth = find(node.right, depth + 1)
            if leftDepth == rightDepth:
                return node, leftDepth
            elif leftDepth > rightDepth:
                return leftLca, leftDepth
            else:
                return rightLca, rightDepth

        lca, _ = find(root, 0)
        return lca