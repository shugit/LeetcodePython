class Solution:
    def longestSubstring(self, s: str, k: int) -> int:

        def find(s):
            if len(s) < k:
                return 0
            c = Counter(s)
            for i, letter in enumerate(s):
                if c[letter] < k:
                    left = find(s[:i])
                    right = find(s[i+1:])
                    return max(left, right)
            return len(s)
        return find(s)