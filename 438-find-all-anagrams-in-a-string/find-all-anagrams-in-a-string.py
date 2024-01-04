class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        return self.sol3(s,p)
    def sol3(self, s, p):
        need = Counter(p)
        window = Counter()
        l, r = 0, 0
        matched = 0
        res = []
        while r < len(s):
            c = s[r]
            window[c] += 1
            if c in need and window[c] == need[c]:
                matched += 1
            while matched == len(need):
                if r - l + 1 == len(p):
                    res.append(l)
                d = s[l]
                if d in need and window[d] == need[d]:
                    matched -= 1
                window[d] -= 1
                l += 1
            r += 1
        return res



    def sol2(self, s, p):
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
    def sol1(self, s, p):
        p_counter = Counter(p)
        s_counter = Counter()
        left,right = 0,0
        matched = 0
        res = []
        while right < len(s):
            c = s[right]
            s_counter[c] += 1
            if s_counter[c] == p_counter[c]:
                matched += 1
            while matched == len(p_counter) and right - left + 1 > len(p):
                left_c = s[left]
                s_counter[left_c] -= 1
                if s_counter[left_c] < p_counter[left_c]:
                    matched -= 1
                left += 1
            if right-left + 1 == len(p) and matched == len(p_counter):
                res.append(left)
            right += 1
        return res