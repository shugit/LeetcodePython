class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        q = deque([root])
        nullFound = False
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                if not node:
                    nullFound = True
                else:
                    if nullFound:
                        return False
                    q.append(node.left)
                    q.append(node.right)
        return True
