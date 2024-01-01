
class MaxStack:
    class Node:
        def __init__(self, val):
            self.val = val
            self.left = None
            self.right = None

    def __init__(self):
        self.q = []
        self.l = self.Node(0)
        self.head = self.l
        self.h = defaultdict(list)

    def push(self, x: int) -> None:
        cur = self.Node(x)
        self.l.right, cur.left = cur, self.l
        self.l = self.l.right
        heapq.heappush(self.q, -x)
        self.h[x].append(cur)

    def pop(self) -> int:
        res = self.l.val
        self.l = self.l.left
        self.l.right = None
        self.h[res].pop()
        if not self.h[res]:
            del self.h[res]
        return res

    def top(self) -> int:
        return self.l.val
        
    def peekMax(self) -> int:
        while -self.q[0] not in self.h:
            heapq.heappop(self.q)
        return -self.q[0]

    def popMax(self) -> int:
        res = self.peekMax()
        node = self.h[res].pop()
        if not self.h[res]:
            del self.h[res]
        if node == self.l:
            self.l = self.l.left
            self.l.right = None
        else:
            node.left.right, node.right.left = node.right, node.left
        return res
        
        


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()