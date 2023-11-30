class Solution:
    def longestValidSubstring2(self, word: str, forbidden: List[str]) -> int:
        def build_trie():
            root = {}
            for w in forbidden:
                curr = root
                for c in w:
                    if c not in curr:
                        curr[c] = {}
                    curr = curr[c]
                curr["*"] = True
            return root
        root = build_trie()

        def isForbidden(w):
            curr = root
            length = 0
            for c in w:
                if c not in curr:
                    return 0
                curr = curr[c]
                length += 1
                if "*" in curr:
                    return length
            return 0
        j = len(word)
        maxi = 0
        for i in range(len(word) -1, -1 , -1):
            length = isForbidden(word[i:j])
            if length > 0:
                j = i + length - 1
            # print(length, j-i)
            maxi = max(maxi, j-i)
        return maxi

    def longestValidSubstring(self, word: str, forbidden: List[str]) -> int:
        s = set(forbidden)
        n = len(word)
        left = 0
        ans = 0
        for right in range(0, len(word)):
            cur = right
            while cur >= left and cur > right - 10:
                if word[cur:right + 1] in s:
                    left = cur + 1
                    break
                cur -= 1
            ans = max(ans, right - left + 1)
        return ans