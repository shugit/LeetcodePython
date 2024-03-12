class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.stack = deque([])
        self.push_left(root)
    
    def push_left(self,root):
        while root:
            self.stack.append(root)
            root = root.left

    def next(self) -> int:
        root = self.stack.pop()
        if root.right:
            self.push_left(root.right)
        return root.val

    def hasNext(self) -> bool:
        if len(self.stack)!=0:
            return True
        return False
