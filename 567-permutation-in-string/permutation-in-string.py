class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        return self.sol3(s1,s2)

    def sol3(self, s1,s2):
        if len(s1) > len(s2):
            return False
        need = Counter(s1)
        window = Counter()
        l, r = 0, 0
        matched = 0
        while r < len(s2):
            c = s2[r]
            window[c] += 1
            if c in need and window[c] == need[c]:
                matched += 1
            while matched == len(need):
                if len(s1) == r - l + 1:
                    return True
                d = s2[l]
                if d in need and window[d] == need[d]:
                    matched -= 1
                window[d] -= 1
                l += 1
            r += 1
        return False


    def sol2(self, s1, s2):
        if len(s1) > len(s2):
            return False
        h1 = Counter(s1)
        h2 = Counter(s2[:len(s1)])
        i = 0
        if h1 == h2:
            return True
        for i in range(1, len(s2) - len(s1) + 1):
            j = i + len(s1) - 1
            h2[s2[i-1]] -= 1
            h2[s2[j]] += 1
            if h1 == h2:
                return True
        return False
        
    def checkInclusion2(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        c1 = Counter(s1)
        c2 = Counter()
        matched = 0
        left = 0
        for right in range(0, len(s2)):
            c = s2[right]
            c2[c] += 1
            if c2[c] == c1[c]:
                matched += 1
            while matched == len(c1) and right - left + 1 > len(s1):
                left_c = s2[left]
                c2[left_c] -= 1
                left += 1
                if c2[left_c] < c1[left_c]:
                    matched -= 1
            if matched == len(c1) and right - left + 1 == len(s1):
                return True
        return False
            