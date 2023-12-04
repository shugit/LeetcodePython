class Solution:
    def checkInclusion2(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        h1 = {}
        h2 = {}
        for i in range(0, 26):
            c = chr(ord("a") + i)
            h1[c] = 0
            h2[c] = 0
        for s in s1:
            h1[s] += 1
        i = 0
        n = len(s1)
        for i in range(0, n):
            h2[s2[i]] += 1
        def match(h1,h2):
            # print(h1,h2)
            for i in range(0, 26):
                c = chr(ord("a") + i)
                if h1[c] != h2[c]:
                    return False
            return True
        if match(h1,h2):
            return True
        for i in range(1, len(s2) - len(s1) + 1):
            j = i + len(s1) - 1
            h2[s2[i-1]] -= 1
            h2[s2[j]] += 1
            if match(h1,h2):
                return True
        return False
        
    def checkInclusion(self, s1: str, s2: str) -> bool:
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
            