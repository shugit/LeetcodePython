class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        def mergeSort(arr):
            if len(arr) == 1:
                return arr
            mid = len(arr) // 2
            l1 = mergeSort(arr[:mid])
            l2 = mergeSort(arr[mid:])
            merged = merge(l1, l2)
            # print(l1, l2, merged, res)
            return merged
        def merge(l1, l2):
            temp = []
            i, j = 0, 0
            while i < len(l1) and j < len(l2):
                if l1[i][0] <= l2[j][0]:
                    res[l1[i][1]] += j
                    temp.append(l1[i])
                    i += 1
                else:
                    temp.append(l2[j])
                    j += 1
            while i < len(l1):
                res[l1[i][1]] += j
                temp.append(l1[i])
                i += 1
            while j < len(l2):
                temp.append(l2[j])
                j += 1
            return temp
        res = [0] * len(nums)
        arr = [[n, i] for i, n in enumerate(nums)]
        mergeSort(arr)
        return res
        