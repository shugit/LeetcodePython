class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.q = []
        def it(curr):
            if not curr:
                return
            it(curr.left)
            self.q.append(curr.val)
            it(curr.right)
        it(root)

    def next(self) -> int:
        return self.q.pop(0)
        

    def hasNext(self) -> bool:
        return len(self.q) > 0