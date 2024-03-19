# The read4 API is already defined for you.
# def read4(buf4: List[str]) -> int:

class Solution:
    def __init__(self):
        self.myBuf = deque([])
        self.ended = False

    def read(self, buf: List[str], n: int) -> int:
        while n > len(self.myBuf) and not self.ended:
            buf4 = [''] * 4
            res = read4(buf4)
            if res == 0:
                self.ended = True
            else:
                self.myBuf += buf4[:res]
        i = 0
        while self.myBuf and i < n:
            buf[i] = self.myBuf.popleft()
            i += 1
        return i