class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        q = deque([root])
        level = []
        while q:
            level = []
            for _ in range(len(q)):
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        def find(node):
            if not node:
                return node
            if node.val in level:
                return node
            left = find(node.left)
            right = find(node.right)
            if left and right:
                return node
            return left or right
        return find(root)