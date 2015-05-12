#unfinished
import math
class Solution:
    # @param {integer} n
    # @return {integer}
    def countPrimes(self, n):
        if n  == 2:
            return 0
        elif n == 3:
            return 1
        array = [-1]*int(n/2)
        max = int(math.sqrt(n))
        count = len(array)
        for i in range(1,n,2):
            array[i/2] = i
        for i in range(1,max):
            if array[i] != -1:
                for j in range(i+1,max):
                    if array[j]!=-1:
                        #print 'array[%d]=%d array[%d]=%d'%(i,array[i],j,array[j])
                        if array[j]%array[i] == 0:
                            #print 'eliminate'
                            array[j] = -1
                            count-= 1
        #print array
        return count


s = Solution()
print s.countPrimes(4002900)