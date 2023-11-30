class Solution:
    def longestValidSubstring(self, word: str, forbidden: List[str]) -> int:
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