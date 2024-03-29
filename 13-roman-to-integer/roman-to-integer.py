class Solution:
    def romanToInt(self, s: str) -> int:
        res = 0
        i = 0
        h = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        special = {'I':set(['V','X']),'X':set(['L','C']),'C':set(['D','M'])}
        while i < len(s):
            if s[i] in special and i+1 < len(s) and s[i+1] in special[s[i]]:
                res -= h[s[i]]
            else:
                res += h[s[i]]
            i += 1
        return res
            
