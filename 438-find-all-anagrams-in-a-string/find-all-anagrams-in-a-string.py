class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        cp = Counter(p)
        cs = Counter(s[0:len(p)])
        res = []
        if cp == cs:
            res.append(0)
        for i in range(1, len(s)-len(p) + 1):
            cs[s[i+len(p)-1]] += 1
            cs[s[i-1]] -= 1
            if cp == cs:
                res.append(i)
        return res
            