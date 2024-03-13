class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return self.sol1(s, t)
    def sol1(self, s: str, t: str) -> bool:
        c1 = Counter(s)
        c2 = Counter(t)
        return c1 == c2

    def sol2(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        h = {}
        for l in s:
            if l in h:
                h[l] += 1
            else:
                h[l] = 1
        # print(h)
        for l in t:
            if l in h:
                h[l] -= 1
            else:
                h[l] = -1
        # print(h)
        for k,v in h.items():
            if v != 0:
                return False
        return True