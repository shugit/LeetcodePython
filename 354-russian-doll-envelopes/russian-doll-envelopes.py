class Solution2:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda x:(x[0], -x[1]))
        # print(envelopes)
        n = len(envelopes)
        dp = [1] * n
        for i in range(0, n):
            for j in range(0, i):
                if envelopes[j][1] < envelopes[i][1]:
                    dp[i] = max(dp[i], dp[j]+1)
        # print(dp)
        return max(dp)

class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda x: (x[0], -x[1]))        
        res = []
        for _, h in envelopes:
            idx = bisect_left(res, h)
            if idx == len(res):
                res.append(h)
            else:
                res[idx]=h
        return len(res)                                                                                              