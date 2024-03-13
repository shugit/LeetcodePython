class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        h = {"6":"9", "9":"6", "8":"8", "1":"1", "0":"0"}
        res = ""
        for n in num:
            if n not in h:
                return False
            res += h[n]
        if num[::-1] == res:
            return True
        return False
