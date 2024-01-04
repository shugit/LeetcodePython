class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        cnt = 0
        def mergeSort(arr):
            if len(arr) == 1:
                return arr
            mid = len(arr) //2
            l1 = mergeSort(arr[:mid])
            l2 = mergeSort(arr[mid:])
            nonlocal cnt
            merged = merge(l1, l2)
            # print(l1, l2, cnt)
            return merged
        def merge(l1, l2):
            nonlocal cnt
            res = []
            i, j = 0, 0
            while i < len(l1) and j < len(l2):
                if l1[i] <= 2 * l2[j]:
                    i += 1
                else:
                    cnt += len(l1) - i
                    j += 1
            return sorted(l1 + l2) 
        mergeSort(nums)        
        return cnt