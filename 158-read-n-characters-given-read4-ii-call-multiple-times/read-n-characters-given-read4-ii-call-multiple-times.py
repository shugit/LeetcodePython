# The read4 API is already defined for you.
# def read4(buf4: List[str]) -> int:

class Solution:
    def __init__(self):
        self.myBuf = []
        self.ended = False

    def read(self, buf: List[str], n: int) -> int:
        while n > len(self.myBuf) and not self.ended:
            buf4 = [''] * 4
            res = read4(buf4)
            if res == 0:
                self.ended = True
            else:
                self.myBuf += buf4[:res]
        if n > len(self.myBuf):
            i = 0
            while i < len(buf) and buf[i] != '':
                buf[i] = ''
                i += 1
            for i in range(len(self.myBuf)):
                buf[i] = self.myBuf[i]
            self.myBuf = []
            return len(buf)
        for i in range(n):
            buf[i] = self.myBuf[i]
        self.myBuf = self.myBuf[n:]
        return n