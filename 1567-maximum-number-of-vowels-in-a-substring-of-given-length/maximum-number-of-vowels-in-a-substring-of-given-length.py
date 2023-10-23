class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        l = 0
        cur = 0
        vowels = set(['a','e','i','o','u'])
        maxi = 0
        for r in range(0, len(s)):
            if s[r] in vowels:
                cur += 1
            maxi = max(maxi, cur)
            if r - l + 1 >= k:
                if s[l] in vowels:
                    cur -= 1
                l += 1
        return maxi