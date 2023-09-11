class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
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