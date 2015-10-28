class Solution:
    # @param {string} s
    # @param {string} t
    # @return {boolean}
    def isIsomorphic(self, s, t):
        dict_st = dict()
        for i in range(len(s)):
            if dict_st.get(s[i]) is None:
                for value in dict_st.values():
                    if value == t[i]:
                        return False
                dict_st[s[i]] = t[i]
            else:
                if dict_st[s[i]] != t[i]:
                    return False

        return True



s = Solution()
#print s.isIsomorphic('egg','add')
#print s.isIsomorphic('foo','bar')
#print s.isIsomorphic('foo','b--')
print s.isIsomorphic('ab','aa')