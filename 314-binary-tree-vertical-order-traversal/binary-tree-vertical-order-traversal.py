class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        h = defaultdict(list)
        if not root:
            return []
        q = deque([(root,0)])
        while q:
            node, order = q.popleft()
            h[order].append(node.val)
            if node.left:
                q.append([node.left, order-1])
            if node.right:
                q.append([node.right, order+1])
        res = []
        for k,v in sorted(h.items()):
            res.append(v)
        return res
