class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        h = {2:"abc", 3:"def", 4:"ghi", 5:"jkl", 6:"mno", 7:"pqrs", 8:"tuv", 9:"wxyz"}
        res = []
        def bt(i, path):
            if len(path) == len(digits):
                res.append(path)
                return
            for c in h[int(digits[i])]:
                bt(i+1, path+c)
        bt(0, "")
        return res
