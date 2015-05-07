class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        splits = s.split(' ')
        print splits
        result = ''
        for i in reversed(range(0, len(splits))):
            if splits[i]!='':
                result = result+splits[i].strip()+' '
        return result.strip()

s = Solution()
print s.reverseWords('the sky is blue')
print s.reverseWords('   a   b ')