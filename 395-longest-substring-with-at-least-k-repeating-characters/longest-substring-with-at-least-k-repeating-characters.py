class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        c = Counter(s)
        left = 0
        maxi = 0
        for i, letter in enumerate(s):
            if c[letter] < k:
                left = self.longestSubstring(s[:i], k)
                right = self.longestSubstring(s[i+1:], k)
                return max(left, right)
        return len(s)