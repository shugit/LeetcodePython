class Solution:
    def minWindow(self, s: str, t: str) -> str:
        return self.sol2(s,t)
    
    def sol2(self, s, t):
        l, r = 0, 0
        window = Counter()
        need = Counter(t)
        matched = 0
        res = ""
        mini = inf
        while r < len(s):
            c = s[r]
            window[c] += 1
            if c in need and need[c] == window[c]:
                matched += 1
            while matched == len(need):
                if r - l + 1 < mini:
                    mini = r - l + 1
                    res = s[l: r+1]
                d = s[l]
                if d in need and window[d] == need[d]:
                    matched -= 1
                l += 1
                window[d] -= 1
            r += 1
        return res

    def sol1(self, s, t):
        window = {}
        count = {}
        for c in t:
            count[c] = count.get(c, 0) + 1
        matched = 0
        res = []
        mini = inf
        l = 0
        for r in range(0, len(s)):
            c = s[r]
            window[c] = window.get(c,0) + 1
            if c in count and window[c] == count[c]:
                matched += 1
            while matched == len(count):
                if (r-l+1) < mini:
                    res = [l,r]
                    mini = r - l + 1
                window[s[l]] -= 1
                if s[l] in count and window[s[l]] < count[s[l]]:
                    matched -= 1
                l += 1
        return s[res[0]:res[1] + 1] if mini != inf else ""