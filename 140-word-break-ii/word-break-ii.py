class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        return self.topDown(s, wordDict)

    def topDown(self, s: str, wordDict: List[str]) -> List[str]:
        words = set(wordDict)
        path = []
        res = []
        def backtrack(i):
            if i == len(s):
                res.append(" ".join(path))
            for w in words:
                if i + len(w) <= len(s) and s[i: i+ len(w)] == w:
                    path.append(w)
                    backtrack(i+len(w))
                    path.pop()
        backtrack(0)
        return res



    def downTop(self, s: str, wordDict: List[str]) -> List[str]:
        path = []
        return path