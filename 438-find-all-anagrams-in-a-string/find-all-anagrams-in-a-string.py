class Solution:
    def findAnagrams2(self, s: str, p: str) -> List[int]:
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

    def findAnagrams(self, s: str, p: str) -> List[int]:
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