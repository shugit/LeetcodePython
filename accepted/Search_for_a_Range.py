def find(nums, target,offset,range):
    half = int(len(nums)/2)
    print '%r, middle is %d, offset is %d,range is %r'%(nums,nums[half],offset,range)
    if half == 0:
        if target!=nums[half]:
            return # Didn't find anything
        else:
            setRange(range,offset+half)
    else:
        if target == nums[half]:
            setRange(range,offset+half)
        if nums[half]>= target: find(nums[0:half],target,offset,range)
        if nums[half]<= target: find(nums[half:len(nums)],target,offset+half,range)

def setRange(range,index):
    if range[0] == -1 or (range[0]!=-1 and index<range[0]):
            range[0] = index
    if range[1] == -1 or index > range[1]:
        range[1] = index


class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def searchRange(self, nums, target):
        range = [-1,-1]
        find(nums,target,0,range)
        #return surround(index,nums) if index is not None else [-1,-1]
        return range




s = Solution()
#print s.searchRange([5, 7, 7, 8, 8, 10] ,8)
#should be [3, 4]
#print s.searchRange([0,1,1,1,1,2,3] ,1)
print s.searchRange([1,1,1,2,3,3,4,5,6,7,8,9,9,9,9,9,9,9,9] ,3)
#print s.searchRange([1] ,1)