class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        # res = right
        while left < right:
            mid = left + (right - left) // 2
            cnt = 0
            for p in piles:
                if p <= mid:
                    cnt += 1
                elif p % mid == 0:
                    cnt += (p/mid)
                else:
                    cnt += (p//mid) + 1
            # print(mid, cnt)
            if cnt <= h:
                right = mid
                # res = min(res, mid)
            else:
                left = mid + 1
        # return res
        return right