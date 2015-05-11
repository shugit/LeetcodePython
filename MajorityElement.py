class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def majorityElement(self, nums):
        threshold = 1.0*len(nums)/2
        table = dict()
        for num in nums:
            if table.get(num) is None:
                table[num] = 0
            table[num]+= 1
        print table
        print 'threshold='+str(threshold)
        for key,value in table.iteritems():
            if value >= threshold:
                return key


s = Solution()
#print s.majorityElement([2,2,2,2,2,3,4,5,6])
#print s.majorityElement([1])
print s.majorityElement([8,8,7,7,7])