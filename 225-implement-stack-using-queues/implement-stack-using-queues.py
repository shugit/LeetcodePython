class MyStack:

    def __init__(self):
        self.q1 = []
        self.q2 = []
        self.mytop = None

    def push(self, x: int) -> None:
        o = self.q1 if self.q1 >= self.q2 else self.q2
        o.append(x)
        self.mytop = x

    def pop(self) -> int:
        o1 = self.q1 if self.q1 >= self.q2 else self.q2
        o2 = self.q2 if o1 == self.q1 else self.q1
        while len(o1) > 1:
            res = o1.pop(0)
            self.mytop = res
            o2.append(res)
        return o1.pop(0)

    def top(self) -> int:
        return self.mytop

    def empty(self) -> bool:
        return len(self.q1) == len(self.q2)

class MyStack2:

    def __init__(self):
        self.q = []

    def push(self, x: int) -> None:
        new_q = [x] + self.q
        self.q = new_q

    def pop(self) -> int:
        return self.q.pop(0)

    def top(self) -> int:
        return self.q[0]

    def empty(self) -> bool:
        return len(self.q) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()