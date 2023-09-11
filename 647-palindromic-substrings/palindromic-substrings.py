class Solution:
    def countSubstrings(self, s: str) -> int:
        size = len(s)
        dp = [[False for _ in range(size)] for _ in range(size)]
        cnt = 0
        for length in range(1,size+1):
            limit = size - length
            for left in range(0, limit + 1):
                right = left + length - 1
                if left == right:
                    dp[left][right] = True
                    cnt += 1
                    continue
                if s[left] == s[right]:
                    if left + 1 == right:
                        dp[left][right] = True
                        cnt += 1
                        continue
                    if dp[left+1][right-1] == True:
                        dp[left][right] = True
                        cnt += 1
        # print(dp)
        return cnt
                        
