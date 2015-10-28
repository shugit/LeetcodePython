def add_all(s):
    my_sum = 0
    for i in range(len(s)):
        my_sum += pow(int(s[i]),2)
        #print 's[%d]=%d,sum=%d'%(i,int(s[i]),my_sum)
    #print my_sum
    return  my_sum


class Solution:
    # @param {integer} n
    # @return {boolean}
    def isHappy(self, n):
        s = str(n)
        my_sum = add_all(s)
        while my_sum >= 10:
            my_sum = add_all(str(my_sum))
        return True if my_sum== 1 else False


s = Solution()
print s.isHappy(7)
#print s.isHappy(72)