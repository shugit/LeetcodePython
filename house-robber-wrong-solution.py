
class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def rob(self, nums):
        if nums is None:
            return 0
        table = dict()
        for i in range(len(nums)):
            if table.get(nums[i]) is None:
                table[nums[i]] = [i]
            else:
                table[nums[i]].append(i)
        sorted_table = sorted(table.iteritems(),None,None,True)
        #print sorted_table
        sum = 0
        robbed = []
        for key,t in enumerate(sorted_table):
            #print t
            for house_number in t[1]:
                if house_number in robbed or house_number-1 in robbed or house_number+1 in robbed:
                    #print 'house no.%d is adjancent,pass'%(house_number)
                    pass
                else:
                    #print 'house no.%d is robbed'%(house_number)
                    robbed.append(t[1][0])
                    sum += t[0]
        #print robbed
        return sum


s = Solution()
#print s.rob([23,31,15,1,2,10,39,1,4,29,15,29,10])
#method 1: sort O(n) = log(n)
#method 2: find max O(n) = n^2
#print s.rob([0,0])
#print s.rob([0])
#print s.rob([1])
print s.rob([2,3,2])