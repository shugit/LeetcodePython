class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        l, r = 0, k-1
        total = sum(arr[:r])
        res = 0
        while r < len(arr):
            total += arr[r]
            if total/k >= threshold:
                res += 1
            total -= arr[l]
            l += 1
            r += 1
        return res