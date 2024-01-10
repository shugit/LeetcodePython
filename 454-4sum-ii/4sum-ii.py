class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        h = defaultdict(int)
        for n1 in nums1:
            for n2 in nums2:
                h[n1+n2]+=1
        res = 0
        for n3 in nums3:
            for n4 in nums4:
                # if -(n3+n4) in h:
                res += h[-(n3+n4)]
        return res