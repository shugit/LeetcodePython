import re
class Solution:
    # @param {string} s
    # @return {boolean}
    def isPalindrome(self, s):
        if s is None or s == '':
            return True
        j = len(s) -1
        i=0
        isLetter = re.compile('^[\w]+$')
        while i < len(s):
            while i < len(s) and isLetter.match(s[i]) is None:
                #print 's[%d]=%r is skipped'%(i,s[i])
                i += 1
            while j >= 0 and isLetter.match(s[j]) is None:
                #print 's[%d]=%r is skipped'%(j,s[j])
                j -= 1
            if i > j:
                return True
            #print 's[%d]=%r,s[%d]=%r'%(i,s[i].lower(),j,s[j].lower())
            if s[i].lower() != s[j].lower():
                return False
            j -= 1
            i += 1
        return True





s = Solution()
#print s.isPalindrome('A man, a plan, a canal: Panama')
print s.isPalindrome('A man, a plan, a canal -- Panama')

#print s.isPalindrome('race a car')
#print s.isPalindrome(' ')
#print s.isPalindrome('a')