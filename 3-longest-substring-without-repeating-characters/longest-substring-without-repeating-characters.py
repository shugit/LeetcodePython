class Solution:
    def lengthOfLongestSubstring2(self, s: str) -> int:
        if len(s) == 0:
            return 0
        res = float("-inf")
        h = {}
        l = 0
        for r in range(len(s)):
            if s[r] not in h or h[s[r]] == 0:
                h[s[r]] = 1
                res = max(res, r - l + 1)
            else:
                h[s[r]] += 1
                while l < r and h[s[r]] > 1: 
                    h[s[l]] -= 1
                    l += 1
        return res

    def lengthOfLongestSubstring(self, s: str) -> int:
        h = set()
        l = 0
        res = 0
        for r in range(len(s)):
            while s[r] in h:
                h.remove(s[l])
                l += 1
            h.add(s[r])
            res = max(res, r-l+ 1)
        return res

    def lengthOfLongestSubstring3(self, s: str) -> int:
            c = Counter()
            left = 0
            res = 0
            for right in range(0, len(s)):
                c[s[right]] += 1
                while c[s[right]] > 1:
                    c[s[left]] -= 1
                    left += 1
                res = max(res, right - left + 1)
            return res
