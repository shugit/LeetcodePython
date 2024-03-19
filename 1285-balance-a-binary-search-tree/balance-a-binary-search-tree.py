class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        path = []
        def inorder(root):
            if not root: 
                return
            inorder(root.left)
            path.append(root)
            inorder(root.right)

        inorder(root)
        def build(l , r):
            if l > r: 
                return
            mid = l + (r - l) // 2
            node = path[mid]
            node.left = build(l, mid - 1)
            node.right = build(mid + 1, r)
            return node
        return build(0, len(path)- 1)
        