class Solution:
    def customSortString(self, order: str, s: str) -> str:
        h = {}
        c = Counter(s)
        res = ""
        for o in order:
            if o in c:
                res += o * c[o]
                c[o] = 0
        for o, num in c.items():
            res += o * num
        return res